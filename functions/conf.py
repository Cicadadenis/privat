import asyncio
import os, time
import random
from rich.prompt import Prompt, Confirm
from rich.console import Console
from multiprocessing import Process
from telethon import events, types
import os 
import webbrowser
from functions.function import Function
from tkinter import * 
from tkinter import filedialog, Tk, messagebox

console = Console()

class ReportFunc(Function):
    """Изменить Начальные Настройки"""
    async def execute(self):
        os.system("cls")
        time.sleep(4)
        os.system("del /S/Q config.toml")
        from modules import settings