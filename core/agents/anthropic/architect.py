"""Anthropic provider implementation of ``BaseArchitect``."""
from __future__ import annotations

import json
import logging
from typing import Any

from core.agents.base import BaseArchitect, ModelProvider, ReasoningMode

from .client import execute_message_request
from .prompting import default_prompt_template, format_prompt
from .request_builder import PreparedRequest, prepare_request
from .response_parser import parse_response
from .tooling import resolve_tool_config

logger = logging.getLogger("project_extractor")


class AnthropicArchitect(BaseArchitect):
    """Architect class for interacting with Anthropic's Claude models."""

    def __init__(
        self,
        model_name: str = "claude-sonnet-4-5",
        reasoning: ReasoningMode = ReasoningMode.DISABLED,
        name: str | None = None,
        role: str | None = None,
        responsibilities: list[str] | None = None,
        prompt_template: str | None = None,
        tools_config: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            provider=ModelProvider.ANTHROPIC,
            model_name=model_name,
            reasoning=reasoning,
            name=name,
            role=role,
            responsibilities=responsibilities,
            tools_config=tools_config,
        )
        self.prompt_template = prompt_template or default_prompt_template()

    # Public API -----------------------------------------------------------------
    def format_prompt(self, context: dict[str, Any]) -> str:
        return format_prompt(
            template=self.prompt_template,
            agent_name=self.name or "Claude Architect",
            agent_role=self.role or "analyzing the project",
            responsibilities=self.responsibilities,
            context=context,
        )

    async def analyze(self, context: dict[str, Any], tools: list[Any] | None = None) -> dict[str, Any]:
        try:
            prompt = context.get("formatted_prompt") or self.format_prompt(context)
            provider_tools = resolve_tool_config(tools, self.tools_config)
            prepared = self._prepare_request(prompt, provider_tools)

            from core.utils.model_config_helper import get_model_config_name  # Local import to avoid cycles

            model_config_name = get_model_config_name(self)
            agent_name = self.name or "Claude Architect"
            detail_parts: list[str] = []
            if "thinking" in prepared.payload:
                thinking = prepared.payload["thinking"]
                if isinstance(thinking, dict):
                    budget = thinking.get("budget_tokens")
                    detail = thinking.get("type")
                    if detail == "enabled" and budget:
                        detail_parts.append(f"with thinking (budget={budget})")
                    elif detail:
                        detail_parts.append(f"with thinking ({detail})")
            if provider_tools:
                detail_parts.append("with tools enabled")

            detail_suffix = f" ({', '.join(detail_parts)})" if detail_parts else ""
            logger.info(
                f"[bold purple]{agent_name}:[/bold purple] Sending request to {self.model_name} "
                f"(Config: {model_config_name}){detail_suffix}"
            )

            response = execute_message_request(prepared.payload)

            logger.info(
                f"[bold green]{agent_name}:[/bold green] Received response from {self.model_name}"
            )

            parsed = parse_response(response)
            results: dict[str, Any] = {
                "agent": agent_name,
                "findings": parsed.findings,
                "tool_calls": parsed.tool_calls,
            }

            if parsed.tool_calls:
                logger.info(
                    f"[bold purple]{agent_name}:[/bold purple] Model requested tool call(s)."
                )

            return results
        except Exception as exc:  # pragma: no cover - defensive logging
            agent_name = self.name or "Claude Architect"
            logger.error(f"[bold red]Error in {agent_name}:[/bold red] {str(exc)}")
            return {
                "agent": agent_name,
                "error": str(exc),
            }

    async def create_analysis_plan(self, phase1_results: dict, prompt: str | None = None) -> dict[str, Any]:
        context: dict[str, Any] = {"phase1_results": phase1_results}
        if prompt:
            context["formatted_prompt"] = prompt
        result = await self.analyze(context)
        response: dict[str, Any] = {
            "plan": result.get("findings", "No plan generated"),
            "error": result.get("error"),
        }
        if result.get("tool_calls"):
            response["tool_calls"] = result["tool_calls"]
        return response

    async def synthesize_findings(self, phase3_results: dict, prompt: str | None = None) -> dict[str, Any]:
        context: dict[str, Any] = {"phase3_results": phase3_results}
        if prompt:
            context["formatted_prompt"] = prompt
        result = await self.analyze(context)
        response: dict[str, Any] = {
            "analysis": result.get("findings", "No synthesis generated"),
            "error": result.get("error"),
        }
        if result.get("tool_calls"):
            response["tool_calls"] = result["tool_calls"]
        return response

    async def final_analysis(self, consolidated_report: dict, prompt: str | None = None) -> dict[str, Any]:
        context: dict[str, Any] = {"consolidated_report": consolidated_report}
        if prompt:
            context["formatted_prompt"] = prompt
        result = await self.analyze(context)
        response: dict[str, Any] = {
            "analysis": result.get("findings", "No final analysis generated"),
            "error": result.get("error"),
        }
        if result.get("tool_calls"):
            response["tool_calls"] = result["tool_calls"]
        return response

    async def consolidate_results(self, all_results: dict, prompt: str | None = None) -> dict[str, Any]:
        content = prompt or (
            "Consolidate these results into a comprehensive report:\n\n"
            f"{json.dumps(all_results, indent=2)}"
        )

        result = await self.analyze({"formatted_prompt": content})
        response: dict[str, Any] = {
            "phase": "Consolidation",
            "report": result.get("findings", "No report generated"),
        }
        if result.get("error"):
            response["error"] = result["error"]
        if result.get("tool_calls"):
            response["tool_calls"] = result["tool_calls"]
        return response

    # Internal helpers -----------------------------------------------------------
    def _prepare_request(
        self,
        prompt: str,
        tools: list[Any] | None,
    ) -> PreparedRequest:
        return prepare_request(
            model_name=self.model_name,
            prompt=prompt,
            reasoning=self.reasoning,
            tools=tools,
        )


__all__ = ["AnthropicArchitect"]
