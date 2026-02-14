from textual import messages, on
from textual.app import ComposeResult
from textual.widgets import Input, Label, Markdown

from ai.llm.llm import LLM


class PromptInput(Input):
    def __init__(self, llm: LLM):
        super().__init__(id="prompt-input")
        self.llm = llm
        self.messages = messages

    def on_mount(self) -> None:
        self.refresh_bindings()
        self.placeholder = "Write your prompt here"

    def compose(self) -> ComposeResult:
        return super().compose()

    @on(Input.Submitted)
    def on_submitted(self, event: Input.Submitted):
        event.input.value = ""
        message_label = Label(event.value, classes="me")
        message_label.border_title = "Me"
        self.app.query_one("#messages").mount(message_label)
        res = self.llm.generate_text(event.value)
        self.app.query_one("#messages").mount(Markdown(res))
