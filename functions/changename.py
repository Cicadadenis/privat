import random
from telethon.tl.functions.account import UpdateProfileRequest
from rich.console import Console
import time, os
from functions.function import Function

console = Console()


class ChangeNameFunc(Function):
    """Изменить имена"""

    async def execute(self):
        def logo():
            console.print("[blink blue]     _             __         ___       __[/]", justify="center")
            console.print("[blink blue] ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow]/ __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
            time.sleep(2)
        os.system("cls")
        console.print("[italic blue]\n\nИзменить Имя\n\n[/]", justify="center")
        from_file = console.input("[italic red]Загрузить из файла? (y/n)> ")

        for session in self.sessions:
            if from_file == "y":
                with open("assets/names.txt", "r", encoding="utf-8") as file:
                    names = file.read().strip().splitlines()

                name = random.choice(names).split()
            else:
                name = console.input("[italic red]\n\nимя> [/]").split()
            try:
                first_name = name[0]
            except:
                pass
            if len(name) == 2:
                last_name = name[1]
            else:
                last_name = ""
            try:
                async with self.storage.ainitialize_session(session):
                    with console.status("[reverse yellow]Изменения Имени..."):
                        await session(
                            UpdateProfileRequest(
                                first_name=first_name,
                                last_name=last_name
                            )
                        )
            except:
                pass
