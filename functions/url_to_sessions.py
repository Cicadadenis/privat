
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
import os, rarfile
import shutil
import requests
from datetime import datetime
import time
import webbrowser

from telethon.sessions import StringSession
from modules.convert_tdata import *
import time
from telethon.sync import TelegramClient
from telethon import connection
from loguru import logger
from tkinter import *
from tkinter import Tk
from tkinter import filedialog


import shutil
from modules.Conwert import to_session

console = Console()
def logo():
    console.print("[blink blue]     _             __         ___       __[/]", justify="center")
    console.print("[blink blue] ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
    console.print("[blink yellow]/ __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
    console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
    console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
    time.sleep(3)


class SetPasswordFunc(Function):
    """Конвертер в Sessions из URL Сылок"""
    async def execute(self):

        root=Tk()
        root.geometry('478x450')
        root.wm_title('Конвертер в Sessions из URL Сылок')
        root.resizable(False, False)
        root.iconbitmap('core\py\ccc.ico')
        def retrieve_input():
            baza = []
            dir_name = "temp_aka"

            dit_temp = "tdata_to_sessions"
            inputValue=textBox.get("1.0","end-1c")
            dd = inputValue.split("\n")
            root.destroy()
            for x in dd:
                baza.append(x)
            for x in baza:
                y = x.split("/")[-1]
                z = x.split("/")[-1]
                nn = z.split("-")[0]
                os.system(f"curl -O {x}")
                rarobj = rarfile.RarFile(f"{y}")
                rarobj.extractall(dit_temp)
                time.sleep(3)
                os.system(f"del  {y}")
                sessions = []
                API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
                API_ID = 17463049
                for tdata in os.listdir("tdata_to_sessions"):
                        auth_key = convert_tdata(f"tdata_to_sessions/{tdata}/tdata")[0]


                        sessions.append(StringSession(auth_key))
                        logger.info("Проверка аккаунтов")
                        j = 0
                        for session in sessions:

                            j = j + 1
                            client =  TelegramClient(
                                session,
                                api_hash=API_HASH,
                                api_id=API_ID
                            )



                            client.connect()
                            auth_key =  client.session.save()
                            with open(f"sessions/{tdata}.session", "w") as file:
                                file.write(auth_key)
                                client.disconnect()
                                logger.success(f"{tdata} — сохранён.")

            import main
        textBox=Text(root, height=20, width=40)
        textBox.pack()
        buttonCommit=Button(root, height=1, width=10, text="Добавить", 
                            command=lambda: retrieve_input())
        #command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack()

        


        mainloop()
            







