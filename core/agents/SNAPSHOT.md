.
├── __init__.py                # Public entry point for the agents package, exposing factory method.
├── anthropic/                 # Contains all logic for interacting with Anthropic's Claude models.
│   ├── __init__.py            # Public entry point for the Anthropic sub-package.
│   ├── architect.py           # Implements the BaseArchitect for Anthropic models.
│   ├── client.py              # Lazy Anthropic SDK client helpers.
│   ├── prompting.py           # Prompt templates and formatters for Claude agents.
│   ├── request_builder.py     # Constructs Claude Messages API payloads.
│   ├── response_parser.py     # Normalizes Anthropic responses into findings/tool calls.
│   └── tooling.py             # Provider-specific tool configuration helpers.
├── base.py                    # Defines the abstract BaseArchitect class and common enums.
├── deepseek.py                # Implements the architect for DeepSeek models via OpenAI-compatible API.
├── factory/                   # Contains the logic for creating different architect instances.
│   ├── __init__.py            # Exposes the architect factory function.
│   └── factory.py             # Implements a factory to create architect instances based on configuration.
├── gemini/                    # Contains all logic for interacting with Google Gemini models.
│   ├── __init__.py            # Public entry point for the Gemini sub-package.
│   ├── architect.py           # Implements the BaseArchitect for Google Gemini models.
│   ├── client.py              # Provides helpers for creating and interacting with the Gemini API client.
│   ├── errors.py              # Defines custom exception types for the Gemini provider.
│   ├── legacy.py              # Provides a backward-compatible GeminiAgent wrapper.
│   ├── prompting.py           # Contains helper functions for formatting prompts for Gemini models.
│   ├── response_parser.py     # Utilities for parsing responses from the Gemini API.
│   └── tooling.py             # Helper functions for handling tool configurations for Gemini.
└── openai/                    # Contains all logic for interacting with OpenAI models.
    ├── __init__.py            # Public entry point for the OpenAI sub-package.
    ├── architect.py           # Implements the BaseArchitect for OpenAI models.
    ├── client.py              # Manages the shared OpenAI client and dispatches API requests.
    ├── compat.py              # Provides a backward-compatible OpenAIAgent shim.
    ├── config.py              # Defines default configurations for various OpenAI models.
    ├── request_builder.py     # Constructs API request payloads for OpenAI models.
    └── response_parser.py     # Utilities for parsing and normalizing responses from OpenAI APIs.
