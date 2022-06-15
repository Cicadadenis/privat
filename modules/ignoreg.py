


import os
import asyncio
from rich.console import Console
from contextlib import contextmanager, asynccontextmanager
from typing import List, Dict
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import socks
import time
from modules.Conwert import to_session
console = Console()




no_akk = (
f"                              {re}У тебя нет Акаунтов{gr}\n\n"


f"              {re}1.  Загрузи Акаунты Tdata В папку tdata_to_sessions Для Конвертации В sessions{gr}\n\n"

f"              {re}2.  Загрузить Купленные Акаунты Ссылками На rar Архив{gr}\n\n"

f"              {re}3   Перенести По Номеру{gr}\n\n" 

f"              {re}x.  Выход{gr}\n\n"
            
            )
print(no_akk)
mode = console.input("[bold red]        Выбор Загрузки:    [/] ")
if mode == 1:

    ses = os.listdir("tdata_to_sessions")
    if len(ses) >= 1:
        os.system("cls")
        print(logo)
        to_session()
    else:
        console.print("[bold red]       В Папке tdata_to_sessions Отсутствует Акаунты[/] ")
        time.sleep(5)

if mode == 2:
    try:
        url_ses = open("sessions\\URL_to_sessions.txt", "r").readlines()
        for x in url_ses:
            dir_name = "tdata_to_sessions"
            rar_file = x.split('/')[9][:-1]
            if len(rar_file) == 17:
                    rar_file = f"{rar_file}r"
                    os.system(f"curl -O  {x}")
            os.system(f"curl -O  {x}")        
            rarobj = rarfile.RarFile(rar_file)
            rarobj.extractall(dir_name)
            os.system(f"del /S /Q {rar_file}")
        to_session()
    except:
        console.print("[bold red]       В Ссылки  На  Акаунты Отсутствуют[/] ")
        time.sleep(5)
if mode == 3:
    import py.sessions_add
if mode == 'x':
    exit(1)


