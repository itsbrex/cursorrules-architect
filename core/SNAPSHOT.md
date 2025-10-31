.
├── __init__.py                # Marks the directory as the 'core' Python package.
├── agent_tools/               # Contains tools that can be used by AI agents.
│   ├── tool_manager.py        # Manages and converts tool definitions for different AI providers.
│   └── web_search/            # Contains tools for performing web searches.
│       ├── __init__.py        # Exposes the Tavily search tool functions and schema.
│       └── tavily.py          # Implements a web search tool using the Tavily API.
├── agents/                    # Contains abstractions for different large language model providers.
│   ├── __init__.py            # Exposes the main architect factory function for easy access.
│   ├── anthropic.py           # Implements the architect for Anthropic's Claude models.
│   ├── base.py                # Defines the abstract base class and enums for all AI agents.
│   ├── deepseek.py            # Implements the architect for DeepSeek models.
│   ├── factory/               # Contains the factory for creating specific agent instances.
│   │   ├── __init__.py        # Exposes the architect factory function.
│   │   └── factory.py         # Creates agent instances based on configuration.
│   ├── gemini/                # Contains the implementation for Google Gemini models.
│   │   ├── __init__.py        # Gemini provider package entry point.
│   │   ├── architect.py       # Implements the main architect class for Gemini models.
│   │   ├── client.py          # Helper functions for creating and using the Gemini client.
│   │   ├── errors.py          # Custom exceptions for the Gemini provider.
│   │   ├── legacy.py          # A backward-compatibility wrapper for the Gemini architect.
│   │   ├── prompting.py       # Helper functions for creating and formatting Gemini prompts.
│   │   ├── response_parser.py # Parses responses from the Gemini API into a standard format.
│   │   └── tooling.py         # Helper for converting tool definitions to the Gemini format.
│   └── openai/                # Contains the implementation for OpenAI models.
│       ├── __init__.py        # OpenAI provider package entry point.
│       ├── architect.py       # Implements the main architect class for OpenAI models.
│       ├── client.py          # Manages the shared OpenAI client and executes requests.
│       ├── compat.py          # Provides a backward-compatible agent shim for legacy code.
│       ├── config.py          # Defines default configurations for various OpenAI models.
│       ├── request_builder.py # Constructs API request payloads for OpenAI.
│       └── response_parser.py # Parses responses from OpenAI APIs into a standard format.
├── analysis/                  # Contains the logic for each phase of the project analysis pipeline.
│   ├── __init__.py            # Exposes all analysis phase classes.
│   ├── final_analysis.py      # Implements the final analysis phase to generate cursor rules.
│   ├── phase_1.py             # Implements Phase 1: Initial project discovery and research.
│   ├── phase_2.py             # Implements Phase 2: Creates an analysis plan and defines agents.
│   ├── phase_3.py             # Implements Phase 3: In-depth code analysis by specialized agents.
│   ├── phase_4.py             # Implements Phase 4: Synthesizes findings from the deep analysis.
│   └── phase_5.py             # Implements Phase 5: Consolidates all results into a single report.
├── types/                     # Contains custom type definitions and data structures.
│   ├── __init__.py            # Exposes type definitions and predefined model configs.
│   ├── agent_config.py        # Defines a TypedDict for agent phase configurations.
│   ├── models.py              # Defines the ModelConfig class and predefined model configurations.
│   └── tool_config.py         # Defines the data structures for agent tool configurations.
└── utils/                     # Contains various utility functions and helper modules.
    ├── file_creation/         # Utilities for creating files during the analysis process.
    │   ├── cursorignore.py    # Manages the creation and modification of .cursorignore files.
    │   └── phases_output.py   # Saves the output of each analysis phase to structured files.
    ├── file_system/           # Utilities for interacting with the file system.
    │   ├── __init__.py        # Exposes file system utility functions.
    │   ├── file_retriever.py  # Retrieves and formats file contents, respecting exclusion rules.
    │   └── tree_generator.py  # Generates an ASCII tree representation of the project structure.
    ├── formatters/            # Utilities for formatting file content.
    │   ├── __init__.py        # Exposes the clean_cursorrules function.
    │   └── clean_cursorrules.py # Cleans .cursorrules files to ensure correct formatting.
    ├── model_config_helper.py # Helper to get the display name of a model configuration.
    ├── offline.py             # Provides a dummy architect for offline testing of the pipeline.
    └── parsers/               # Utilities for parsing structured data from model outputs.
        ├── __init__.py        # Exposes agent parsing utility functions.
        └── agent_parser.py    # Parses agent definitions and file assignments from Phase 2 output.