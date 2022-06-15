import asyncio
from rich.console import Console
from functions.function import Function
import time, os
import asyncio
from rich.console import Console
from functions.function import Function
import time, os
import os
import asyncio
from rich.console import Console
from contextlib import contextmanager, asynccontextmanager
from typing import List, Dict
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import socks
import time
from telethon.sessions import StringSession
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import time
from telethon.sync import TelegramClient
from loguru import logger



console = Console()
def logo():
    console.print("[blink blue]     _             __         ___       __[/]", justify="center")
    console.print("[blink blue] ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
    console.print("[blink yellow]/ __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
    console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
    console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
    time.sleep(3)


class SetPasswordFunc(Function):
    """Конвертер С Формата SQLiteSession"""

    async def execute(self):
        os.system("cls")
        logo()

        api_hash = "bd4bbac77f54cd096ede52dd2e8e2e50"
        api_id = 17463049
        ff = filedialog.askdirectory()
        logger.info("Проверка аккаунтов")
        for s in os.listdir(ff):
            if s.split(".")[-1] == 'json':
                os.system(f"del /S/Q {s}")
            
            if s.split(".")[-1] == 'session':
            

                client = TelegramClient(s, api_id, api_hash)
                client.connect()
                aut = StringSession.save(client.session)
                with open(f"sessions/{s}", "w") as f:
                    f.write(aut)
                    os.system(f"powershell copy  sessions/{s} sessions/+{s}")
                    client.disconnect()
                    logger.success(f"{s} — сохранён.")
