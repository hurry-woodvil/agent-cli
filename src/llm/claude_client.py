from anthropic import Anthropic
from config import Settings


class ClaudeLLMClient:
    def __init__(self, settings: Settings):
        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.model = settings.claude_model

    def generate(self, prompt: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )

        texts: list[str] = []

        for content in message.content:
            if content.type == "text":
                texts.append(content.text)

        return "\n".join(texts)
