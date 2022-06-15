import asyncio
import random
import asyncio
import os
import random
from rich.prompt import Prompt, Confirm
from rich.console import Console
from multiprocessing import Process
from telethon import events, types
import pyautogui
import pyperclip
from functions.function import Function
from rich.progress import track
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
    """Спам По Списку Текстом И Картинкой"""

    def __init__(self, storage, settings):
        super().__init__(storage, settings)

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
        console.print("[italic blue]\n\nСпам По Списку Текстом И Картинкой\n\n[/]", justify="center")
        file = random.choice(os.listdir("media"))
        a = open('ussers.txt', 'r', encoding='utf-8').readlines()
        self.ask_accounts_count()
        meees = open("message.txt", "r", encoding="utf-8").read()
        if len(meees) >= 500:
            os.system("cls")
            logo()
            console.print("[italic red]\n\n\n\n\nТекст Не Должен Привышать Более 500 Символов В Режиме Отправки Вместе С Медиа Файлом...[/]" , justify="center")
            time.sleep(5)
            console.print("[bold green italic]\n\n\nЧтобы Продолжить нажми Enter[/]", justify='center')
            input()
        else:
            text = meees.split("$")
            baza = []
            for z in a:
                d = z.split("\n")
                for s in d:
                    if s >= '0':
                        baza.append(s)




            pauza = int(console.input("[italic red]Задержка:    [/]"))
            os.system("cls")
            print(log())
            for index, session in track(
                enumerate(self.sessions),
                "[italic yellow]Отправка смс...[/]" + s
            ): 
                i = 0
                for x in baza:
                    if i <= 35:
                        try:
                            async with self.storage.ainitialize_session(session):
                                me = await session.get_me()
                                try:
                                    v = await session.get_input_entity(x) 
                                except:
                                    pass
                                us = int(v.user_id)         
                                mes = random.choice(text)
                                await session.send_file(
                                    us,
                                    os.path.join("media", file),
                                    caption=mes,
                                    parse_mode="html"
                                )
                                baza.remove(x) 
                                console.print("[italic yellow]Отправленно...[/]" + x)
                                i = i + 1  
                                time.sleep(pauza)
                                open("ussers.txt", "w")
                                for x in baza:
                                    with open("ussers.txt", "a", encoding="utf-8") as f:
                                        f.write(f"{x}\n")
                        except Exception as err:
                            pass
                            console.print(
                                "[{name}] [italic red]error.[/] {error}"
                                .format(name=me.first_name, error=err)
                            )
