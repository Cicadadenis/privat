
import sys, os
from rich.console import Console
from opentele.api import API
from modules.settings import Settings
from telethon import errors
from tkinter import * 
from tkinter import filedialog, Tk, messagebox
from modules.sessions_storage import SessionsStorage
from modules.functions_storage import FunctionsStorage
from modules.Conwert import to_session
from rich.table import Table
from rich import print
from rich.style import Style
import time
import os
import sys
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from telethon import functions, types
from pprint import pprint
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest, GetGroupsForDiscussionRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import re
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

import sys
import logging
from rich.columns import Columns
import rarfile
import  shutil
import requests
from rich.progress import track
import time
from datetime import datetime, date, time
import time
import json
from urllib.request import urlopen
from probiv import prob
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
import rich
from threading import Timer
from datetime import datetime
from rich.table import Table
from rich.spinner import *
from datetime import datetime
from rich.traceback import install
import logging
import PySimpleGUI as sg
from functions.ch_add import ch_add_c
import pyautogui
import pyperclip

#FILENAME = r'cicada.png'          # if you want to use a file instead of data, then use this in Image Element
#ss = open(FILENAME, "rb").read()
#DISPLAY_TIME_MILLISECONDS = 8000

#sg.Window('Window Title', [[sg.Image(data=ss)]], transparent_color=sg.theme_background_color(), no_titlebar=True, keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)
pyautogui.hotkey('win', 'up')
pyautogui.press('F11')
logging.basicConfig(
    level=logging.DEBUG,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logging.info('Hello')
install(show_locals=True)

first_date = date.today()
second_date   =  date(2022, 6, 29)
delta = second_date - first_date



console = Console()

if delta == "0":
    console.print("\n\n\n\n\n[italic blink cyan]???????? Trial Version ?????????? !", justify="center")
    time.sleep(10)
    exit(1)
zazaz = f'Trial Version ???????????????? {delta.days} ????????'




console.set_window_title("Cicada3301")
console.get_datetime()
def logo():
    console.print("[blink blue]      _             __         ___       __[/]", justify="center")
    console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
    console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
    console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
    console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")

#print(logo)

os.system("cls")
console.print("\n\n\n\n\n[italic blink cyan]"+zazaz, justify="center")
time.sleep(5)

logo()
print("\n\n")
for step in track(                  range(100),style="bar.back", description="[italic blink yellow]                                         ????????????       ??????????????????...\n\n",):
    time.sleep(0.01)
                                                                                  
for step in track(                  range(100),    description="[italic blink yellow]                                         ????????????????????  ????????????????????...\n\n",           ):
    time.sleep(0.02)
                                                                                  
for step in track(                  range(100), description="[italic blink yellow]                                         ?????????????????????? ??  ??????????????...\n\n",):
    time.sleep(0.02)

console.print("[light_steel_blue bold]\n\n-------------------------------------------------------[/]\n\n", justify="center")

nam = []
nam2 = []

if sys.version_info < (3, 8, 0):
    console.print("\n[red]Error: ???? ?????????????????????? ???????????????????? ???????????? Python. ???????????????????? Python 3.9.0 ???? ?????????????? ????????.")
else:
    if sys.platform == "win32":
        pass



    while True:
        try:
            nam2.clear()
            settings = Settings()
            
            sessions_storage = SessionsStorage(
                "sessions",
                settings.api_id,
                settings.api_hash
            )    
            functions_storage = FunctionsStorage(
                "functions",
                sessions_storage,
                settings
            )
            #for  x in functions_storage.functions:
            #    f = x[0]
            #    ff = f()
            #    print(ff)
            #input()
            os.system("cls")
            print(Panel("[cayan blink bold]Hello, [red]World!", title="Welcome",  subtitle="Thank you"))
            logo()
            console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")

            try:
                ban = len(os.listdir("sessions/spamblock"))
            except:
                os.mkdir("sessions/spamblock")
                ban = len(os.listdir("sessions/spamblock"))
            uus = len(open("ussers.txt", 'r').readlines())
            try:
                pr = len(open("sessions/proxy.txt", "r").readlines())
            except:
                open("sessions/proxy.txt", "w")
                pr = len(open("sessions/proxy.txt", "r").readlines())
            try:
                rep = len(open("report.txt", "r").readlines())
            except:
                open("report", "w")
                rep = len(open("report.txt", "r").readlines())
            table = Table(show_header=True, caption_style='cyan', border_style='cyan', header_style="bold magenta", caption_justify="center", box=None, show_edge=False,  padding=(0, 1))
            table.add_column(f"????????????????", justify='center', style="cyan")
            table.add_column(f"?? ????????" , justify='center', style="cyan")
            table.add_column(f"????????????",justify='center', style="cyan")
            table.add_column(f"Users", justify='center', style="cyan")
            table.add_column(f"Reports", justify='center', style="cyan")
            table.add_row(
                f"[italik bold blue]{len(sessions_storage)}[/]", f"{ban}", f"auto", f"{uus}", f"{rep}"
            )
            os.system("cls")
            print(Panel("[cayan blink bold]", title="Cicada-Telegram-Soft",  subtitle="Cicada3301", style="on blue"))
            logo()
            console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
            console.print(table, justify="center")
            console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
            table2 = Table(show_header=True, border_style='cyan', header_style="bold magenta",box=None, show_edge=False)
            table2.add_column(f"???", style="blink cyan", footer_style='green' )
            table2.add_column(f"??????????????", style="cyan")
            
            fo = []

            texxt = f"[+]???????????????? {len(sessions_storage)}   [+]?? ???????? {ban}    [+]???????????? {pr}    [+]?????????????????????????? {uus}"
            #console.print("[reverse silver]\n "+texxt+" [/]\n" , justify="center")
            
            table2.add_row('[italic bold]'
            f"1", f"????????????????\n"
            )
            table2.add_row('[italic bold]'
            f"2", f"??????????????????\n"
            )
            table2.add_row('[italic bold]'
            f"3", f"????????????????????\n"
            )
            table2.add_row('[italic bold]'
            f"4", f"???????????? ?? ??????????????????\n"
            )
            table2.add_row('[italic bold]'
            f"5", f"??????????????\n"
            )
            table2.add_row('[italic bold]'
            f"6", f"?????????? ??????????\n"
            )
            table2.add_row('[italic bold]'
            f"7", f"???????????? ???? ???????????? ?? ???????? ????\n"
            )
            table2.add_row('[italic bold]'
            f"x", f"?????????? ?? ??????????????????"
            )

                #console.print(
                #    "[italic  yellow]                                         [{index}]       {doc}[/]"
                #    .format(index=index + 1, doc=doc),justify="left"
                #)

            #console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
            console.print(table2, justify="center")
            #console.print()
            console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
            vv = console.input(
                    "[italic blink yellow]                                       Cicada3301 >>>  [/]  "
            
            )
            if vv == "7":
                prob()
            if vv == "x":
                os.system("cls")
                logo()
                console.print('[bold blink cyan]\n\n\n\n?????????????????? ?????????????????? ?? ???????????????? ??????????????????', justify="center")
                time.sleep(5)
                break
            if vv == "1":
                ban = len(os.listdir("sessions/spamblock"))
                uus = len(open("ussers.txt", 'r').readlines())
                pr = len(open("sessions/proxy.txt", "r").readlines())
                rep = len(open("report.txt", "r").readlines())
                table = Table(show_header=True, caption_style='cyan', border_style='cyan', header_style="bold magenta", caption_justify="center", box=None, show_edge=False,  padding=(0, 1))
                table.add_column(f"????????????????", justify='center', style="cyan")
                table.add_column(f"?? ????????" , justify='center', style="cyan")
                table.add_column(f"????????????",justify='center', style="cyan")
                table.add_column(f"Users", justify='center', style="cyan")
                table.add_column(f"Reports", justify='center', style="cyan")
                table.add_row(
                    f"[italik bold blue]{len(sessions_storage)}[/]", f"{ban}", f"auto", f"{uus}", f"{rep}"
                )
                os.system("cls")
                logo()
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                table2 = Table(show_header=True, border_style='cyan', header_style="bold magenta",box=None, show_edge=False)
                table2.add_column(f"???", style="blink cyan", footer_style='green' )
                table2.add_column(f"??????????????", style="cyan")
                
            
                texxt = f"[+]???????????????? {len(sessions_storage)}   [+]?? ???????? {ban}    [+]???????????? {pr}    [+]?????????????????????????? {uus}"
                #console.print("[reverse silver]\n "+texxt+" [/]\n" , justify="center")
                
                table2.add_row('[italic bold]'
                    f"1", f"?????????????????? Users ?????? Report\n")
                table2.add_row('[italic bold]'
                    f"2", f"???????????????? Users ?????? Report\n")
                table2.add_row('[italic bold]'
                    f"3", f"?????????????????? ???????? ???????????? ?????? ??????????\n")
                table2.add_row('[italic bold]'
                    f"4", f"?????????????????? ???????????? ????????????\n")
                table2.add_row('[italic bold]'
                    f"5", f"?????????????????? ????????/??????????/???????? ?????? ??????????\n")
                table2.add_row('[italic bold]'
                    f"6", f"?????????????????? ?????????? ???????? ??????????????????\n")
                table2.add_row('[italic bold]'
                    f"7", f"?????????????????? ???????? ???? ????????????????????\n")

                table2.add_row('[italic bold]'
                    f"x", f"??????????")
       
         
                    #console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table2, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                vv = console.input(
                        "[italic blink yellow]                                      Cicada3301 >>>  [/]  "
                    )
                if vv == '1':
                    functions_storage.execute(0)
                    continue
                if vv == '2':
                    open("report.txt", "w")
                    os.system("cls")
                    logo()
                    console.print("[bold italic blue]???????????? ?????? Report ???????????? !", justify="center")
                    time.sleep(3)
                    continue
                if vv == '3':
                    functions_storage.execute(2)
                    continue
                if vv == "4":
                    functions_storage.execute(3)
                    continue
                if vv == "5":
                    functions_storage.execute(4)
                    continue
                if vv == "6":
                    functions_storage.execute(9)
                    continue
                if vv == "7":
                    ch_add_c()
                    continue
                if vv == 'x':
                    continue
                else:
                    os.system("cls")
                    logo()
                    console.print("[red bold italic]\n\n\n\n???????????????? ???????? [/]", justify='center')
                    time.sleep(3)
            if vv == 'den':
                api_hash = "b826075fd7ea762e6b9f853146d47995"
                api_id = 1325339
                for file in os.listdir(sessions):
                    if file.endswith(".session"):
                        session_path = os.path.join("sessions", file)
                        
                        with open(session_path) as fileobj:
                            auth_key = fileobj.read()
                        try:
                            session = TelegramClient(
                                StringSession(auth_key),
                                api_id,
                                api_hash,
                                device_model="Redmi Note 10",
                                lang_code="en",
                                system_lang_code="en"
                            )
                            session.connect()
                            xxxx = open("aaa.txt", 'r').readlines()[-1]
                            print(xxxx)
                            input()
                            for invite in xxxx: 
                                session(JoinChannelRequest(invite))
                        except:pass
            if vv == '2':
                if len(sessions_storage) <= 0:
                    os.system("cls")
                    logo()
                    console.print("[bold italic red]\n\n\n\n?????????????? ???????????? ??????????????[/]", justify="center")
                    time.sleep(5)
                    continue
                ban = len(os.listdir("sessions/spamblock"))
                uus = len(open("ussers.txt", 'r').readlines())
                pr = len(open("sessions/proxy.txt", "r").readlines())
                rep = len(open("report.txt", "r").readlines())
                table = Table(show_header=True, caption_style='cyan', border_style='cyan', box=None, show_edge=False, header_style="bold magenta", padding=(0, 1))
                table.add_column(f"????????????????", style="cyan")
                table.add_column(f"?? ????????" , style="cyan")
                table.add_column(f"????????????",style="cyan")
                table.add_column(f"Users", justify='center', style="cyan")
                table.add_column(f"Reports", justify='center', style="cyan")
                table.add_row(
                    f"[italik bold blue]{len(sessions_storage)}[/]", f"{ban}", f"auto", f"{uus}", f"{rep}"
                )
                os.system("cls")
                logo()
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                table2 = Table(show_header=True, border_style='cyan', box=None, show_edge=False, header_style="bold magenta")
                table2.add_column(f"???", style="blink cyan", footer_style='green' )
                table2.add_column(f"??????????????", style="cyan")
                table2.add_row('[italic bold]'
                    f"1", f"???????????????? ??????????????????\n")
                table2.add_row('[italic bold]'
                    f"2", f"???????????????? ??????????\n")
                table2.add_row('[italic bold]'
                    f"3", f"???????????????? ???????? ??????????????\n")
                table2.add_row('[italic bold]'
                    f"x", f"??????????")
           
                #console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table2, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                xx = console.input(
                        "[italic blink yellow]                                      Cicada3301 >>>  [/]  "
                    )
                if xx =='1':
                        
                    continue
                if xx == "2":
                    functions_storage.execute(7)
                    continue
                if xx == "3":
                    functions_storage.execute(10)
                    continue
                if xx == 'x':
                    continue
                else:
                    os.system("cls")
                    logo()
                    console.print("[red bold italic]\n\n\n\n???????????????? ???????? [/]", justify='center')
                    time.sleep(3)
                
            if vv == '3':
                ban = len(os.listdir("sessions/spamblock"))
                uus = len(open("ussers.txt", 'r').readlines())
                pr = len(open("sessions/proxy.txt", "r").readlines())
                rep = len(open("report.txt", "r").readlines())
                table = Table(show_header=True, caption_style='cyan', border_style='cyan', box=None, show_edge=False, header_style="bold magenta", padding=(0, 1))
                table.add_column(f"????????????????", style="cyan")
                table.add_column(f"?? ????????" , style="cyan")
                table.add_column(f"????????????",style="cyan")
                table.add_column(f"Users", justify='center', style="cyan")
                table.add_column(f"Reports", justify='center', style="cyan")
                table.add_row(
                    f"[italik bold blue]{len(sessions_storage)}[/]", f"{ban}", f"auto", f"{uus}", f"{rep}"
                )
                os.system("cls")
                logo()
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                table2 = Table(show_header=True, border_style='cyan', box=None, show_edge=False, header_style="bold magenta")
                table2.add_column(f"???", style="blink cyan", footer_style='green' )
                table2.add_column(f"??????????????", style="cyan")
                table2.add_row('[italic bold]'
                    f"1", f"?????????????????? ?? Sessions ???? URL\n")
                table2.add_row('[italic bold]'
                    f"2", f"?????????????? SQLiteSession\n")
                table2.add_row('[italic bold]'
                    f"3", f"?????????????????? ?? ?????????????? Tdata\n")
                table2.add_row('[italic bold]'
                    f"x", f"??????????")
  
                #console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table2, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                xx = console.input(
                        "[italic blink yellow]                                      Cicada3301 >>>  [/]  "
                    )
                if xx =='1':
                    functions_storage.execute(11)
                    continue
                if xx == "2":
                    functions_storage.execute(12)
                    continue
                if xx == "3":
                    functions_storage.execute(13)
                    continue
                if xx == "x":
                    continue
                else:
                    os.system("cls")
                    logo()
                    console.print("[red bold italic]\n\n\n\n???????????????? ???????? [/]", justify='center')
                    time.sleep(3)

            if vv == '4':
                if len(sessions_storage) <= 0:
                    os.system("cls")
                    logo()
                    console.print("[bold italic red]\n\n\n\n?????????????? ???????????? ??????????????[/]", justify="center")
                    time.sleep(5)
                    continue
                ban = len(os.listdir("sessions/spamblock"))
                uus = len(open("ussers.txt", 'r').readlines())
                pr = len(open("sessions/proxy.txt", "r").readlines())
                rep = len(open("report.txt", "r").readlines())
                table = Table(show_header=True, caption_style='cyan', border_style='cyan',box=None, show_edge=False,  header_style="bold magenta", padding=(0, 1))
                table.add_column(f"????????????????", style="cyan")
                table.add_column(f"?? ????????" , style="cyan")
                table.add_column(f"????????????",style="cyan")
                table.add_column(f"Users", justify='center', style="cyan")
                table.add_column(f"Reports", justify='center', style="cyan")
                table.add_row(
                    f"[italik bold blue]{len(sessions_storage)}[/]", f"{ban}", f"auto", f"{uus}", f"{rep}"
                )
                os.system("cls")
                logo()
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                table2 = Table(show_header=True, border_style='cyan',box=None, show_edge=False,  header_style="bold magenta")
                table2.add_column(f"???", style="blink cyan", footer_style='green' )
                table2.add_column(f"??????????????", style="cyan")
                table2.add_row('[italic bold]'
                    f"1", f"???????????????? ?????? ??????????????\n")
                table2.add_row('[italic bold]'
                    f"2", f"???????????? ??????????\n")
                table2.add_row('[italic bold]'
                    f"3", f"?????????????????????????????? ?? ???????????????????? ????????Tdata\n")
                table2.add_row('[italic bold]'
                    f"4", f"?????????????????????????????? ?? ????????\n")
                table2.add_row('[italic bold]'
                    f"5", f"?????????????????? ???? ????????\n")
                table2.add_row('[italic bold]'
                    f'6', f"???????????????????? 2fa ????????????\n"
                )
                table2.add_row('[italic bold]'
                    f'7', f"?????????????? ?????????????? ?????????????? ?? ????????\n"
                )
                table2.add_row('[italic bold]'
                    f'8', f"????????????\n"
                )
                table2.add_row('[italic bold]'
                    f'x', f"??????????"
                )
      
               # console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table2, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                xx = console.input(
                        "[italic blink yellow]                                      Cicada3301 >>>  [/]  "
                    )
                if xx =='1':
                    functions_storage.execute(14)
                    continue
                if xx == "2":
                    functions_storage.execute(15)
                    continue
                if xx == "3":
                    functions_storage.execute(16)
                    continue
                if xx =='4':
                    functions_storage.execute(17)
                    continue
                if xx == "5":
                    functions_storage.execute(18)
                    continue
                if xx == "6":
                    functions_storage.execute(22)
                    continue
                if xx == "7":
                    with rich.progress_bar():
                        os.system("cls")
                        logo()
                        os.system("del /S/Q sessions/spamblock")
                        time.sleep(2)
                        os.mkdir("sessions/spamblock")
                    
                    continue
                if xx == "8":
                    from sup_invait import inv
                    inv()
                    continue
                if xx == "x":
                    continue
                else:
                    os.system("cls")
                    logo()
                    console.print("[red bold italic]\n\n\n\n???????????????? ???????? [/]", justify='center')
                    time.sleep(3)
                


            if vv == '5':
                if len(sessions_storage) <= 0:
                    os.system("cls")
                    logo()
                    console.print("[bold italic red]\n\n\n\n?????????????? ???????????? ??????????????[/]", justify="center")
                    time.sleep(5)
                    continue
                ban = len(os.listdir("sessions/spamblock"))
                uus = len(open("ussers.txt", 'r').readlines())
                if uus <= 0:
                    os.system("cls")
                    logo()
                    console.print("[bold italic red]?????????????? ???????????? Users ?????? ??????????[/]", justify="center")
                    time.sleep(5)
                    continue
                pr = len(open("sessions/proxy.txt", "r").readlines())
                rep = len(open("report.txt", "r").readlines())
                ms = len(open("message.txt", "r", encoding="utf-8").read())
                if ms <= 0:
                    os.system("cls")
                    logo()
                    console.print("[bold italic red]?????????????? ???????????? ?????????? ?????? ??????????[/]", justify="center")
                    time.sleep(5)
                    continue
                table = Table(show_header=True, caption_style='cyan', border_style='cyan',box=None, show_edge=False,  header_style="bold magenta", padding=(0, 1))
                table.add_column(f"????????????????", style="cyan")
                table.add_column(f"?? ????????" , style="cyan")
                table.add_column(f"????????????",style="cyan")
                table.add_column(f"Users", justify='center', style="cyan")
                table.add_column(f"Reports", justify='center', style="cyan")
                table.add_row(
                    f"[italik bold blue]{len(sessions_storage)}[/]", f"{ban}", f"auto", f"{uus}", f"{rep}"
                )
                os.system("cls")
                logo()
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                table2 = Table(show_header=True, border_style='cyan', box=None, show_edge=False, header_style="bold magenta")
                table2.add_column(f"???", style="blink cyan", footer_style='green' )
                table2.add_column(f"??????????????", style="cyan")
                table2.add_row('[italic bold]'
                    f"1", f"???????? ???? ????????????\n")
                table2.add_row('[italic bold]'
                    f"2", f"???????? ???? ???????????? ?????????????? ?? ??????????????????\n")
                table2.add_row('[italic bold]'
                    f"3", f"???????? ?? ??????????\n")
                table2.add_row('[italic bold]'
                    f"4", f"???????? ?? ??????\n")
                table2.add_row('[italic bold]'
                    f"5", f"???????? ???? ?????????????????????? ?? ????????????\n")
                table2.add_row('[italic bold]'
                    f"6", f"?????????????????? Report\n")
                table2.add_row('[italic bold]'
                    f'x', f"??????????"
                )
  
               # console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table2, justify="center")
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                xx = console.input(
                        "[italic blink yellow]                                      Cicada3301 >>>  [/]  "
                    )
                if xx =='1':
                    functions_storage.execute(20)
                    continue
                if xx == "2":
                    functions_storage.execute(21)
                    continue
                if xx == "3":
                    functions_storage.execute(23)
                    continue
                if xx == '4':
                    functions_storage.execute(24)
                    continue
                if xx == "5":
                    functions_storage.execute(25)
                    continue
                if xx == "6":
                    functions_storage.execute(5)
                    continue
                if xx == "x":
                    continue
                else:
                    os.system("cls")
                    logo()
                    console.print("[red bold italic]\n\n\n\n???????????????? ????????[/]", justify='center')
                    time.sleep(3)


            if vv == '6':
                os.system("cls")
                logo()
                console.print("[light_steel_blue bold]\n------------------------------------------------[/]\n", justify="center")
                console.print(table, justify="center")
                
                console.print("[light_steel_blue, bold]\n------------------------------------------------[/]\n", justify="center")
                
                console.print("[bold italic yellow  red blink]\n\n\n?????????? ??????????[/]\n\n", justify="center")
                
                api_hash = "b826075fd7ea762e6b9f853146d47995"
                api_id = 1325339
                for file in os.listdir(f"sessions"):
                    if file.endswith(".session"):
                        session_path = os.path.join("sessions", file)
                        try:
                           with open(session_path) as fileobj:
                               auth_key = fileobj.read()
                           session = TelegramClient(
                                               StringSession(auth_key),
                                               api_id,
                                               api_hash,
                                               device_model="Redmi Note 10",
                                               lang_code="en",
                                               system_lang_code="en"
                                           )
                           session.connect()
                        except:pass
                        q = console.input(
                                "[italic blink yellow]???????????????? ????????????:    [/]  "
                            )

                        result = []
                        try:
                            result =  session(
                                functions.contacts.SearchRequest(
                                    q, 
                                    limit=100
                                    )
                                ) 

                            open("chats.txt", "w")

                            for x in result.chats:
                                ress = (
                                    f"\n\n###############################################################\n\n"
                                    f"????????????????:   {x.title}\n"
                                    f"---------------------------------------------------------------\n"
                                    f"??????????:  http://t.me/{x.username}\n"
                                    f"---------------------------------------------------------------\n"
                                    f"??????????????????????????:  {x.participants_count}\n"
                                    f"---------------------------------------------------------------\n"
                                )
                                with open(f"chats.txt", "a", encoding="utf-8") as f:
                                    f.write(f"{ress}\n")
                            os.system("chats.txt")
                            break
                        except:pass
            else:
                os.system("cls")
                logo()
                console.print("[red bold italic]\n\n\n\nError: ???????????????? ????????[/]", justify="center")
                time.sleep(4)

        except:
            pass



