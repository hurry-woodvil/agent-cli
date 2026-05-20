import argparse

from src.config import load_settings
from src.llm.claude_client import ClaudeLLMClient


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=str)

    args = parser.parse_args()

    prompt = args.prompt

    settings = load_settings()

    client = ClaudeLLMClient(settings)
    response = client.generate(prompt)

    print(response)


if __name__ == "__main__":
    main()
