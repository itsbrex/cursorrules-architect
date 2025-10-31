"""
Typer-based command-line interface for the CursorRules Architect pipeline.
"""

from __future__ import annotations

import asyncio
import os
import time
from pathlib import Path
from textwrap import dedent
from typing import Any, Dict, List, Optional, Tuple

import questionary
import typer
from dotenv import load_dotenv
from rich.console import Console

from agentrules.analyzer import ProjectAnalyzer
from agentrules.config_service import (
    PROVIDER_ENV_MAP,
    apply_config_to_environment,
    get_current_provider_keys,
    set_phase_model,
    set_provider_key,
)
from agentrules.logging_setup import configure_logging
from agentrules import model_config

app = typer.Typer(
    name="agentrules",
    help="Analyze a project and generate Cursor rules using multi-provider AI agents.",
    invoke_without_command=True,
    add_completion=False,
)


def _load_env_files() -> None:
    env_path = Path(".env")
    if env_path.exists():
        load_dotenv(env_path)


def _activate_offline_mode(console: Console) -> None:
    if os.getenv("OFFLINE", "0") != "1":
        return
    try:
        from core.utils.offline import patch_factory_offline

        patch_factory_offline()
        console.print("[yellow]OFFLINE=1 detected: using DummyArchitects (no network calls).[/]")
    except Exception as error:
        console.print(f"[red]Failed to enable OFFLINE mode: {error}[/]")


def _run_pipeline(directory: Path, offline: bool, console: Console) -> None:
    if offline:
        os.environ["OFFLINE"] = "1"
    _activate_offline_mode(console)

    analyzer = ProjectAnalyzer(directory, console)
    start_time = time.time()
    try:
        asyncio.run(analyzer.analyze())
    except RuntimeError:
        # Fallback for already-running loops (e.g., inside notebooks)
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(analyzer.analyze())
        finally:
            loop.close()
    analyzer.persist_outputs(start_time)
    console.print(f"\n[green]Analysis finished for:[/] {directory}")


def _masked(key: Optional[str]) -> str:
    if not key:
        return "[not set]"
    if len(key) <= 6:
        return "*" * len(key)
    return f"{key[:3]}…{key[-3:]}"


def _configure_keys(console: Console) -> None:
    console.print("\n[bold]Configure Provider API Keys[/bold]")
    console.print("Select a provider to update. Leave the key blank to keep the current value.\n")

    updated = False

    while True:
        current_keys = get_current_provider_keys()
        choices: List[questionary.Choice] = []
        for provider, env_var in PROVIDER_ENV_MAP.items():
            display_label = f"{provider.title()} ({env_var}) [{_masked(current_keys.get(provider))}]"
            choices.append(questionary.Choice(title=display_label, value=provider))
        choices.append(questionary.Choice(title="Done", value="__DONE__"))

        selection = questionary.select(
            "Select provider to configure:",
            choices=choices,
            qmark="🔐",
        ).ask()

        if selection is None:
            console.print("[yellow]Configuration cancelled.[/]")
            return
        if selection == "__DONE__":
            break

        env_var = PROVIDER_ENV_MAP[selection]
        current_display = _masked(current_keys.get(selection))
        answer = questionary.password(
            f"Enter {selection.title()} API key ({env_var}) [{current_display}]:",
            qmark="🔐",
            default="",
        ).ask()

        if answer is None:
            console.print("[yellow]Configuration cancelled.[/]")
            return

        trimmed = answer.strip()
        if trimmed:
            set_provider_key(selection, trimmed)
            updated = True
            console.print(f"[green]{selection.title()} key updated.[/]")
        else:
            console.print("[dim]No changes made.[/]")

    if updated:
        model_config.apply_user_overrides()
        console.print("[green]Provider keys updated.[/]")
    else:
        console.print("[dim]No provider keys changed.[/]")


def _configure_models(console: Console) -> None:
    console.print("\n[bold]Configure model presets per phase[/bold]")
    console.print("Select a phase to adjust its model preset. Choose 'Reset to default' inside the phase menu to revert.\n")

    provider_keys = get_current_provider_keys()
    active = model_config.get_active_presets()
    updated = False

    def _split_preset_label(label: str) -> Tuple[str, Optional[str]]:
        if " (" in label and label.endswith(")"):
            base, remainder = label.split(" (", 1)
            return base, remainder[:-1]
        return label, None

    def _variant_display_text(variant_label: Optional[str]) -> str:
        if not variant_label:
            return "Default"
        return variant_label[0].upper() + variant_label[1:]

    while True:
        phase_choices: List[questionary.Choice] = []
        handled_phases: set[str] = set()

        def _current_display(key: Optional[str]) -> str:
            info = model_config.get_preset_info(key) if key else None
            if not info:
                return "Not configured"
            return f"{info.label} [{info.provider_display}]"

        for phase in model_config.PHASE_SEQUENCE:
            if phase in handled_phases:
                continue

            if phase == "phase1" and "researcher" in model_config.PHASE_SEQUENCE:
                header_title = model_config.get_phase_title("phase1")
                phase_choices.append(questionary.Separator(header_title))

                general_key = active.get("phase1", model_config.get_default_preset_key("phase1"))
                general_label = _current_display(general_key)
                phase_choices.append(
                    questionary.Choice(
                        title=f"├─ General Agents [{general_label}]",
                        value="phase1",
                    )
                )

                researcher_key = active.get("researcher", model_config.get_default_preset_key("researcher"))
                researcher_label = _current_display(researcher_key)
                researcher_title = model_config.get_phase_title("researcher")
                phase_choices.append(
                    questionary.Choice(
                        title=f"└─ {researcher_title} [{researcher_label}]",
                        value="researcher",
                    )
                )

                handled_phases.update({"phase1", "researcher"})
                continue

            title = model_config.get_phase_title(phase)
            current_key = active.get(phase, model_config.get_default_preset_key(phase))
            display_label = _current_display(current_key)
            phase_choices.append(questionary.Choice(title=f"{title} [{display_label}]", value=phase))
            handled_phases.add(phase)

        phase_choices.append(questionary.Choice(title="Done", value="__DONE__"))

        phase_selection = questionary.select(
            "Select phase to configure:",
            choices=phase_choices,
            qmark="🧠",
        ).ask()

        if phase_selection is None:
            console.print("[yellow]Model configuration cancelled.[/]")
            return
        if phase_selection == "__DONE__":
            break

        phase = phase_selection
        title = model_config.get_phase_title(phase)
        presets = model_config.get_available_presets_for_phase(phase, provider_keys)
        if not presets:
            console.print(f"[yellow]No presets available for {title}; configure provider keys first.[/]")
            continue

        default_key = model_config.get_default_preset_key(phase)
        current_key = active.get(phase, default_key)
        default_info = model_config.get_preset_info(default_key) if default_key else None

        model_choices: List[questionary.Choice] = []
        if default_info:
            model_choices.append(
                questionary.Choice(
                    title=f"Reset to default ({default_info.label} – {default_info.provider_display})",
                    value="__RESET__",
                )
            )
        else:
            model_choices.append(questionary.Choice(title="Reset to default", value="__RESET__"))

        grouped_entries: List[Dict[str, Any]] = []
        grouped_lookup: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
        for preset in presets:
            base_label, variant_label = _split_preset_label(preset.label)
            group_key = (preset.provider_slug, base_label, preset.provider_display)
            if group_key not in grouped_lookup:
                grouped_lookup[group_key] = {
                    "base_label": base_label,
                    "provider_display": preset.provider_display,
                    "variants": [],
                }
                grouped_entries.append(grouped_lookup[group_key])
            grouped_lookup[group_key]["variants"].append(
                {
                    "preset": preset,
                    "preset_key": preset.key,
                    "variant_label": variant_label,
                    "variant_display": _variant_display_text(variant_label),
                }
            )

        group_selection_map: Dict[str, Dict[str, Any]] = {}
        for idx, entry in enumerate(grouped_entries):
            variants = entry["variants"]
            if len(variants) == 1:
                variant = variants[0]
                title_label = f"{entry['base_label']} [{entry['provider_display']}]"
                if variant["preset_key"] == default_key:
                    title_label += " (default)"
                if variant["preset_key"] == current_key:
                    title_label += " [current]"
                model_choices.append(questionary.Choice(title=title_label, value=variant["preset_key"]))
            else:
                current_variant = next((v for v in variants if v["preset_key"] == current_key), None)
                default_variant = next((v for v in variants if v["preset_key"] == default_key), None)
                summary = f"{entry['base_label']} [{entry['provider_display']}] – {len(variants)} options"
                if current_variant:
                    summary += f" (current: {current_variant['variant_display']})"
                elif default_variant:
                    summary += f" (default: {default_variant['variant_display']})"
                group_value = f"__GROUP__{idx}"
                model_choices.append(questionary.Choice(title=summary, value=group_value))
                group_selection_map[group_value] = {
                    "entry": entry,
                    "variants": variants,
                    "current_key": current_key,
                    "default_key": default_key,
                }

        default_value = model_choices[0].value
        if current_key and any(choice.value == current_key for choice in model_choices):
            default_value = current_key
        else:
            for group_value, group_data in group_selection_map.items():
                if any(v["preset_key"] == current_key for v in group_data["variants"]):
                    default_value = group_value
                    break
            else:
                if default_key and any(choice.value == default_key for choice in model_choices):
                    default_value = default_key
                else:
                    for group_value, group_data in group_selection_map.items():
                        if any(v["preset_key"] == default_key for v in group_data["variants"]):
                            default_value = group_value
                            break

        selection = questionary.select(
            f"{title}:",
            choices=model_choices,
            default=default_value,
            qmark="🧠",
        ).ask()

        if selection is None:
            console.print("[yellow]Model configuration cancelled.[/]")
            return

        if selection in group_selection_map:
            group_data = group_selection_map[selection]
            entry = group_data["entry"]
            variants = group_data["variants"]

            variant_choices: List[questionary.Choice] = []
            for variant in variants:
                variant_title = variant["variant_display"]
                if variant["preset_key"] == group_data["default_key"]:
                    variant_title += " (default)"
                if variant["preset_key"] == group_data["current_key"]:
                    variant_title += " [current]"
                variant_choices.append(questionary.Choice(title=variant_title, value=variant["preset_key"]))

            preferred_default = group_data["current_key"] or group_data["default_key"]
            if not preferred_default or not any(choice.value == preferred_default for choice in variant_choices):
                preferred_default = variant_choices[0].value

            selection = questionary.select(
                f"{entry['base_label']} [{entry['provider_display']}] – choose variant:",
                choices=variant_choices,
                default=preferred_default,
                qmark="🧠",
            ).ask()

            if selection is None:
                console.print("[yellow]Model configuration cancelled.[/]")
                return

        if selection == "__RESET__":
            set_phase_model(phase, None)
            active.pop(phase, None)
            console.print(f"[green]{title} reset to default preset.[/]")
        else:
            set_phase_model(phase, selection)
            active[phase] = selection
            preset_info = model_config.get_preset_info(selection)
            if preset_info:
                console.print(f"[green]{title} now uses {preset_info.label} [{preset_info.provider_display}].[/]")
            else:
                console.print(f"[green]{title} preset updated.[/]")
        updated = True

    if updated:
        overrides = {phase: key for phase, key in active.items() if phase in model_config.PHASE_SEQUENCE}
        model_config.apply_user_overrides(overrides)
        console.print("[green]Model selections saved.[/]")
        model_config.apply_user_overrides()
    else:
        console.print("[dim]No model presets changed.[/]")


def _show_keys(console: Console) -> None:
    console.print("\n[bold]Current Provider Configuration[/bold]")
    for provider, key in get_current_provider_keys().items():
        console.print(f"- {provider.title():<10}: {_masked(key)}")
    console.print("")


def _interactive_menu(console: Console) -> None:
    banner = dedent(
        """
        [bold cyan]
         █████╗  ██████╗ ███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
        ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
        ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ███████╗█████╗
        ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ╚════██║██╔══╝
        ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████║███████╗
        ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
        [/bold cyan]
        """
    )
    console.print(banner)

    menu_choices = {
        "Analyze current directory": "analyze_current",
        "Analyze another path": "analyze_other",
        "Configure provider API keys": "configure_keys",
        "Configure models per phase": "configure_models",
        "Show configured providers": "show_keys",
        "Exit": "exit",
    }

    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=list(menu_choices.keys()),
            qmark="🤖",
        ).ask()

        if choice is None or menu_choices[choice] == "exit":
            console.print("Goodbye!")
            return

        action = menu_choices[choice]
        if action == "analyze_current":
            _run_pipeline(Path.cwd(), offline=False, console=console)
        elif action == "analyze_other":
            path_answer = questionary.path("Target project directory:", only_directories=True).ask()
            if not path_answer:
                continue
            target = Path(path_answer).expanduser().resolve()
            if not target.exists() or not target.is_dir():
                console.print(f"[red]Invalid directory: {target}[/]")
                continue
            _run_pipeline(target, offline=False, console=console)
        elif action == "configure_keys":
            _configure_keys(console)
        elif action == "configure_models":
            _configure_models(console)
        elif action == "show_keys":
            _show_keys(console)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help="Show the agentrules version and exit.",
    ),
) -> None:
    console = Console()
    configure_logging()
    apply_config_to_environment()
    _load_env_files()
    model_config.apply_user_overrides()

    if version:
        import importlib.metadata

        version_str = importlib.metadata.version("agentrules")
        console.print(f"agentrules {version_str}")
        raise typer.Exit()

    if ctx.invoked_subcommand is not None:
        return

    _interactive_menu(console)


@app.command()
def analyze(
    path: Path = typer.Argument(Path.cwd(), exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    offline: bool = typer.Option(False, "--offline", help="Run using offline dummy architects (no API calls)."),
) -> None:
    console = Console()
    configure_logging()
    apply_config_to_environment()
    _load_env_files()
    model_config.apply_user_overrides()
    _run_pipeline(path, offline, console)


@app.command()
def configure(
    provider: Optional[str] = typer.Option(
        None,
        "--provider",
        "-p",
        help="Limit configuration to a single provider.",
    ),
    models_only: bool = typer.Option(
        False,
        "--models",
        help="Configure model presets instead of API keys.",
    ),
) -> None:
    console = Console()
    configure_logging()

    if models_only and provider:
        raise typer.BadParameter("Cannot combine --models with --provider.")

    if models_only:
        _configure_models(console)
        return

    if provider:
        if provider not in PROVIDER_ENV_MAP:
            raise typer.BadParameter(f"Unknown provider '{provider}'. Options: {', '.join(PROVIDER_ENV_MAP.keys())}")
        answer = questionary.password(f"{provider.title()} API key:", qmark="🔐").ask()
        if answer is None:
            console.print("[yellow]No changes made.[/]")
            return
        set_provider_key(provider, answer.strip() or None)
        console.print(f"[green]{provider.title()} key updated.[/]")
        model_config.apply_user_overrides()
        return

    _configure_keys(console)


@app.command("keys")
def show_keys() -> None:
    console = Console()
    configure_logging()
    _show_keys(console)
