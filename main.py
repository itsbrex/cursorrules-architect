from __future__ import annotations

try:
    from agentrules.cli import app
except ModuleNotFoundError:  # pragma: no cover - exercised when running locally without install
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parent
    src_path = project_root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))

    from agentrules.cli import app

if __name__ == "__main__":
    app()
