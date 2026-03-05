from g4f import Optional
from .llm import LLM
import openai


class OpenAI(LLM):
    def __init__(self, api_key: str, model: str = "gpt-5.2") -> None:
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def get_models(self) -> list[str]:
        return [model.id for model in self.client.models.list()]

    def set_model(self, model: str):
        self.model = model

    def generate_text(self, message: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=message,
        )

        return response.output_text
