import random
import asyncio
import os, time

from rich.progress import track
from rich.console import Console
from rich.prompt import Prompt, Confirm

from time import perf_counter

from telethon import events, types
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.sync import TelegramClient

from functions.flood import Flood
from functions.function import Function

console = Console()


class JoinerFunc(Function):
    """Присоединяйтесь к чату"""

    async def join(self, session, link, index, mode):
        if mode == "1":
            try:
                
                if not "joinchat" in link:
                    await session(JoinChannelRequest(link))
                else:
                    await session(ImportChatInviteRequest(link))
            except Exception as error:
                print(f"[-] [acc {index + 1}] {error}")
            else:
                return True

        elif mode == "2":
            try:
                try:
                    channel = await session(GetFullChannelRequest(link))
                    chat = channel.chats[1]
                except:
                    await session(JoinChannelRequest(link))
            except Exception as error:
                    print(f"[-] [acc {index + 1}] {error}")
            else:
                return True

    async def solve_captcha(self, session: TelegramClient):
        session.add_event_handler(
            self.on_message,
            events.NewMessage
        )

        await session.run_until_disconnected()

    async def on_message(self, msg: types.Message):
        if msg.mentioned:
            if msg.reply_markup:
                captcha = msg.reply_markup.rows[0] \
                    .buttons[0].data.decode("utf-8")

                await msg.click(data=captcha)

    async def execute(self):
        def logo():
            console.print("[blink blue]     _             __         ___       __[/]", justify="center")
            console.print("[blink blue] ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow]/ __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
            time.sleep(2)
        os.system("cls")
        logo()
        console.print("[italic blue]\n\nВступить В Чат\n\n[/]", justify="center")
        self.ask_accounts_count()

        print()

        console.print(
            "[1] Просто присоединяйтесь к чату/каналу",
            "[2] Присоединяйтесь к чату канала и проспамить его",
            sep="\n",
            style="italic green"
        )

        print()

        mode = console.input("[italic red]Режим> [/]")
        link = console.input("[italic red]Ссылка На чат/канал> [/]")
        if mode == "1":
            if len(link) >= 3:
                os.system("cls")
                logo()
                for index, session in track(
                    enumerate(self.sessions),
                    "[italic yellow]присоединение к чату/каналу...[/]" 
                ): 
                    await session.start()
                    try:

                        if not "joinchat" in link:
                            s1 = await session(JoinChannelRequest(link))
                            print(s1)
                            input()
                        else:
                            await session(ImportChatInviteRequest(link))
                    except Exception as error:
                        os.system("cls")
                        logo()
                        console.print(f"[bold red italic][-] [acc {index + 1}] {error}")
                        pass
            else:
                console.print("[italic blink red]\n\n\nСсылка Не Указана Либо Неверна[/]", justify="center")
        if mode == "2":
            os.system("cls")
            logo()
            speed = Prompt.ask(
                "[bold red]скорость>[/]",
                choices=["normal", "fast"]
            )

            #flood = Confirm.ask(password="cicada", *)

           # if flood:
            flood_func = Flood(self.storage, self.settings)
            function_index = flood_func.ask()

            joined = 0

            if speed == "normal":
                os.system("cls")
                logo()
                #delay = Prompt.ask("[italic red]Пауза[/]", default="0")
                captcha = Confirm.ask("[italic red]капча[/]")

                start = perf_counter()

                if function_index != 1:
                    os.system("cls")
                    logo()
                    for index, session in track(
                        enumerate(self.sessions),
                        "[italic yellow]присоединение к чату/каналу...[/]",
                        total=len(self.sessions)
                    ):
                        await session.start()

                        if captcha:
                            asyncio.create_task(
                                self.solve_captcha(session)
                            )

                        is_joined = await self.join(session, link, index, mode)

                        if is_joined:
                            joined += 1

                        await asyncio.sleep(int(5))

                elif function_index == 1:
                    for index, session in enumerate(self.sessions):
                        await session.start()

                        if captcha:
                            asyncio.create_task(
                                self.solve_captcha(session)
                            )

                        is_joined = await self.join(session, link, index, mode)

                        console.print("[italic green]Бот присоединился[/]")

                        if is_joined:
                            joined += 1

                        console.print("[italic green]Старт Флуда[/]")

                        await flood_func.flood(session, link, flood_func.function)
                        await asyncio.sleep(int(5))

            if speed == "fast":
                os.system("cls")
                logo()
                if not self.storage.initialize:
                    for session in track(
                        self.sessions,
                        "[italic yellow]Инициализация сессии[/]",
                        total=len(self.sessions)
                    ):
                        await session.connect()

                with console.status("присоединение к чату/каналу..."):
                    start = perf_counter()

                    tasks = await asyncio.wait([
                        self.join(session, link, index, mode)
                        for index, session in enumerate(self.sessions)

                    ])

                for result in tasks:
                    if result:
                        joined += 1

            #if flood and function_index != 1:
            await asyncio.wait([
                flood_func.flood(session, link, flood_func.function)
                for session in self.sessions
            ])

            joined_time = round(perf_counter() - start, 2)
            console.print(f"[+] {joined} боты присоединились к [italic yellow]{joined_time}[/]s")

