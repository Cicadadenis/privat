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
from modules.Conwert import to_session
from telethon.sync import TelegramClient
from loguru import logger
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import * 
from tkinter import filedialog, Tk, messagebox



console = Console()
def logo():
    console.print("[blink blue]     _             __         ___       __[/]", justify="center")
    console.print("[blink blue] ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
    console.print("[blink yellow]/ __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
    console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
    console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
    time.sleep(3)


class SetPasswordFunc(Function):
    """Конвертер С Формата Tdata"""

    async def execute(self):
        os.system("cls")
        logo()
        try:
            to_session()
        except:
            pass