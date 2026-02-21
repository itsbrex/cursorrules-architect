"""Shared locking primitives for ExecPlan mutations."""

from __future__ import annotations

import os
import re
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import BinaryIO, Callable, cast

try:
    import fcntl
except ImportError:  # pragma: no cover - not available on Windows.
    fcntl = None

try:
    import msvcrt
except ImportError:  # pragma: no cover - not available on POSIX.
    msvcrt = None


EXECPLAN_ID_RE = re.compile(r"^EP-\d{8}-\d{3}$")
_WINDOWS_LOCK_RETRIES = 200
_WINDOWS_LOCK_RETRY_DELAY_SECONDS = 0.05
_LOCKS_DIRNAME = ".locks"


def _acquire_windows_lock(lock_handle: BinaryIO) -> None:
    if msvcrt is None:
        raise RuntimeError("msvcrt backend is unavailable.")

    locking_func = getattr(msvcrt, "locking", None)
    nonblocking_lock_mode = getattr(msvcrt, "LK_NBLCK", None)
    if locking_func is None or nonblocking_lock_mode is None:
        raise RuntimeError("msvcrt backend does not expose required locking symbols.")

    lock = cast(Callable[[int, int, int], None], locking_func)

    lock_handle.seek(0, os.SEEK_END)
    if lock_handle.tell() == 0:
        lock_handle.write(b"\0")
        lock_handle.flush()
        os.fsync(lock_handle.fileno())

    for _ in range(_WINDOWS_LOCK_RETRIES):
        try:
            lock_handle.seek(0)
            lock(lock_handle.fileno(), int(nonblocking_lock_mode), 1)
            return
        except OSError:
            time.sleep(_WINDOWS_LOCK_RETRY_DELAY_SECONDS)

    raise TimeoutError("Could not acquire lock within retry budget.")


def _release_windows_lock(lock_handle: BinaryIO) -> None:
    if msvcrt is None:
        raise RuntimeError("msvcrt backend is unavailable.")

    locking_func = getattr(msvcrt, "locking", None)
    unlock_mode = getattr(msvcrt, "LK_UNLCK", None)
    if locking_func is None or unlock_mode is None:
        raise RuntimeError("msvcrt backend does not expose required locking symbols.")

    lock = cast(Callable[[int, int, int], None], locking_func)
    lock_handle.seek(0)
    lock(lock_handle.fileno(), int(unlock_mode), 1)


@contextmanager
def file_lock(lock_path: Path) -> Iterator[None]:
    """Acquire an exclusive process lock at lock_path."""
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+b") as lock_handle:
        if fcntl is not None:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        elif msvcrt is not None:
            _acquire_windows_lock(lock_handle)
        else:
            raise RuntimeError("No supported file-locking backend available.")
        try:
            yield
        finally:
            if fcntl is not None:
                fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
            elif msvcrt is not None:
                _release_windows_lock(lock_handle)


def get_execplan_lock_path(*, execplans_dir: Path, execplan_id: str) -> Path:
    """Return the stable lock path used for all mutations for one ExecPlan."""
    if EXECPLAN_ID_RE.fullmatch(execplan_id) is None:
        raise ValueError(f"Invalid ExecPlan ID {execplan_id!r}. Expected EP-YYYYMMDD-NNN.")
    resolved_execplans_dir = execplans_dir.resolve()
    if not resolved_execplans_dir.exists():
        raise FileNotFoundError(f"ExecPlans directory not found: {resolved_execplans_dir}")
    return (resolved_execplans_dir / _LOCKS_DIRNAME / f"{execplan_id}.lock").resolve()


@contextmanager
def execplan_mutation_lock(*, execplans_dir: Path, execplan_id: str) -> Iterator[None]:
    """
    Serialize all mutations (milestone create/archive and plan archive) for one ExecPlan ID.
    """
    lock_path = get_execplan_lock_path(execplans_dir=execplans_dir, execplan_id=execplan_id)
    with file_lock(lock_path):
        yield
