from telethon.tl.functions.account import UpdateProfileRequest
from rich.console import Console
import time, os
from functions.function import Function
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import * 
from tkinter import filedialog, Tk, messagebox


class ChangeBioFunc(Function):
    """Изменить биографию"""

    async def execute(self):
        bio = open("core/bio.txt", "r", encoding="utf-8").read()
      
        for session in self.sessions:
            try:
                async with self.storage.ainitialize_session(session):
                    await session(
                        UpdateProfileRequest(about=bio)
                    )

            except:
                messagebox.showinfo(f'Info',
                        f'Биография Не Изменена Неизвестная Ошибка !')

        messagebox.showinfo(f'Info',
                f'Биография Успешно Изменена !')
