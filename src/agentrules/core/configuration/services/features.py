"""Feature toggle helpers."""

from __future__ import annotations

from ..models import CLIConfig, ResearcherMode
from ..utils import normalize_researcher_mode


def set_researcher_mode(config: CLIConfig, mode: str | None) -> None:
    config.features.researcher_mode = normalize_researcher_mode(mode, default="auto")


def get_researcher_mode(config: CLIConfig, default: ResearcherMode = "auto") -> ResearcherMode:
    normalized = normalize_researcher_mode(config.features.researcher_mode, default=default)
    config.features.researcher_mode = normalized
    return normalized


def is_researcher_enabled(
    config: CLIConfig,
    *,
    offline_mode: bool,
    has_tavily_credentials: bool,
) -> bool:
    mode = normalize_researcher_mode(config.features.researcher_mode, default="auto")

    if offline_mode:
        return True
    if mode == "on":
        return True
    if mode == "off":
        return False
    return has_tavily_credentials

