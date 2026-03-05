from .llm import LLM
import groq


class Groq(LLM):
    def __init__(self, api_key: str, model: str = "gpt-5.2") -> None:
        self.client = groq.Groq(api_key=api_key)
        self.model = model

    def get_models(self) -> list[str]:
        return [model[0] for model in self.client.models.list()]

    def set_model(self, model: str):
        self.model = model

    def generate_text(self, message: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model=self.model,
        )
        return response.choices[0].message.content
