from agentrules.config.prompts.final_analysis_prompt import format_final_analysis_prompt
from agentrules.core.utils.constants import DEFAULT_RULES_FILENAME


def test_format_final_analysis_prompt_uses_default_rules_filename() -> None:
    prompt = format_final_analysis_prompt({"report": "sample"})
    assert f"`{DEFAULT_RULES_FILENAME}` files" in prompt
    assert f"tailored {DEFAULT_RULES_FILENAME} file using" in prompt
    assert f"effective `{DEFAULT_RULES_FILENAME}` files" in prompt


def test_format_final_analysis_prompt_uses_custom_rules_filename() -> None:
    prompt = format_final_analysis_prompt({"report": "sample"}, rules_filename="CLAUDE.md")
    assert "`CLAUDE.md` files" in prompt
    assert "tailored CLAUDE.md file using" in prompt
    assert "effective `CLAUDE.md` files" in prompt


def test_format_final_analysis_prompt_invalid_filename_falls_back_to_default() -> None:
    prompt = format_final_analysis_prompt({"report": "sample"}, rules_filename="nested/CLAUDE.md")
    assert f"`{DEFAULT_RULES_FILENAME}` files" in prompt
