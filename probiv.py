import os
from opentele.td import TDesktop
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from opentele.api import API, UseCurrentSession
import asyncio
from telethon.sync import TelegramClient as den
from telethon.tl.types import PeerChannel, InputPeerChannel, GroupCall, ImportedContact
#async def main():
from telethon.tl.types import InputPhoneContact
from telethon import functions, types
from rich.console import Console

def prob():
        
    c = Console()
    def logo():
        c.print("[blink blue]      _             __         ___       __[/]", justify="center")
        c.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
        c.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
        c.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
        c.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
    os.system("cls")
    logo()
    i = 1
    for ses in os.listdir("sessions"):
        if ses.split("session"):
            #try:
                guest_phone_number= c.input("[bold italic green]\n\n\nВведи Номер Телефона Для Проверки Его В Базе: [/]")
                api = API.TelegramAndroid.Generate()
                try:
                    with open(f"sessions/{ses}", "r") as f:
                        sss = f.read()
                    client = TelegramClient(StringSession(f"{sss}"), api_id=api.api_id, api_hash=api.api_hash)
                    client.connect()
                except:pass
                xyx = "satanasat"
                us = "tarmtram444"
                try:
                    contact = InputPhoneContact(client_id=0, phone=guest_phone_number, first_name="custom_first_name", last_name="custom_last_name")
                    result = client(functions.contacts.ImportContactsRequest([contact]))
                    contact_info = client.get_entity(guest_phone_number)
                    c.print("[bold blue italic]id                  [/][bold italic cayan]{id}[/]".format(id=contact_info.id))
                    c.print("[bold blue italic]is_self             [/][bold cayan italic]{is_self}[/]".format(is_self=contact_info.is_self))
                    c.print("[bold blue italic]contact             [/][bold cayan italic]{contact}[/]".format(contact=contact_info.contact))
                    c.print("[bold blue italic]mutual_contact      [/][bold italic cayan]{mutual_contact}[/]".format(mutual_contact=contact_info.mutual_contact))
                    c.print("[bold blue italic]deleted             [/][bold italic cayan]{deleted}[/]".format(deleted=contact_info.deleted))
                    c.print("[bold blue italic]bot                 [/][bold italic cayan]{bot}[/]".format(bot=contact_info.bot))
                    c.print("[bold blue italic]bot_chat_history    [/][bold italic cayan]{bot_chat_history}[/]".format(bot_chat_history=contact_info.bot_chat_history))
                    c.print("[bold blue italic]bot_nochats         [/][bold italic cayan]{bot_nochats}[/]".format(bot_nochats=contact_info.bot_nochats))
                    c.print("[bold blue italic]verified            [/][bold italic cayan]{verified}[/]".format(verified=contact_info.verified))
                    c.print("[bold blue italic]min                 [/][bold italic cayan]{min}[/]".format(min=contact_info.min))
                    c.print("[bold blue italic]bot_inline_geo      [/][bold italic cayan]{bot_inline_geo}[/]".format(bot_inline_geo=contact_info.bot_inline_geo))
                    c.print("[bold blue italic]support             [/][bold italic cayan]{support}[/]".format(support=contact_info.support))
                    c.print("[bold blue italic]scam                [/][bold italic cayan]{scam}[/]".format(scam=contact_info.scam))
                    c.print("[bold blue italic]apply_min_photo     [/][bold italic cayan]{apply_min_photo}[/]".format(apply_min_photo=contact_info.apply_min_photo))
                    c.print("[bold blue italic]access_hash         [/][bold italic cayan]{access_hash}[/]".format(access_hash=contact_info.access_hash))
                    c.print("[bold blue italic]username            [/][bold italic cayan]{username}[/]".format(username=contact_info.username))
                    c.print("[bold blue italic]phone               [/][bold italic cayan]{phone}[/]".format(phone=contact_info.phone))
                    c.print("[bold blue italic]photo               [/][bold italic cayan]{photo}[/]".format(photo=contact_info.photo))
                    c.print("[bold blue italic]status              [/][bold italic cayan]{status}[/]".format(status=contact_info.status))
                    c.input("[bold green italic]\n\nЧтобы Продолжить Нажми [/][italic blink yellow]Enter[/]")
                    break
                except:
                    c.print("[bold red italic]\n\n\nНомер В Базе Не Зарегистрирован[/]", justify="center")