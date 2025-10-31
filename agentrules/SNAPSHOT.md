.
├── __init__.py                # Package initializer for the agentrules CLI.
├── analyzer.py                # Core orchestration logic for the multi-phase project analysis pipeline.
├── cli.py                     # Typer-based command-line interface for running analysis and configuration.
├── config_service.py          # Manages user configuration for API keys and model presets via a TOML file.
├── logging_setup.py           # Sets up Rich-based logging and filters for consistent CLI output.
├── model_config.py            # Manages and applies model presets based on user configuration.