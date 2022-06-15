import asyncio
import random
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
    """Спам По Списку"""

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

        console.print("[italic blue]\n\nСпам По Списку\n\n[/]", justify="center")
        a = open('ussers.txt', 'r', encoding='utf-8').readlines()
        self.ask_accounts_count()
        meees = open("message.txt", "r", encoding="utf-8").read()
        text = meees.split("$")

        baza = []
        for z in a:
            d = z.split("\n")
            for s in d:
                if s >= '0':
                    baza.append(s)

     

        pauza = int(console.input("[italic red]Задержка:    [/]"))
        os.system("cls")
        logo()
        for index, session in track(
            enumerate(self.sessions),
            "[italic yellow]Отправка смс...[/]" 
        ): 
            z = 0
            i = 0
            for x in baza:
                if i == 35:
                    break
                try:
                    async with self.storage.ainitialize_session(session):
                        me = await session.get_me()
                        try:
                            dd = await session.get_entity('809050978223')
                            print(dd)
                            input()
                            v = await session.get_input_entity(x)     
                        except:
                            continue
                        us = int(v.user_id)         
                        asa = await session.get_input_entity(PeerUser(us))
                        mes = random.choice(text)
                        i = i + 1  
                        await session.send_message(us, mes, parse_mode="html")
                        baza.remove(x) 
                        console.print("[italic green][{name}]Отправленно...[/]{x}".format(name=me.first_name, x=x))
                        z = 0
                        time.sleep(pauza)
                        open("ussers.txt", "w")
                        for x in baza:
                            with open("ussers.txt", "a", encoding="utf-8") as f:
                                f.write(f"{x}\n")
                except:
                    if z == 3:
                        break
                    console.print("[italic reverse red][{name}]Не Отправленно...[/]{x}".format(name=me.first_name, x=x))
                    time.sleep(3)
                    z = z + 1
                    #console.print(
                        #   "[{name}] [italic red]error.[/] {error}"
                        #  .format(name=me.first_name, error=err)
                    #)
                    