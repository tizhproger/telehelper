# -*- coding: utf-8 -*-

# Module author: @ftgmodulesbyfl1yd, @dekftgmodules, @memeframe
import io
from os import remove

from telethon.errors import MessageTooLongError
from telethon.tl.functions.messages import GetCommonChatsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)

import utils


class ChatMod:
    """Чат модуль"""

    strings = {"name": "Chat Tools"}

    async def useridcmd(self, message):
        """Команда .userid <@ или реплай> показывает ID выбранного пользователя."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        try:
            if args:
                user = await message.client.get_entity(int(args) if args.isdigit() else args)
            else:
                user = await message.client.get_entity(reply.sender_id)
        except ValueError:
            user = await message.client.get_entity(message.sender_id)

        await message.edit(
            f"<b>Имя:</b> <code>{user.first_name}</code>\n"
            f"<b>ID:</b> <code>{user.id}</code>",
            parse_mode='html'
        )

    async def chatidcmd(self, message):
        """Команда .chatid показывает ID чата."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")
        args = utils.get_args_raw(message)
        to_chat = None

        try:
            if args:
                to_chat = int(args) if args.isdigit() else args
            else:
                to_chat = message.chat_id

        except ValueError:
            to_chat = message.chat_id

        chat = await message.client.get_entity(to_chat)

        await message.edit(
            f"<b>Название:</b> <code>{chat.title}</code>\n"
            f"<b>ID</b>: <code>{chat.id}</code>",
            parse_mode='html'
        )

    async def userscmd(self, message):
        """Команда .users <имя>; ничего выводит список всех пользователей в чате."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>", parse_mode='html')
        await message.edit("<b>Считаем...</b>", parse_mode='html')
        args = utils.get_args_raw(message)
        info = await message.client.get_entity(message.chat_id)
        title = info.title or "этом чате"

        if args:
            users = await message.client.get_participants(
                message.chat_id, search=f"{args}"
            )
            mentions = f'<b>В чате "{title}" найдено {len(users)} пользователей с именем {args}:</b> \n'

        else:
            users = await message.client.get_participants(message.chat_id)
            mentions = f'<b>Пользователей в "{title}": {len(users)}</b> \n'
        for user in users:
            if user.deleted:
                mentions += f"\n• Удалённый аккаунт <b>|</b> <code>{user.id}</code>"

            else:
                mentions += f'\n• <a href ="tg://user?id={user.id}">{user.first_name}</a> | <code>{user.id}</code>'
        try:
            await message.edit(mentions, parse_mode='html')
        except MessageTooLongError:
            await message.edit(
                "<b>Черт, слишком большой чат. Загружаю список пользователей в файл...</b>"
            )
            with open("userslist.md", "w+") as file:
                file.write(mentions)
            await message.client.send_file(
                message.chat_id,
                "userslist.md",
                caption=f"<b>Пользователей в {title}:</b>",
                reply_to=message.id,
                parse_mode='html'
            )

            remove("userslist.md")
            await message.delete()

    async def adminscmd(self, message):
        """Команда .admins показывает список всех админов в чате."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>", parse_mode='html')
        await message.edit("<b>Считаем...</b>", parse_mode='html')
        info = await message.client.get_entity(message.chat_id)
        title = info.title or "this chat"

        admins = await message.client.get_participants(
            message.chat_id, filter=ChannelParticipantsAdmins
        )
        mentions = f'<b>Админов в "{title}": {len(admins)}</b>\n'

        for user in admins:
            admin = admins[
                admins.index((await message.client.get_entity(user.id)))
            ].participant
            if admin:
                rank = admin.rank or "admin"

            else:
                rank = (
                    "creator" if type(admin) == ChannelParticipantCreator else "admin"
                )
            if user.deleted:
                mentions += f"\n• Удалённый аккаунт <b>|</b> <code>{user.id}</code>"

            else:
                mentions += f'\n• <a href="tg://user?id={user.id}">{user.first_name}</a> | {rank} | <code>{user.id}</code>'
        try:
            await message.edit(mentions, parse_mode='html')
        except MessageTooLongError:
            await message.edit(
                "Черт, слишком много админов здесь. Загружаю список админов в файл..."
            )
            with open("adminlist.md", "w+") as file:
                file.write(mentions)
            await message.client.send_file(
                message.chat_id,
                "adminlist.md",
                caption=f'<b>Админов в "{title}":<b>',
                reply_to=message.id,
                parse_mode='html'
            )

            remove("adminlist.md")
            await message.delete()

    async def botscmd(self, message):
        """Команда .bots показывает список всех ботов в чате."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>", parse_mode='html')
        await message.edit("<b>Считаем...</b>", parse_mode='html')

        info = await message.client.get_entity(message.chat_id)
        title = info.title or "this chat"

        bots = await message.client.get_participants(
            message.to_id, filter=ChannelParticipantsBots
        )
        mentions = f'<b>Ботов в "{title}": {len(bots)}</b>\n'

        for user in bots:
            mentions += (
                f"\n• Удалённый бот <b>|</b> <code>{user.id}</code> "
                if user.deleted
                else f'\n• <a href="tg://user?id={user.id}">{user.first_name}</a> | <code>{user.id}</code>'
            )

        try:
            await message.edit(mentions, parse_mode="html")
        except MessageTooLongError:
            await message.edit(
                "Черт, слишком много ботов здесь. Загружаю " "список ботов в файл..."
            )
            with open("botlist.md", "w+") as file:
                file.write(mentions)
            await message.client.send_file(
                message.chat_id,
                "botlist.md",
                caption=f'<b>Ботов в "{title}":</b>',
                reply_to=message.id,
                parse_mode='html'
            )

            remove("botlist.md")
            await message.delete()

    async def commoncmd(self, message):
        """Используй .common <@ или реплай>, чтобы узнать общие чаты с
        пользователем."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args and not reply:
            return await message.edit("<b>Нет аргументов или реплая.</b>", parse_mode='html')
        await message.edit("<b>Считаем...</b>", parse_mode='html')
        try:
            if args:
                if args.isnumeric():
                    user = int(args)
                    user = await message.client.get_entity(user)
                else:
                    user = await message.client.get_entity(args)
            else:
                user = await utils.get_user(reply)
        except ValueError:
            return await message.edit("<b>Не удалось найти пользователя.</b>", parse_mode='html')
        msg = f"<b>Общие чаты с {user.first_name}:</b>\n"
        user = await message.client(GetFullUserRequest(user.id))
        comm = await message.client(
            GetCommonChatsRequest(user_id=user.user.id, max_id=0, limit=100)
        )
        count = 0
        m = ""
        for chat in comm.chats:
            m += f'\n• <a href="tg://resolve?domain={chat.username}">{chat.title}</a> <b>|</b> <code>{chat.id}</code> '
            count += 1
        msg = f"<b>Общие чаты с {user.user.first_name}: {count}</b>\n"
        await message.edit(f"{msg} {m}", parse_mode='html')

    async def chatdumpcmd(self, message):
        """.chatdump <n> <m> <s>
        Дамп юзеров чата
        <n> - Получить только пользователей с открытыми номерами
        <m> - Отправить дамп в избранное
        <s> - Тихий дамп
        """
        if not message.chat:
            await message.edit("<b>Это не чат</b>", parse_mode='html')
            return
        chat = message.chat
        num = False
        silent = False
        tome = False
        if utils.get_args_raw(message):
            a = utils.get_args_raw(message)
            if "n" in a:
                num = True
            if "s" in a:
                silent = True
            if "m" in a:
                tome = True
        if not silent:
            await message.edit("🖤Дампим чат...🖤")
        else:
            await message.delete()
        f = io.BytesIO()
        f.name = f"Dump by {chat.id}.csv"
        f.write("FNAME;LNAME;USER;ID;NUMBER\n".encode())
        me = await message.client.get_me()
        for i in await message.client.get_participants(message.to_id):
            if i.id == me.id:
                continue
            if num and i.phone or not num:
                f.write(
                    f"{str(i.first_name)};{str(i.last_name)};{str(i.username)};{str(i.id)};{str(i.phone)}\n".encode()
                )
        f.seek(0)
        if tome:
            await message.client.send_file("me", f, caption="Дамп чата " + str(chat.id))
        else:
            await message.client.send_file(
                message.to_id, f, caption=f"Дамп чата {str(chat.id)}"
            )

        if not silent:
            if tome:
                if num:
                    await message.edit("🖤Дамп юзеров чата сохранён в " "избранных!🖤")
                else:
                    await message.edit(
                        "🖤Дамп юзеров чата с открытыми "
                        "номерами сохранён в избранных!🖤"
                    )
            else:
                await message.delete()
        f.close()