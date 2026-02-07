"""Helpers for canonical ExecPlan identity derived from filenames."""

from __future__ import annotations

import re

EXECPLAN_FILENAME_RE = re.compile(
    r"^(?P<id>EP-(?P<date>\d{8})-(?P<sequence>\d{3}))(?:$|[_-].*)"
)


def parse_execplan_filename(filename: str) -> tuple[str, str, int] | None:
    """
    Parse canonical ExecPlan identity from a filename.

    Returns (id, date_token, sequence) when the filename starts with
    EP-YYYYMMDD-NNN, optionally followed by suffix text.
    """
    match = EXECPLAN_FILENAME_RE.match(filename)
    if match is None:
        return None
    plan_id = match.group("id")
    date_token = match.group("date")
    sequence = int(match.group("sequence"))
    return plan_id, date_token, sequence


def extract_execplan_id_from_filename(filename: str) -> str | None:
    parsed = parse_execplan_filename(filename)
    if parsed is None:
        return None
    plan_id, _, _ = parsed
    return plan_id
