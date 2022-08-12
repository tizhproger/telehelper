import utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


def register(cb):
    cb(NedoQuotesMod())
    
class NedoQuotesMod:
    """Генератор всратых цитат by @ShittyQuoteBot"""
    strings = {'name': 'NedoQuotes'}

    async def nqcmd(self, message):
        """Используй: .nq <текст или реплай>."""
        chat = "@ShittyQuoteBot"
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("**Нет текста или реплая.**")
            return
        await message.edit("**Минуточку...**")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1389323591))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("**Разблокируй @ShittyQuoteBot**")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1389323591))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("**Разблокируй @ShittyQuoteBot**")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<b> {response.text}</b>")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()