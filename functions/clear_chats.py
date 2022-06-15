import asyncio
from telethon import functions, types, TelegramClient
from rich.console import Console
from rich.prompt import Confirm
import time, os
from functions.function import Function

console = Console()


class ClearDialogsFunc(Function):
    """Очистить все диалоги"""

    async def clear(self, session: TelegramClient):
        async with self.storage.ainitialize_session(session):
            async for dialog in session.iter_dialogs():
                console.log(dialog)

                if not isinstance(dialog.entity, types.Channel):
                    await session(functions.messages.DeleteHistoryRequest(
                        peer=dialog.entity,
                        max_id=0,
                        just_clear=True,
                        revoke=True
                    ))
                else:
                    await session(
                        functions.channels.LeaveChannelRequest(dialog.id)
                    )

                console.log(dialog)

    async def execute(self):
        def logo():
            console.print("[blink blue]     _             __         ___       __[/]", justify="center")
            console.print("[blink blue] ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow]/ __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
            time.sleep(2)
        os.system("cls")
        logo()
        console.print("[italic blue]\n\nСтереть все Диалоги\n\n[/]", justify="center")
        confirm = Confirm.ask("[italic red]\n\nуверен ?[/]")

        if confirm:
            try:
                await asyncio.wait([
                    self.clear(session)
                    for session in self.sessions
                ])
            except:
                pass

