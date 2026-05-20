import os
from dataclasses import dataclass


@dataclass
class Settings:
    anthropic_api_key: str
    claude_model: str


def load_settings() -> Settings:
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY is not set")

    claude_model = os.getenv("CLAUDE_MODEL", "claude-haiku-4-5-20251001")

    return Settings(anthropic_api_key=anthropic_api_key, claude_model=claude_model)
