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
import random


def register(cb):
    cb(YesNoMod())


class YesNoMod:
    """Helps you make important life choices"""
    def __init__(self):
        self.name = "YesNo"

    async def yesnocmd(self, message):
        """Make a life choice"""
        # TODO translate
        yes = ["Да", "Конечно", "Абсолютно", "Вероятно"]
        no = ["Нет", "Неа", "Не", "Такое"]
        if random.getrandbits(1):
            await message.edit(random.choice(yes))
        else:
            await message.edit(random.choice(no))
