# █ █ ▀ █▄▀ ▄▀█ █▀█ ▀    ▄▀█ ▀█▀ ▄▀█ █▀▄▀█ ▄▀█
# █▀█ █ █ █ █▀█ █▀▄ █ ▄  █▀█  █  █▀█ █ ▀ █ █▀█
#
#              © Copyright 2022
#
#          https://t.me/hikariatama
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://img.icons8.com/external-flaticons-lineal-color-flat-icons/344/external-anime-addiction-flaticons-lineal-color-flat-icons.png
# meta developer: @hikariatama

import utils  # noqa: F401
from telethon.tl.types import Message  # noqa: F401
import logging
from random import choice

logger = logging.getLogger(__name__)


class AnimatedQuotesMod:
    """Simple module to create animated stickers via bot"""

    def __init__(self, client) -> None:
        self._client = client
        self.strings = {
            "name": "AnimatedQuotes",
            "no_text": "🚫 **Provide a text to create sticker with**",
            "processing": "⏱ **Processing...**",
        }

    async def aniqcmd(self, message: Message) -> None:
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_text"])
            return

        message = await utils.answer(message, self.strings["processing"])
        if isinstance(message, (list, set, tuple)):
            message = message[0]

        try:
            query = await self._client.inline_query("@QuotAfBot", args)
            await message.respond(file=choice(query).document)
        except Exception as e:
            await utils.answer(message, str(e))
            return

        await message.delete()
