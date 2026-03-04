from typing import Optional
from .llm import LLM

from g4f.client import Client
from g4f.models import ModelRegistry


class G4Free(LLM):
    def __init__(self, model: str = "gpt-4.1", api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key
        self.client = Client()

    def get_models(self) -> list[str]:
        return [model for model in ModelRegistry.all_models()]

    def set_model(self, model: str):
        self.model = model

    def set_api_key(self, api_key: str):
        self.api_key = api_key
        if self.api_key:
            self.client.api_key = self.api_key

    def generate_text(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}],
            web_search=False,
        )
        return response.choices[0].message.content
