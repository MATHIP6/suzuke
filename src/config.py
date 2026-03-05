from pathlib import Path
from typing import Optional
from platformdirs import PlatformDirs
from shutil import copy
import tomllib
from ai.llm.g4f import G4Free
from ai.llm.llm import LLM
from ai.llm.openai import OpenAI


dirs = PlatformDirs("suzuke")


class LLMConfig:
    def __init__(self, name: str, model: str, api_key: Optional[str] = None):
        self.name = name
        self.model = model
        self.api_key = api_key

    def get_llm(self) -> LLM:
        llm = None
        match self.name:
            case "g4f":
                llm = G4Free()
                llm.model = self.model
                if self.api_key:
                    llm.set_api_key(self.api_key)
            case "openai":
                if not self.api_key:
                    raise Exception("You must have an API Key to use this model")
                llm = OpenAI(self.api_key)
                llm.model = self.model

            case _:
                raise Exception("Unknown llm name in config")
        return llm


class Config:
    def __init__(self, llm: LLMConfig):
        self.llm = llm


def load():
    config_dir = Path(dirs.user_config_dir)
    if not config_dir.exists():
        config_dir.mkdir(parents=False)
    default_config = Path(__file__).parent.parent / "config.toml"
    config_file = config_dir / "config.toml"
    if not config_file.exists():
        copy(default_config, config_file)
    with open(config_file, "rb") as f:
        toml_data = tomllib.load(f)
        llm_config = LLMConfig(**toml_data["llm"])
        return Config(llm_config)
