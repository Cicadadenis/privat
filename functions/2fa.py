import asyncio
from rich.console import Console
from functions.function import Function
import time, os
import os
import tkinter as tk
from tkinter import ttk
from tkinter import * 
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
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import * 
from tkinter import filedialog, Tk, messagebox



console = Console()
class SetPasswordFunc(Function):
    """Установить 2fa пароль"""

    async def execute(self):
        password = console.input("[italic red]новый пароль> [/]")
        try:
            await asyncio.wait([
                session.edit_2fa(new_password=password)
                for session in self.sessions
            ])
    
        except:
            messagebox.showinfo(f'Info',
                    f'2fa Пароль Не Установлен !\n'
                    f'Так Как Он Возможно Уже Стоит')






    
