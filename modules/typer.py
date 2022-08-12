#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import utils

from telethon.errors.rpcerrorlist import MessageNotModifiedError

import asyncio


class TyperMod:
    """Makes your messages type slower"""
    def config_dict(self, *entries):
        keys = []
        values = []
        defaults = []
        docstrings = []
        for i, entry in enumerate(entries):
            if i % 3 == 0:
                keys.append(entry)
            elif i % 3 == 1:
                values.append(entry)
                defaults.append(entry)
            else:
                docstrings.append(entry)

        return dict(zip(keys, values))
        
    def __init__(self):
        self.config = self.config_dict("TYPE_CHAR", "_", lambda m: self.strings["type_char_cfg_doc"],
                                          "DELAY_TYPER", 0.04, lambda m: self.strings["delay_typer_cfg_doc"],
                                          "DELAY_TEXT", 0.02, lambda m: self.strings["delay_text_cfg_doc"])
        self.strings = {"name": "Typewriter",
               "no_message": "**You can't type nothing!**",
               "type_char_cfg_doc": "Character for typewriter",
               "delay_typer_cfg_doc": "How long to delay showing the typewriter character",
               "delay_text_cfg_doc": "How long to delay showing the text"}

    async def typecmd(self, message):
        """.type <message>"""
        a = utils.get_args_raw(message)
        if not a:
            await utils.answer(message, self.strings["no_message"])
            return
        m = ""
        entities = message.entities or []
        for c in a:
            m += self.config["TYPE_CHAR"]
            message = await update_message(message, m, entities)
            await asyncio.sleep(0.04)
            m = m[:-1] + c
            message = await update_message(message, m, entities)
            await asyncio.sleep(0.02)


async def update_message(message, m, entities):
    try:
        return await utils.answer(message, m, parse_mode=lambda t: (t, entities))
    except MessageNotModifiedError:
        return message  # space doesnt count