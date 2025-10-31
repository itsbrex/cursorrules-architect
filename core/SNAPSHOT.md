.
├── __init__.py                # Marks the directory as the 'core' Python package.
├── agent_tools/               # Contains tools that can be used by AI agents.
│   ├── tool_manager.py        # Manages and converts tool schemas for different LLM providers.
│   └── web_search/            # Contains web search tool implementations.
│       ├── __init__.py        # Exposes the Tavily web search tool implementation.
│       └── tavily.py          # Implements a web search tool using the Tavily API.
├── agents/                    # Defines interfaces and implementations for various AI model providers.
│   ├── __init__.py            # Exposes a factory function for creating agent instances.
│   ├── anthropic/             # Contains the implementation for Anthropic (Claude) models.
│   │   ├── __init__.py        # Exposes the AnthropicArchitect class.
│   │   ├── architect.py       # Implements the BaseArchitect interface for Anthropic models.
│   │   ├── client.py          # Manages the Anthropic SDK client instance.
│   │   ├── prompting.py       # Provides helper functions for formatting Anthropic prompts.
│   │   ├── request_builder.py # Constructs API request payloads for Anthropic models.
│   │   ├── response_parser.py # Parses and normalizes responses from the Anthropic API.
│   │   └── tooling.py         # Helper for preparing tool configurations for Anthropic models.
│   ├── base.py                # Defines the abstract BaseArchitect class for all AI agents.
│   ├── deepseek.py            # Implements the BaseArchitect for DeepSeek models.
│   ├── factory/               # Contains the factory for creating agent instances.
│   │   ├── __init__.py        # Exposes the main factory function.
│   │   └── factory.py         # Implements a factory to create architect instances based on configuration.
│   ├── gemini/                # Contains the implementation for Google Gemini models.
│   │   ├── __init__.py        # Exposes the GeminiArchitect and a legacy agent.
│   │   ├── architect.py       # Implements the BaseArchitect interface for Gemini models.
│   │   ├── client.py          # Manages the Google GenAI (Gemini) client instance.
│   │   ├── errors.py          # Defines custom exceptions for the Gemini provider.
│   │   ├── legacy.py          # Provides a backward-compatible wrapper for the Gemini architect.
│   │   ├── prompting.py       # Provides helper functions for formatting Gemini prompts.
│   │   ├── response_parser.py # Parses and normalizes responses from the Gemini API.
│   │   └── tooling.py         # Helper for preparing tool configurations for Gemini models.
│   └── openai/                # Contains the implementation for OpenAI models.
│       ├── __init__.py        # Exposes the OpenAIArchitect and a legacy agent.
│       ├── architect.py       # Implements the BaseArchitect interface for OpenAI models.
│       ├── client.py          # Manages the OpenAI SDK client instance.
│       ├── compat.py          # Provides a backward-compatible wrapper for the OpenAI architect.
│       ├── config.py          # Defines default configurations for various OpenAI models.
│       ├── request_builder.py # Constructs API request payloads for OpenAI models.
│       └── response_parser.py # Parses and normalizes responses from the OpenAI API.
├── analysis/                  # Implements the multi-phase project analysis pipeline.
│   ├── __init__.py            # Exports all analysis phase classes.
│   ├── final_analysis.py      # Implements the final analysis phase to generate cursor rules.
│   ├── phase_1.py             # Implements Phase 1: Initial project discovery and research.
│   ├── phase_2.py             # Implements Phase 2: Creates a methodical plan for deep analysis.
│   ├── phase_3.py             # Implements Phase 3: In-depth file analysis by specialized agents.
│   ├── phase_4.py             # Implements Phase 4: Synthesizes findings from the deep analysis.
│   ├── phase_5.py             # Implements Phase 5: Consolidates all findings into a final report.
├── types/                     # Defines custom data types and structures for the project.
│   ├── __init__.py            # Exports primary type definitions for models and agents.
│   ├── agent_config.py        # Defines the TypedDict for agent configuration.
│   ├── models.py              # Defines the ModelConfig named tuple and pre-configured model instances.
│   └── tool_config.py         # Defines TypedDicts for tool configurations.
└── utils/                     # Contains shared utility functions and helper modules.
    ├── file_creation/         # Utilities for generating files like .cursorignore and phase outputs.
    │   ├── cursorignore.py    # Manages the creation and modification of .cursorignore files.
    │   └── phases_output.py   # Saves the output of each analysis phase to structured files.
    ├── file_system/           # Utilities for file system operations like reading files and generating trees.
    │   ├── __init__.py        # Exposes main functions for file retrieval and tree generation.
    │   ├── file_retriever.py  # Retrieves file contents from a directory, respecting exclusion rules.
    │   └── tree_generator.py  # Generates a visual ASCII tree representation of the project structure.
    ├── formatters/            # Contains file content formatting utilities.
    │   ├── __init__.py        # Exposes the clean_cursorrules function.
    │   └── clean_cursorrules.py # Cleans .cursorrules files to ensure a proper starting prompt.
    ├── model_config_helper.py # Helper to resolve the string name of a model configuration for logging.
    ├── offline.py             # Provides a dummy architect for running the pipeline without API calls.
    └── parsers/               # Contains parsers for extracting structured data from text.
        ├── __init__.py        # Exposes agent parser functions.
        └── agent_parser.py    # Parses agent definitions and file assignments from Phase 2's output.