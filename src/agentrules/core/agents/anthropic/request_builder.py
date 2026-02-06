"""Helpers for constructing Anthropic Messages API payloads."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from agentrules.core.agents.base import ReasoningMode

DEFAULT_MAX_TOKENS = 20_000
DEFAULT_THINKING_BUDGET = 16_000


@dataclass(frozen=True)
class PreparedRequest:
    """Container for a ready-to-dispatch Anthropic request."""

    payload: dict[str, Any]


def prepare_request(
    *,
    model_name: str,
    prompt: str,
    reasoning: ReasoningMode,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    tools: list[Any] | None,
) -> PreparedRequest:
    payload: dict[str, Any] = {
        "model": model_name,
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    thinking = _build_thinking_payload(model_name=model_name, reasoning=reasoning)
    if thinking is not None:
        payload["thinking"] = thinking

    if tools:
        payload["tools"] = tools

    return PreparedRequest(payload=payload)


def _build_thinking_payload(*, model_name: str, reasoning: ReasoningMode) -> dict[str, Any] | None:
    if reasoning == ReasoningMode.ENABLED:
        return {"type": "enabled", "budget_tokens": DEFAULT_THINKING_BUDGET}

    if reasoning == ReasoningMode.DYNAMIC:
        # Claude Opus 4.6 introduced "adaptive" thinking mode. Other models do not
        # support it; fail fast so callers get an actionable error instead of a
        # confusing API 400.
        if _supports_adaptive_thinking(model_name):
            return {"type": "adaptive"}
        raise ValueError(
            "Adaptive thinking (ReasoningMode.DYNAMIC) is only supported for Claude Opus 4.6 "
            "(model 'claude-opus-4-6'). Use ReasoningMode.ENABLED for fixed-budget thinking "
            "on other Claude models."
        )

    if reasoning == ReasoningMode.DISABLED:
        return None

    return None


def _supports_adaptive_thinking(model_name: str) -> bool:
    normalized = model_name.strip().lower()
    return normalized == "claude-opus-4-6" or normalized.startswith("claude-opus-4-6-")
