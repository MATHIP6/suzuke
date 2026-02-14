from .llm import LLM

from g4f.client import Client
from g4f.models import ModelRegistry


class G4Free(LLM):
    def __init__(self):
        self.model = "deepseek-v3"

    def get_models(self) -> list[str]:
        return [model for model in ModelRegistry.all_models()]

    def set_model(self, model: str):
        self.model = model

    def generate_text(self, message: str) -> str:
        client = Client()
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}],
            web_search=False,
        )
        return response.choices[0].message.content
