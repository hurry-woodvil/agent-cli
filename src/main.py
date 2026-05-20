import argparse

from src.config import load_settings
from llm.claude_client import ClaudeLLMClient


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=str)

    args = parser.parse_args()

    prompt = args.prompt

    settings = load_settings()

    print(f"prompt: {prompt}")
    print(f"ANTHROPIC_API_KEY: {settings.anthropic_api_key}")
    print(f"CLAUDE_MODE: {settings.claude_model}")


if __name__ == "__main__":
    main()
