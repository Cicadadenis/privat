from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os, time
from telethon.tl.types import PeerChannel, InputPeerChannel, GroupCall
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from rich.console import Console
from telethon import errors
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
def inv():
    console = Console()

    api_hash = "b826075fd7ea762e6b9f853146d47995"
    api_id = 1325339
    def logo():
        console.print("[blink blue]      _             __         ___       __[/]", justify="center")
        console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
        console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
        console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
        console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
        time.sleep(2)
    os.system("cls")
    logo()
    link = console.input("[bold green italic]\n\nСсылка на чат:  [/]")
    paus = int(console.input("[bold green italic]Пауза:  [/]"))
    users = open("ussers.txt", 'r').readlines()
    print(int(len(users)))
    xxc = int(len(users)/100)
    print(xxc)
    xxxc = int(len(users)/100)
    for file in os.listdir(f"sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
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

            try:
                fr = session(JoinChannelRequest(link))

                for target_group in fr.chats:
                
                    target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)


                
                for user in users:

                    try:
                        user_to_add = session.get_input_entity(user)
                        sq = session(InviteToChannelRequest(target_group_entity,[user_to_add]))
                        os.system("cls")
                        logo()
                        console.print("[bold green italic]\n\nВыполненно {xxc}%[/]".format(xxc=xxc), justify="center")
                        console.print("[bold green italic]\n\nПользователь [/][bold blue italic]{user} [/][bold green italic]Добавлен В [/][bold blue italic]{chat}   [/][bold green italic] Пауза [/][bold blue italic]{paus} с[/][bold green italic]екунд...[/]".format(user=user[:-1], chat=target_group.title, paus=paus))
                        xxc = xxc + xxxc
                        time.sleep(paus)
                    except:
                        pass
            except:
                pass

        #            except:
         #               pass
                    #except PeerFloodError:
                     #   print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    #except UserPrivacyRestrictedError:
                     #   print("The user's privacy settings do not allow you to do this. Skipping.")
                    #except:
                     #   traceback.print_exc()
                      #  print("Unexpected Error")
                       # continue
