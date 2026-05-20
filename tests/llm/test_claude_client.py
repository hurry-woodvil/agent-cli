from types import SimpleNamespace

from src.config import Settings
from src.llm.claude_client import ClaudeLLMClient


def test_generate_returns_text(monkeypatch):
    settings = Settings(anthropic_api_key="test-api-key", claude_model="test-model")

    client = ClaudeLLMClient(settings)

    def mock_create(*args, **kwargs):
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text="test response")]
        )

    monkeypatch.setattr(client.client.messages, "create", mock_create)

    response = client.generate("hello")

    assert response == "test response"
