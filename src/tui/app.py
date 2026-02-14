from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, VerticalScroll
from textual.widgets import Footer, Header

from ai.llm.llm import LLM

from .wingets.prompt import PromptInput


class MessagesView(VerticalGroup):
    def __init__(self, llm: LLM):
        super().__init__()
        self.llm = llm

    def compose(self) -> ComposeResult:
        yield VerticalScroll(id="messages")
        yield PromptInput(self.llm)


class TuiApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("space", "focus_prompt", "Focus prompt input"),
    ]

    def __init__(self, llm: LLM):
        self.llm = llm
        super().__init__()

    def compose(self) -> ComposeResult:
        self.title = "Suzuke"
        yield Header()
        yield MessagesView(self.llm)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_focus_prompt(self) -> None:
        self.query_one("#prompt-input").focus()
