from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon import functions, types
from rich.table import Table
from rich import print
from pprint import pprint
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest, GetGroupsForDiscussionRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import re
import csv
import pandas as pd
import asyncio
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import GetParticipantsRequest
from rich.prompt import Prompt
from rich.console import Console
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import LeaveChannelRequest

from telethon.tl.types import ChannelParticipantsSearch
import configparser
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import time
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import functions, types
from telethon import errors
from telethon.tl.types import PeerLocated, PeerUser
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import PeerChannel, InputPeerChannel, GroupCall
from rich.columns import Columns
import sys, os
import time
from rich.console import Console
from rich.panel import Panel
import rich
from geopy.geocoders import Nominatim
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logging.info('Hello')



console = Console()

def logo():
    console.print("[blink blue]      _             __         ___       __[/]", justify="center")
    console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
    console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
    console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
    console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")

api_hash = "b826075fd7ea762e6b9f853146d47995"
api_id = 1325339
session = TelegramClient(
                    StringSession("1ApWapzMBu8CmjHE47x8rCF3a7P6l9_mdPEmlFJd25VbEpnAqSSj5FdCwZ_13sbmNNqzWc6Qljztsy2AYLWKrS7391Lmut2t5pxUGe4tKyEsYdEhTjOMdySe1S97DwSxa7igieFUKTCW21C8nPxRXkPz4Cez5XGuSrUfgefkfcuzJolvKkVQd6BCza8ll_-Onk8bI8FgNngFg5_Mr329Lgd8ZGcZzKl87KeUEXrxjKFsJtLBCK2k7VU1LdMHnHDrt97kaNu9vfNQsBNAlDtpU16wc8HNsigj64AnuYelktnzqJaSOA3ZT2uEU7e7fxoDR3JNrWtOjY-4JbHD2MGB_WUWtoTuK-ms="),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
session.connect()

      

search = console.input(
        "[italic blink yellow]Критерий Поиска:    [/]  "
    )


result =   session(functions.contacts.SearchRequest(
    q=search,
    limit=100
))
open("chats.txt", "w")

for x in result.chats:
    ress = (
        f"\n\n###############################################################\n\n"
        f"Название:   {x.title}\n"
        f"---------------------------------------------------------------\n"
        f"Адрес:  http://t.me/{x.username}\n"
        f"---------------------------------------------------------------\n"
        f"Пользователей:  {x.participants_count}\n"
        f"---------------------------------------------------------------\n"
    )
    with open(f"chats.txt", "a", encoding="utf-8") as f:
        f.write(f"{ress}\n")
os.system("chats.txt")

            