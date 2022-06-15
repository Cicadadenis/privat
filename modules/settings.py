import os
import sys
import toml
from rich.console import Console
from typing import List

console = Console()


class Settings:
    def __init__(self):
        os.system("cls")
        if not os.path.exists("config.toml"):
            self.initial_setup()
            sys.exit()

        with open("config.toml") as file:
            config = toml.load(file)

        self.api_id: int = config["sessions"]["api_id"]
        self.api_hash: str = config["sessions"]["api_hash"]
        self.messages: List[str] = config["flood"]["messages"]
        self.messages_count: int = config["flood"]["messages_count"]
        self.trigger: str = config["flood"]["trigger"]
        self.delay: List[int] = config["flood"]["delay"]

    def save(
        self,
        api_id,
        api_hash,
        messages,
        delay,
        messages_count,
        trigger
    ):
        config = dict(
            sessions=dict(
                api_hash=api_hash,
                api_id=api_id
            ),
            flood=dict(
                messages=messages,
                delay=delay,
                messages_count=messages_count,
                trigger=trigger
            )
        )

        with open("config.toml", "w") as file:
            toml.dump(config, file)

    def initial_setup(self):
        console.print(
            "[reverse italic blink yellow]Начальная настройка[/]",
            justify="center"
        )

        print()

        console.print(
            "[italic blue]Sessions[/]",
            justify="center"
        )

        print()
        api_id, api_hash = self.setup_sessions()

        console.print(
            "[italic blue]Flood[/]",
            justify="center"
        )

        print()
        messages, delay, trigger = self.setup_flood()

        self.save(
            api_id,
            api_hash,
            messages,
            delay,
            0,
            trigger
        )
        os.system("cls")
        import main
    def setup_sessions(self):
        api_id = console.input("[reverse italic blink yellow]Вводи API ID: [/]")
        api_hash = console.input("[reverse italic blink yellow]Вводить API hash: [/]")

        return int(api_id), api_hash

    def setup_flood(self):
        console.print("[reverse italic blink yellow]Введи сообщения (каждая строка + 1 сообщение для рандома, чтобы завершить просто Enter)[/]")

        messages = []

        while message := console.input("[bold yellow]>> [/]"):
            messages.append(message)

        print()

        delay = console.input("[bold yellow]Задержка Флуда(от и до. 10-30): [/]")
        delay = delay.split("-")
        delay = [int(x) for x in delay]

        trigger = console.input("[bold yellow]Введи текст, после которого боты начнут флудить: [/]")

        return messages, delay, trigger


