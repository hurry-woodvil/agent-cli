import sys

import src.main


def test_main_outputs_llm_response(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["src.main", "hello"])
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-api-key")
    monkeypatch.setenv("CLAUDE_MODEL", "test-model")

    def mock_generate(self, prompt: str) -> str:
        return "Hello World"

    monkeypatch.setattr("src.llm.claude_client.ClaudeLLMClient.generate", mock_generate)

    src.main.main()

    captured = capsys.readouterr()

    assert "Hello World" in captured.out
