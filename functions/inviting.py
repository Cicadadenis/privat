import random
import asyncio
import os, time
from telethon import functions, types
from telethon import errors
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import GetParticipantsRequest
from rich.prompt import Prompt
from rich.console import Console
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import LeaveChannelRequest
from functions.function import Function
from telethon.tl.types import ChannelParticipantsSearch
console = Console()


class InvitingFunc(Function):
    """Парсер Групп"""

    @staticmethod
    def transform_to_valid_invite(link):
        if "t.me" in link:
            if "joinchat" in link:
                invite = link.split("/")[-1]
            else:
                invite = "@" + link.split("/")[-1]
        elif link.startswith("@"):
            invite = link

        return invite

    @staticmethod
    def chunkify(lst, n):  # split list
        return [lst[i::n] for i in range(n)]
   
    async def invite(self, users, channel, session):
        users_for_invite = []

        async with self.storage.ainitialize_session(session):
            channel = await session.get_entity(channel)
            for user in users: 
                if user.username:
                    user = await session.get_entity(user.username)
                    users_for_invite.append(user)

            for user in users_for_invite:
                try:
                    await session(InviteToChannelRequest(
                        channel=channel,
                        users=[user]
                    ))
                except PeerFloodError as err:
                    console.print(f"[bold red]{err}[/]")
                    return
                except UserPrivacyRestrictedError:
                    pass

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
        console.print("[italic blue]\n\nПарсинг Групп\n\n[/]", justify="center")
        accounts_count = int(str(len(self.sessions)))

        self.sessions = self.sessions[:accounts_count]
        #spisok = open("aaa.txt", "r", encoding="utf-8").readlines()[:-1]
        #for x in spisok:
        #    link = x
        #    break
        link = console.input("[italic red]ссылка на группу> [/]")
        invite = self.transform_to_valid_invite(link)

        session = None

        with console.status("Парсинг пользователей...", spinner="dots"):
            try:
                ses = []
                for session in self.sessions:
                    ses.append(session)
                    session = random.choice(ses)
                    await session.connect()
                    chats = []
                    last_date = None
                    chunk_size = 200
                    groups=[]
                    offset_user = 0
                    limit_user = 200
                    all_participants = [] 
                    filter_user = ChannelParticipantsSearch('')
                    try:
                        await session(JoinChannelRequest(invite))
                    except errors.FloodWaitError as e:
                        console.print('[bold red italic]\n\nАкаунт Получил Flood На {e} Секунд[/]'.format(e=e.seconds), justify="center")
                        time.sleep(3)
                        break
                    try:
                        participants = await session(GetParticipantsRequest(invite,
                            filter_user, offset_user, limit_user, hash=0))
                        all_participants.extend(participants.users)

                        offset_user += len(participants.users)
                        all_users_details = [] 
                        for participant in all_participants:
                            dd = participant.status
                            if  not participant.username == None:

                                if participant.username not in all_users_details:
                                    all_users_details.append(participant.username)
                        for x in all_users_details:
                            ss = x
                            if not ss[-3:] == "bot":
                                if not ss[-3:] == "Bot":
                                    console.print(
                                            "[bold green][*] Спарсен {} пользователь[/]"
                                            .format(x)
                                        )
                                    with open("ussers.txt", "a") as f:
                                        f.write(str(f"{x}\n"))

                        await session(LeaveChannelRequest(invite))
                        os.system("cls")

                    except errors.FloodWaitError as e:
                        console.print('[bold red italic]\n\nАкаунт Получил Flood На {e} Секунд[/]'.format(e=e.seconds), justify="center")
                        time.sleep(3)
                        break
            except:pass
                
                #zx = len(open('ussers.txt', 'r').readlines())
                #print(f"    \n\nПарсинг окончен Спарсено {zx} Пользователей")
                #time.sleep(5)
    

                   # if "@" in invite:
                   #     await session(JoinChannelRequest(invite))
                   # else:
                   #     await session(ImportChatInviteRequest(invite))
                #except Exception as err:
                #    console.print(err)
                #    await session.disconnect()
                #    continue
                #else:
                #    break

  #          users = await session.get_participants(link, aggressive=True)
#
  #      console.print(
  #          "[bold green][*] Спарсен {} пользователь[/]"
  #          .format(len(users))
  #      )
#
  #      users = self.chunkify(users, len(self.sessions))
#
  #      link = console.input("[bold red]куда приглашать пользователей> [/]")
#
  #      with console.status("Приглашение...", spinner="dots"):
  #          await asyncio.wait([
  #              self.invite(users_chunk, link, session)
  #              for session, users_chunk in zip(self.sessions, users)
  #          ])
#
