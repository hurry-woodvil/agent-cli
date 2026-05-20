import pytest

from src.config import load_settings


def test_load_settings(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-api-key")
    monkeypatch.setenv("CLAUDE_MODEL", "test-model")

    settings = load_settings()

    assert settings.anthropic_api_key == "test-api-key"
    assert settings.claude_model == "test-model"


def test_load_settings_use_default_model_when_model_is_not_set(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-api-key")

    settings = load_settings()

    assert settings.anthropic_api_key == "test-api-key"
    assert settings.claude_model == "claude-haiku-4-5-20251001"


def test_load_settings_raises_error_when_api_key_is_not_set(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

    with pytest.raises(ValueError):
        load_settings()
