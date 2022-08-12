# -*- coding: utf-8 -*-

import logging
import urllib

import utils

logger = logging.getLogger(__name__)


class LMGTFYMod:
    """Let me Google that for you, coz you too lazy to do that yourself."""

    def __init__(self):
        self.strings = {
            "name": "Япоищузатебя",
            "result": "**Вот, держи**\n[{}]({})",
            "default": "Как юзать Google?",
        }

    async def lmgtfycmd(self, message):
        """Use in reply to another message or as .lmgtfy <text>"""
        text = utils.get_args_raw(message)
        if not text:
            if message.is_reply:
                text = (await message.get_reply_message()).message
            else:
                text = self.strings["default"]
        query_encoded = urllib.parse.quote_plus(text)
        lmgtfy_url = "http://lmgtfy.com/?s=g&iie=1&q={}".format(query_encoded)
        await utils.answer(
            message,
            self.strings["result"].format(
                utils.escape_html(text),
                utils.escape_html(lmgtfy_url)
            ),
        )
