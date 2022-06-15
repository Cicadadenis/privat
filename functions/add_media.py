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
    """Загрузить Фото/Видео/Файл Для Спама"""
    async def execute(self):
        os.system("start media")
        time.sleep(4)
        print(f'Успешно Добавленны !')
                           