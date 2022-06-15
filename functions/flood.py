import asyncio
import os
import random
import time
from rich.prompt import Prompt, Confirm
from rich.console import Console
from multiprocessing import Process
from telethon import events, types

from functions.function import Function

console = Console()

class Flood(Function):
    def __init__(self, storage, settings):
        super().__init__(storage, settings)

        self.choice = None
        self.function = None

        self.modes = (
            ("Атака Текстом", self.text_flood),
            ("Одиночный бот рейд", self.text_flood),
            ("Атака с медиа", self.gif_flood),
            ("Атака с ответом", self.reply_flood)
        )

        self.reply_msg_id = 0

    async def text_flood(self, session, peer, text):
        await session.send_message(
            peer,
            text,
            parse_mode="html"
        )
        time.sleep(10)

    async def reply_flood(self, session, peer, text):
        await session.send_message(
            peer,
            text,
            reply_to=self.reply_msg_id,
            parse_mode="html"
        )
        time.sleep(10)

    async def gif_flood(self, session, peer, text):
        file = random.choice(os.listdir("media"))

        await session.send_file(
            peer,
            os.path.join("media", file),
            caption=text,
            parse_mode="html"
        )
        time.sleep(10)

    async def flood(self, session, peer, function):
        users = []
        admins = []

        admin_links = []

        count = 0
        errors = 0
        me = await session.get_me()

        if self.mention_all:
            admins = await session.get_participants(
                peer,
                filter=types.ChannelParticipantsAdmins
            )

            if self.mention_mode == "users":
                users = [
                    user for user in await session.get_participants(peer)
                    if user not in admins
                ]

                users_links = [
                    f"<a href=\"tg://user?id={user.id}\">\u206c\u206f</a>"
                    for user in users
                ]

            admin_links = [
                f"<a href=\"tg://user?id={user.id}\">\u206c\u206f</a>"
                for user in admins
            ]


        while count < self.settings.messages_count \
                or self.settings.messages_count == 0:
            if not self.mention_all:
                mes = open("message.txt", "r", encoding="utf-8").read()
                msg = mes.split("$")
                text = random.choice(msg)
            else:
                if function is not self.gif_flood:
                    mes = open("message.txt", "r", encoding="utf-8").read()
                    msg = mes.split("$")
                    text = random.choice(msg) + \
                        "\u206c\u206f".join(
                            random.sample(users_links, 15) if self.mention_mode == "users"
                            else random.sample(admin_links, len(admins) // 2)
                        )
                else:
                    mes = open("message.txt", "r", encoding="utf-8").read()
                    msg = mes.split("$")
                    text = random.choice(msg) + \
                        "\u206c\u206f".join(
                            random.sample(users_links, 5) if self.mention_mode == "users"
                            else random.sample(admin_links, len(admins) // 2)
                        )

            try:
                await function(session, peer, text)
            except Exception as err:
                console.print(
                    "[{name}] [italic red]не отправлено.[/] [italic green]{err}[/]"
                    .format(name=me.first_name, err=err)
                )

                errors += 1

                if errors >= 3:
                    break
            else:
                count += 1
                console.print(
                    "[{name}] [italic green]послал.[/] Послал: [italic yellow]{count}[/]"
                    .format(name=me.first_name, count=count)
                )
            finally:
                await self.delay()

    def handle(self, session, function):
        @session.on(events.NewMessage)
        async def handler(msg):
            if msg.raw_text == self.settings.trigger:
                await self.flood(
                    session,
                    msg.chat_id,
                    function,
                )

                if msg.reply_to:
                    self.reply_msg_id = msg.reply_to.reply_to_msg_id

        if not self.storage.initialize:
            session.start()

        session.run_until_disconnected()

    def ask(self):
        for index, mode in enumerate(self.modes):
            console.print(
                "[italic green][{index}] {description}[/]"
                .format(index=index + 1, description=mode[0]),
            )

        choice = console.input(
            "[italic green]>> [/]"
        )

        while not choice.isdigit():
            choice = console.input(
                "[italic green]>> [/]"
            )

        else:
            self.choice = int(choice) - 1

        self.function = self.modes[self.choice][1]
        self.ask_accounts_count()

        delay = Prompt.ask(
            "[italic red]задержка[/]",
            default="-".join(str(x) for x in self.settings.delay)
        )

        self.settings.delay = self.parse_delay(delay)
        self.mention_all = Confirm.ask("[italic red]Выбрать все?[/]", default="y")

        if self.mention_all:
            self.mention_mode = Prompt.ask(
                "[italic red]режим упоминания[/]",
                choices=["admins", "users"]
            )
        
        return self.choice
    
    async def start_single_raid(self, sessions, link):
        for session in sessions:
            await session.connect()

            await self.flood(
                session,
                link,
                self.function,
            )

    def start_processes(self):
        
        link = Prompt.ask("[italic red]ссылка на чат[/]")

        asyncio.get_event_loop().run_until_complete(self.start_single_raid(self.sessions, link))

        processes = []

        for session in self.sessions:
            if self.choice != 1:
                process = Process(
                    target=self.handle, args=[session, self.function]
                )

                process.start()
                processes.append(process)


        if self.choice != 1:
            console.print(
                "[italic green][*] послал «[italic green]{trigger}[/]» В чат[/]"
                .format(trigger=self.settings.trigger)
            )

            for process in processes:
                process.join()
