from abc import ABC, abstractmethod


class LLM(ABC):
    @abstractmethod
    def get_models(self) -> list[str]:
        pass

    @abstractmethod
    def set_model(self, model: str):
        pass

    @abstractmethod
    def generate_text(self, message: str) -> str:
        pass
