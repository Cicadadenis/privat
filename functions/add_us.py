import asyncio
import os, time
import random
from rich.prompt import Prompt, Confirm
from rich.console import Console
from multiprocessing import Process
from telethon import events, types
from telethon import events, types, functions
from telethon.sync import TelegramClient
from telethon.utils import get_input_peer
from telethon.tl.types import InputPeerEmpty
from functions.function import Function
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerUser, InputPeerChat, InputPeerChannel
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import os 
import webbrowser
from functions.function import Function
from tkinter import * 
from tkinter import filedialog, Tk, messagebox
import asyncio
from tkinter import *
from rich.console import Console
from rich.prompt import Prompt, Confirm
from telethon.tl.functions.help import GetUserInfoRequest
from telethon import events, types, functions
from telethon.sync import TelegramClient
from telethon.utils import get_input_peer
from telethon.tl.types import InputPeerEmpty
from functions.function import Function
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerUser, InputPeerChat, InputPeerChannel
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys, os
import csv
import re
import traceback
import time
from logotip import log
console = Console()

class ReportFunc(Function):
    """Загрузить Свой Список Для Спама"""
    def __init__(self, storage, settings):
        super().__init__(storage, settings)


    async def execute(self):
        def logo():
            console.print("[blink blue]      _             __         ___       __[/]", justify="center")
            console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
        root=Tk()
        root.geometry('478x450')
        root.wm_title('Список Для Спама')
        root.iconbitmap('core\py\ccc.ico')
        root.attributes("-topmost",True)
        root.resizable(False, False)
        def retrieve_input():
            baza = []
            inputValue=textBox.get("1.0","end-1c")
            usus = inputValue.split("\n")
            for x in usus:
                if x >= '0':
                    baza.append(x)
            open("ussers.txt", "w")
            for x in baza:
                with open("ussers.txt", "a", encoding="utf-8") as f:
                         f.write(f"{x}\n")
            root.destroy()
            os.system("cls")
            logo()
            
        textBox=Text(root, height=20, width=40)
        textBox.pack()
        buttonCommit=Button(root, height=1, width=10, text="Добавить", 
                            command=lambda: retrieve_input())
        #command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack()

        


        root.mainloop()  