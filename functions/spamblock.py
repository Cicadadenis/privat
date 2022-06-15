import asyncio
import os, time
import random
import re

from typing import Dict, List

from rich.prompt import Confirm
from rich.console import Console

from telethon import events
from telethon.sync import TelegramClient

from functions.function import Function

console = Console()


class SpamBlockFunc(Function):
    """Проверить На Спам"""

    async def check(self, session):
        async with self.storage.ainitialize_session(session):
            me = await session.get_me()

            try:
                await session.send_message("SpamBot", "/start")
            except Exception as err:
                console.print(f"[italic red][!] {err}[/]")
                time.sleep(3)
                return

            await asyncio.sleep(0.5)
            messages = await session.get_messages("SpamBot", limit=1)

            text = messages[0].message
            
            if text != "Good news, no limits are currently applied to your account. You’re free as a bird!":
                if "sending spam" in text:
                    console.print(f"[italic red][-] Это вечное ограничение[/]")
                    time.sleep(3)
                    return "permanent", session, me

                else:
                    result = re.findall(r"\d+\s\w+\s\d{4}", text)

                    if len(result) == 0:
                        console.print(f"{text}")
                        time.sleep(3)
                        return
                    
                    date = result[0]

                    console.print(f"[italic red][-] {date}[/]")
                    time.sleep(4)
                    return date, session, me

            else:
                console.print("[italic green][+] Аккаунт без блокировки спама[/]")

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
        console.print("[italic blue]\n\nПроверка На Спам\n\n[/]", justify="center")
        blocks: Dict[str, List[TelegramClient]] = {}

        tasks = await asyncio.wait([
            self.check(session)
            for session in self.sessions
        ])

        for task in tasks[0]:
            result = task.result()

            if result is None:
                continue

            date, session, user = result

            if date == "permanent":
                if not blocks.get("permanent"):
                    blocks["permanent"] = []

                blocks["permanent"].append(session)

            else:
                if not blocks.get(date):
                    blocks[date] = []

                blocks[date].append(session)

        move_sessions = Confirm.ask("[italic magenta]Переместить сеансы с ограниченным доступом в другие папки?[/]")

        if move_sessions:
            if not os.path.exists("sessions/spamblock"):
                os.mkdir("sessions/spamblock")
           
            for date, sessions in blocks.items():
                for session in sessions:
                    path = os.path.join("sessions", "spamblock", date)

                    if not os.path.exists(path):
                        os.mkdir(path)

                    session_path = self.storage.get_session_path(session)
                    session_name = os.path.basename(session_path)
                    try:
                        os.rename(
                            session_path,
                            os.path.join(path, session_name)
                        )
                    except:pass

