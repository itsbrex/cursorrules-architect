import asyncio

import agentrules.core.agents.gemini as gemini_mod
from agentrules.core.agents.gemini import GeminiArchitect


def test_gemini_analyze_client_not_initialized(monkeypatch):
    # Force client construction to fail so __init__ sets self.client=None
    class Boom(Exception):
        pass

    class FakeClient:  # stand-in so name exists
        pass

    def raise_exc(*args, **kwargs):
        raise Boom("no client")

    monkeypatch.setattr(gemini_mod.genai, "Client", raise_exc)

    arch = GeminiArchitect(model_name="gemini-2.5-pro")
    assert arch.client is None

    # analyze should return an error field when client missing
    out = asyncio.run(arch.analyze({}))
    assert "error" in out and "not initialized" in out["error"].lower()
