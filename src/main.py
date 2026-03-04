import config
from tui.app import TuiApp


def main():
    conf = config.load()
    llm = conf.llm.get_llm()
    app = TuiApp(llm)
    app.run()


if __name__ == "__main__":
    main()
