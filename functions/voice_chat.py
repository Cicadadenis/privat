import asyncio
from pytgcalls import idle
from pytgcalls.types import AudioPiped
from pytgcalls import PyTgCalls
from telethon import utils
from rich.console import Console
from youtube_dl import YoutubeDL

from functions.function import Function

console = Console()


class VoicePlayFunc(Function):
    """Присоединяйтесь к голосовому чату"""

    async def join_and_play(self, session):
        await session.start()

        app = PyTgCalls(session)
        await app.start()
        entity = await session.get_entity(self.chat)

        await app.join_group_call(
            utils.get_peer_id(entity),
            AudioPiped(self.media_url)
        )

        await idle()


    async def execute(self):
        self.ask_accounts_count()

        self.chat = console.input("[bold red]ссылка на чат> [/]")
        
        console.print(
            "\n[bold white][1] Из Ютуба\n"
            "[2] Из прямой ссылки на файл[/]\n"
        )

        choice = console.input("[bold white]>> [/]")

        if choice == "1":
            url = console.input("[bold red]URL-адрес видео> [/]")
            ydl = YoutubeDL()

            r = ydl.extract_info(url, download=False)
            self.media_url = r['formats'][-1]['url']
        
        elif choice == "2":
            url = console.input("[bold red]url> [/]")
            self.media_url = url

        await asyncio.wait([
            self.join_and_play(session)
            for session in self.sessions
        ])
