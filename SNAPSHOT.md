Project layout snapshot (November 2025)
======================================

.
├── src/
│   └── agentrules/                  # First-party package exposed to callers.
│       ├── __init__.py              # Warn-filter setup for urllib3 noise.
│       ├── __main__.py              # Allows `python -m agentrules` entry point.
│       ├── analyzer.py              # High-level orchestration of the analysis pipeline.
│       ├── cli/                     # Typer-based CLI, Questionary flows, and services.
│       │   ├── __init__.py
│       │   ├── app.py               # Creates the Typer application.
│       │   ├── bootstrap.py         # Runtime setup (logging, config loading).
│       │   ├── commands/            # Individual Typer command handlers.
│       │   │   ├── __init__.py
│       │   │   ├── analyze.py
│       │   │   ├── configure.py
│       │   │   └── keys.py
│       │   ├── context.py           # Shared CLI context container.
│       │   ├── services/            # Service layer used by commands/UI flows.
│       │   │   ├── __init__.py
│       │   │   ├── configuration.py
│       │   │   └── pipeline_runner.py
│       │   └── ui/                  # Interactive Questionary views.
│       │       ├── __init__.py
│       │       ├── analysis_view.py
│       │       ├── main_menu.py
│       │       └── settings/
│       │           ├── __init__.py
│       │           ├── exclusions/
│       │           │   ├── __init__.py
│       │           │   ├── editor.py
│       │           │   └── summary.py
│       │           ├── logging.py
│       │           ├── menu.py
│       │           ├── models/
│       │           │   ├── __init__.py
│       │           │   ├── researcher.py
│       │           │   └── utils.py
│       │           ├── outputs.py
│       │           └── providers.py
│       ├── config_service.py        # Persistence of CLI + provider configuration.
│       ├── logging_setup.py         # Rich logging utilities.
│       ├── model_config.py          # Helpers for resolving model presets.
│       ├── config/                  # Static configuration surfaced under `agentrules.config`.
│       │   ├── __init__.py
│       │   ├── agents.py            # Declarative model listings per phase/provider.
│       │   ├── exclusions.py        # Default exclusion sets for scans.
│       │   ├── prompts/             # Prompt templates per analysis stage.
│       │   │   ├── __init__.py
│       │   │   ├── final_analysis_prompt.py
│       │   │   ├── phase_1_prompts.py
│       │   │   ├── phase_2_prompts.py
│       │   │   ├── phase_3_prompts.py
│       │   │   ├── phase_4_prompts.py
│       │   │   └── phase_5_prompts.py
│       │   └── tools.py             # Tool configuration per agent.
│       └── core/                    # Engine, agents, and utilities accessible via `agentrules.core`.
│           ├── __init__.py
│           ├── agent_tools/         # Tool registry + Tavily search integration.
│           │   ├── tool_manager.py
│           │   └── web_search/
│           │       ├── __init__.py
│           │       └── tavily.py
│           ├── agents/              # Provider-specific architect implementations.
│           │   ├── __init__.py
│           │   ├── anthropic/
│           │   ├── base.py
│           │   ├── deepseek/
│           │   ├── factory/
│           │   ├── gemini/
│           │   ├── openai/
│           │   └── xai/
│           ├── analysis/            # Phase runners + orchestrators.
│           │   ├── __init__.py
│           │   ├── events.py
│           │   ├── final_analysis.py
│           │   ├── phase_1.py
│           │   ├── phase_2.py
│           │   ├── phase_3.py
│           │   ├── phase_4.py
│           │   └── phase_5.py
│           ├── streaming.py         # Shared streaming event dataclasses.
│           ├── types/               # Core typed configs and dataclasses.
│           │   ├── __init__.py
│           │   └── models.py
│           └── utils/               # Filesystem + formatting helpers.
│               ├── __init__.py
│               ├── async_stream.py
│               ├── constants.py
│               ├── dependency_scanner.py
│               ├── file_creation/
│               │   ├── cursorignore.py
│               │   └── phases_output.py
│               ├── file_system/
│               │   ├── __init__.py
│               │   ├── file_retriever.py
│               │   ├── gitignore.py
│               │   └── tree_generator.py
│               ├── formatters/
│               │   ├── __init__.py
│               │   └── clean_cursorrules.py
│               ├── model_config_helper.py
│               └── offline.py
├── tests/                         # Unit + phase regression suites.
│   ├── unit/
│   ├── phase_1_test/
│   ├── phase_2_test/
│   ├── phase_3_test/
│   ├── phase_4_test/
│   ├── phase_5_test/
│   ├── final_analysis_test/
│   └── utils/
├── scripts/                       # Developer utilities (e.g., env bootstrap).
├── docs/                          # Supplemental project documentation (gitignored in releases).
├── main.py                        # Convenience launcher; adds `src/` to `sys.path`.
├── pyproject.toml                 # Build metadata, dependencies, tooling config.
├── requirements.txt               # Production dependency lock.
├── requirements-dev.txt           # Dev/test tooling dependencies.
├── README.md
├── CONTRIBUTING.md
├── AGENTS.md
└── SNAPSHOT.md                    # This file.
