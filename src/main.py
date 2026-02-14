from ai.llm.g4f import G4Free
from tui.app import TuiApp


def main():
    # [print(model) for model in ModelRegistry.all_models()]
    llm = G4Free()
    app = TuiApp(llm)
    app.run()
    # print(llm.generate_text("Hello"))


if __name__ == "__main__":
    main()
