import random
import os

from telethon import functions, types

from rich.progress import track
from rich.console import Console

from functions.function import Function

console = Console()


class ChangeProfilePhotoFunc(Function):
    """Изменить фото профиля"""

    async def execute(self):
        path = os.path.join(os.getcwd(), "assets", "photos")
        console.input(
            f"\n[bold green]будут использованы фотографии из папки {path}"
            "\nНажмите [Enter], чтобы продолжить[/]"
        )
        
        photos = os.listdir(path)

        for index, session in track(
            enumerate(self.sessions),
            "[yellow]Установка фотографий...[/]",
            total=len(self.sessions)
        ):
            photo = os.path.join(
                path, random.choice(photos)
            )

            async with self.storage.ainitialize_session(session):
                try:
                    await session(functions.photos.UploadProfilePhotoRequest(
                        file=await session.upload_file(photo),
                    ))
                except Exception as err:
                    console.print("[{name}] [bold red]error.[/] {err}".format(name=(await session.get_me()).first_name, error=err))

