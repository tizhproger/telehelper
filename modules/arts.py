import random
import logging
import utils
from random import randint, choice
logger = logging.getLogger(__name__)


def register(cb):
    cb(ArtsMod())

class ArtsMod:
    """Юникод арты"""
    strings = {'name': 'Arts'}

    async def vjuhcmd(self, message):
        """Используй .vjuh <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('**Нет текста после команды :c**')
            return
        else:
            vjuh = ("<code>.∧＿∧\n"
                    "( ･ω･｡)つ━☆・*。\n"
                    "⊂  ノ    ・゜ .\n"
                    "しーＪ   °。  *´¨)\n"
                    "             .· ´¸.·*´¨) ¸.·*¨)\n"
                    "                     (¸.·´ (¸.·'* ☆\n\n"
                    "Вжух и ты </code>" + f"<code>{text}</code>")
            await message.edit(vjuh, parse_mode='html')


    async def cowsaycmd(self, message):
        """Используй .cowsay <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('**Нет текста после команды :c**')
            return
        else:
            cowsay = ("<code> "
                      f"< {text} >\n"
                      "\n"
                      "     \   ^__^\n"
                      "	     \  (oo)\_______\n"
                      "         (__)\       )\/\n"
                      "             ||----w||\n"
                      "	            ||     ||</code>")
            await message.edit(cowsay, parse_mode='html')


    async def lolcmd(self, message):
        """Используй .lol."""
        lol = ("┏━┓┈┈╭━━━━╮┏━┓┈┈\n"
               "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈\n"
               "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓\n"
               "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃\n"
               "┗━━━┛╰━━━━╯┗━━━┛\n")
        await message.edit(lol)


    async def fuckyoucmd(self, message):
        """Используй .fuckyou."""
        fuckyou = ("┏━┳┳┳━┳┳┓\n"
                   "┃━┫┃┃┏┫━┫┏┓\n"
                   "┃┏┫┃┃┗┫┃┃┃┃\n"
                   "┗┛┗━┻━┻┻┛┃┃\n"
                   "┏┳┳━┳┳┳┓┏┫┣┳┓\n"
                   "┣┓┃┃┃┃┣┫┃┏┻┻┫\n"
                   "┃┃┃┃┃┃┃┃┣┻┫┃┃\n"
                   "┗━┻━┻━┻┛┗━━━┛\n")
        await message.edit(fuckyou)


    async def hellocmd(self, message):
        """Используй .hello."""
        hello = ("┈┏┓┏┳━┳┓┏┓┏━━┓┈\n"
                 "┈┃┃┃┃┏┛┃┃┃┃┏┓┃┈\n"
                 "┈┃┗┛┃┗┓┃┃┃┃┃┃┃┈\n"
                 "┈┃┏┓┃┏┛┃┃┃┃┃┃┃┈\n"
                 "┈┃┃┃┃┗┓┗┫┗┫╰╯┃┈\n"
                 "┈┗┛┗┻━┻━┻━┻━━┛┈\n")
        await message.edit(hello)


    async def coffeecmd(self, message):
        """Используй .coffee <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Это тебе :з")
            coffee = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffee, parse_mode='html')
        else:
            coffee = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffee, parse_mode='html')


    async def bruhcmd(self, message):
        """Используй .bruh."""
        bruh = ("╭━━╮╱╱╱╱╱╭╮\n"
                "┃╭╮┃╱╱╱╱╱┃┃\n"
                "┃╰╯╰┳━┳╮╭┫╰━╮\n"
                "┃╭━╮┃╭┫┃┃┃╭╮┃\n"
                "┃╰━╯┃┃┃╰╯┃┃┃┃\n"
                "╰━━━┻╯╰━━┻╯╰╯\n")
        await message.edit(bruh)


    async def unocmd(self, message):
        """Используй .uno."""
        uno = ("⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇")
        await message.edit(uno)


    async def impscmd(self, message):
        """Используй .imps <@ или реплай>."""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        if not args and not reply:
            user = await message.client.get_me()
        if reply:
            user = await utils.get_user(await message.get_reply_message())
        if args:
            user = await message.client.get_entity(args)
        imps = ['wasn`t the impostor', 'was the impostor']
        imp = ("<code>.      　。　　　　•　    　ﾟ　　.      .     。\n"
               "　　.　　　.　　　  .　　　.　　　　　。　　   。　   .\n"
               "　.　　      。        ඞ   。　    .     　.　      •      .\n"
               f"•     {user.first_name} {choice(imps)} 。　   .\n"
               f"　 。     {randint(1, 5)} impostor(s) remains.　　　.　 　.\n"
               ",　　　　.　 .　　       .        •   •    。.\n"
               "。  •　   .   　ﾟ 　  •  　ﾟ .        .    　.</code>")
        await message.edit(imp, parse_mode='html')


    async def fcmd(self, message):
        """Используй .f"""
        r = random.randint(0, 6)
        logger.debug(r)
        if r == 0:
            await utils.answer(message, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await utils.answer(message, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        elif r == 2:
            await utils.answer(message,
                               "̫͍F̥̼F͈̫F͔̱F͓̤F̭̺F̙F͍͕F͚̩F̣̱F͖ͅF̣͙F̗͕F̦͚F̯͍ ̘͇F̰̹F̦̩F͙ͅF̙̹F̝͚ ̻F̥̙F ͙̹ ̩͔ ̘͈ ͍̭\n"
                               "̹̖F̲͔F̜ ̗͎F̭̰F̰̭F̼͍F̹̞F̱͉F͓͓F̬ ̼ͅF̤͔F̦͉Fм̟̙F̦̹F͚̠FF̪̝ ̩̗F͇͓F̟̙F͎͎F͉͚ ̥̟ ̙͚\n"
                               "̯̻F͓͈F̮͔F͉̫F͕̥ ͔̙ ̣ ͙г\n"
                               "̞̖F̝̗F͙͓F̟͓F̖̝ ̤͙\n"
                               "͔͓F̠F̖ͅF̰̹F ̠̟\n"
                               "͓͕F̹͙ ̲̩F̙̠F͇̯F̖̗ ̺ ̱͔ \n"
                               "̜͚F ̱̥F̥̝F̖̦F͇͔ ̜͓ ̪̹\n"
                               "̩̗F̬̟F̰F̙͇F F͉̖F̼ͅF̬͔F͇͖F̞̥F̙̺F̖̮ ̥̙F̜͔F̩̜F͎̣F̲̤F̪̙FF̰̫F̝̘ ̣̻F͙͎ ̜̱ ̠͈F̬̫ ̦̩ \n"
                               "͎͙F̘F͍̲ ̲ͅF͇͇F̜̥F͖͖F̪̟ ̤̩F̠̩F̬͕F̪ ̰̪F̫͍ ̺͓F͕̤F̰ͅ ̬̼F̮̼F ͎̯F͓̟F̻͔F̪F͈̭ ̠͓F̣̺ ̭F̮̩ ͖̣\n"
                               "̙F͎̞F̻ F͖͔F͕̮F̯͖FF̪͕F̫͚F̣̣ ̗̣F̩ ̫͍F̥F̗̮F̻̫F͍̺F̞͉F͚̩F͕̤ ͉̤FF̼͙ ͔͕ ͉ ͙\n"
                               "͍͙ F̯̬F̲̻F̥̟F̝̙ ̘\n"
                               "̦̝ ͔ ̝̬F̝͍F̖͚ F̥͚F̖͉ ̩͔ \n"
                               "͓̪F̝͉F̜ͅF̦ͅF͓͕ ̜̭\n"
                               "͖F ͎̩F̩͕F̻͖F̯̼ ̼̼ ̹͔\n"
                               "͍̱FF̹̥F̭͓F̦̺ ̖͎\n"
                               "̥̜F̞͎F̖̲F̦̹F̬̘ \n"
                               "̦̬F̺̭F͖̗F͕͍F̟͙ ͓͍")
        elif r == 3:
            await utils.answer(message, "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕")
        elif r == 4:
            await utils.answer(message, "┏━━━┓╋╋╋╋╋╋╋╋╋╋╋┏━━━┓\n"
                                        "┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋┃┏━━┛\n"
                                        "┃┗━┛┣━┳━━┳━━┳━━┓┃┗━━┓\n"
                                        "┃┏━━┫┏┫┃━┫━━┫━━┫┃┏━━┛\n"
                                        "┃┃╋╋┃┃┃┃━╋━━┣━━┃┃┃\n"
                                        "┗┛╋╋┗┛┗━━┻━━┻━━┛┗┛")
        elif r == 5:
            await utils.answer(message, "`FFFFFFFFFFFFFFFFFFFFFF\n"
                                        "F::::::::::::::::::::F\n"
                                        "F::::::::::::::::::::F\n"
                                        "FF::::::FFFFFFFFF::::F\n"
                                        "  F:::::F       FFFFFF\n"
                                        "  F:::::F\n"
                                        "  F::::::FFFFFFFFFF\n"
                                        "  F:::::::::::::::F\n"
                                        "  F:::::::::::::::F\n"
                                        "  F::::::FFFFFFFFFF\n"
                                        "  F:::::F\n"
                                        "  F:::::F\n"
                                        "FF:::::::FF\n"
                                        "F::::::::FF\n"
                                        "F::::::::FF\n"
                                        "FFFFFFFFFFF`")
        else:
            await utils.answer(message, "██████╗\n"
                                        "██╔═══╝\n"
                                        "████╗░░\n"
                                        "██╔═╝░░\n"
                                        "██║░░░░\n"
                                        "╚═╝░░░░")