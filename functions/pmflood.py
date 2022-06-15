import asyncio
import random
import os, time
from rich.prompt import Prompt, Confirm
from rich.console import Console

from functions.function import Function

console = Console()


class PmFloodFunc(Function):
    """Флуд в личку"""

    async def flood(self, session, peer,  media):
        count = 0
        errors = 0

        async with self.storage.ainitialize_session(session):
            me = await session.get_me()

            while True:
                try:
                    if not media:
                        mees = open('message.txt', "r", encoding="utf-8").read()
                        ms = mees.split("$")
                        text = random.choice(ms)
                        await session.send_message(peer, text)
                    else:
                        file = random.choice(os.listdir("media"))

                        await session.send_file(
                            peer,
                            os.path.join("media", file),
                            caption=text,
                            parse_mode="html"
                        )
                except Exception as err:
                    console.print(
                        "[{name}] [bold red]не отправлено.[/] {err}"
                        .format(name=me.first_name, err=err)
                    )

                    if errors >= 5:
                        break

                    errors += 1
                else:
                    count += 1
                    console.print(
                        "[{name}] [bold green]отправлено.[/] Шт: [yellow]{count}[/]"
                        .format(name=me.first_name, count=count)
                    )
                finally:
                    await self.delay()

    async def execute(self):
        def logo():
            console.print("[blink blue]      _             __         ___       __[/]", justify="center")
            console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
            time.sleep(2)
        os.system("cls")
        logo()
        console.print("[italic blue]\n\nФлуд\n\n[/]", justify="center")
        self.ask_accounts_count()

        peer = console.input("[italic red]\n\nвведите ID или имя пользователя> [/]")
        media = Confirm.ask("[italic red]\n\nmedia")


        delay = Prompt.ask(
            "[italic red]\n\nПауза[/]",
            default="-".join(str(x) for x in self.settings.delay)
        )

        self.settings.delay = self.parse_delay(delay)

        await asyncio.wait([
            self.flood(session, peer,  media)
            for session in self.sessions
        ])
