import string
import random
import toml
import socks
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import utils



with open("../config.toml") as file:
    config = toml.load(file)["sessions"]
try:
    with open('proxy.txt', 'r') as f:
            proxys = f.readline().split(":")
            s = socks.socksocket()
except:
    pass
api_id = config["api_id"]
api_hash = config["api_hash"]

name = "".join(random.choices(string.ascii_letters, k=10))
try:
    with TelegramClient(
        StringSession(),
        api_id,
        api_hash,
        proxy = s.set_proxy(socks.SOCKS5, f'{proxys[0]}', int(proxys[1]), f'{proxys[2]}', f'{proxys[3]}'),
        device_model="Redmi Note 10",
        lang_code="en",
        system_lang_code="en"
    ) as client:
        with open(f"{name}.session", "w") as file:
            file.write(client.session.save())
except:
    with TelegramClient(
        StringSession(),
        api_id,
        api_hash,
        device_model="Redmi Note 10",
        lang_code="en",
        system_lang_code="en"
    ) as client:
        with open(f"{name}.session", "w") as file:
            file.write(client.session.save())
    me = client.get_me()
    print(me.stringify())
    for dialog in client.get_dialogs():
        print(dialog.name, 'has ID', dialog.id)
    entity = client.get_entity('satanasat')
    peer = utils.get_input_peer(entity)
    print(peer)