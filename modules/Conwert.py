
from telethon.sessions import StringSession
from modules.convert_tdata import *
import time
from telethon.sync import TelegramClient
from telethon import connection
from loguru import logger
from tkinter import *
from tkinter import Tk
from tkinter import filedialog



sessions = []
API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
API_ID = 17463049


def to_session():
    ff = filedialog.askdirectory()
    for tdata in os.listdir(ff):
        try:
            auth_key = convert_tdata(f"{ff}/{tdata}/tdata")[0]



            sessions.append(StringSession(auth_key))

            logger.info("Проверка аккаунтов")
            j = 0
            for session in sessions:
                try:
                    j = j + 1
                    client = TelegramClient(
                        session,
                        api_hash=API_HASH,
                        api_id=API_ID
                    )
        



                    client.connect()
                    auth_key = client.session.save()
                    with open(f"sessions/{tdata}.session", "w") as file:
                        file.write(auth_key)
                        client.disconnect()
                        logger.success(f"{tdata} — сохранён.")
                except:
                    logger.info(f"Аккаунт {session} Мертв !")
        except:
            pass
    os.system("rmdir /S/Q tdata_to_sessions")
    time.sleep(5)
    os.mkdir("tdata_to_sessions")