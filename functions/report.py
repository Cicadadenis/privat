import asyncio

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
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputReportReasonFake
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys, os
import csv
import re
import random
import traceback
import time
console = Console()


class ReportFunc(Function):
    """Запустить Report """

    def __init__(self, storage, settings):
        super().__init__(storage, settings)

        self.reasons = (
            ("Жестокое обращение с ребенком", types.InputReportReasonChildAbuse()),
            ("Авторские права", types.InputReportReasonCopyright()),
            ("Поддельный канал/аккаунт", types.InputReportReasonFake()),
            ("Порнография", types.InputReportReasonPornography()),
            ("Спам", types.InputReportReasonSpam()),
            ("Насилие", types.InputReportReasonViolence()),
            ("Другой", types.InputReportReasonOther())
        )

    async def execute(self):
        def logo():
            console.print("[blink blue]      _             __         ___       __[/]", justify="center")
            console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
            time.sleep(1)

        a = open('report.txt', 'r', encoding='utf-8').readlines()
        if len(a) >= 1:
            self.ask_accounts_count()
            baza = []
            for x in a:
                d = x.split("\n")
                for s in d:
                    if s >= '0':
                        baza.append(s)

            os.system("cls")
            logo()
            console.print("[italic blue]\n\nCнос Контактов (Report)\n\n[/]", justify="center")
            for index, reasons in enumerate(self.reasons):

                reason, _ = reasons

                console.print(
                    "\n[italic yellow][{}] {}[/]"
                    .format(index + 1, reason),
                    justify="center"
                )

            print()

            choice = int(console.input("[italic yellow]             Cicada3301 >>> [/]"))
            reason_type = self.reasons[choice - 1][1]

            comment = console.input("[italic red]         \n\nКоментарий/или просто жми Enter без него> [/]")
            for x in baza:


                for index, session in track(
                    enumerate(self.sessions),
                    "[yellow blink]Reporting...[/]"+x,
                    total=len(self.sessions)
                ):  
                    try:
                        f = random.randint(1,458)
                        iidd = [int(f)]
                        async with self.storage.ainitialize_session(session):
                            time.sleep(3)
                            me = await session.get_me()
                            try:
                                try:
                               
                                    v = await session.get_input_entity(x)   
                                    
                                    t = v
                                    console.print(
                                    "[{name}] [bold green]Отправил(a) Жалобу[/]".format(name=me.first_name))
                                    us = int(v.user_id)         
                                    asa = await session.get_input_entity(PeerUser(us))
                               
                                except:
                                    
                                    vvv = await session.get_input_entity(x)
                                 
                                    console.print(
                                    "[{name}] [bold green]Отправил(a) Жалоьу[/]".format(name=me.first_name))
                                    ttt = vvv
                                    
                                    usus = int(vv.channel_id)  
                                    asa = await session.get_input_entity(PeerChannel(usus))
                    
                           
                                
                            except Exception as err:
                                
                                console.print(
                                    "[{name}] [bold red]error.[/] {error}"
                                    .format(name=me.first_name, error=err)
                                )

                    except:
                        pass
            console.print("[italic blue]\n\nReport Завершил Отправку Жалоб[/]", justify="center")
            console.print("[italic blue]\nЧтобы Продолжить Жми Enter", justify="center")
            input()
        else:
            os.system("cls")
            logo()
            console.print("[italic blue]\n\n\nСписок Для Repor Пуст, Заполни Его", justify="center")
            time.sleep(5)