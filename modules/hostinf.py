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

import logging
import platform
import asyncio
import shutil
import sys

import telethon

import utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(InfoMod())


class InfoMod:
    """Provides system information about the computer hosting this bot"""
    strings = {"name": "System Info",
               "info_title": "**System Info**",
               "kernel": "**Kernel:** `{}`",
               "arch": "**Arch:** `{}`",
               "os": "**OS:** `{}`",
               "distro": "**Linux Distribution:** `{}`",
               "android_sdk": "**Android SDK:**`{}`",
               "android_ver": "**Android Version:** `{}`",
               "android_patch": "**Android Security Patch:** `{}`",
               "unknown_distro": "**Could not determine Linux distribution.**",
               "python_version": "**Python version:** `{}`",
               "telethon_version": "**Telethon version:** `{}`"}

    def __init__(self):
        self.name = self.strings["name"]

    async def infocmd(self, message):
        """Shows system information"""
        reply = self.strings["info_title"]
        reply += "\n" + self.strings["kernel"].format(utils.escape_html(platform.release()))
        reply += "\n" + self.strings["arch"].format(utils.escape_html(platform.architecture()[0]))
        reply += "\n" + self.strings["os"].format(utils.escape_html(platform.system()))

        if platform.system() == "Linux":
            done = False
            try:
                a = open("/etc/os-release").readlines()
                b = {}
                for line in a:
                    b[line.split("=")[0]] = line.split("=")[1].strip().strip("\"")
                reply += "\n" + self.strings["distro"].format(utils.escape_html(b["PRETTY_NAME"]))
                done = True
            except FileNotFoundError:
                getprop = shutil.which("getprop")
                if getprop is not None:
                    sdk = await asyncio.create_subprocess_exec(getprop, "ro.build.version.sdk",
                                                               stdout=asyncio.subprocess.PIPE)
                    ver = await asyncio.create_subprocess_exec(getprop, "ro.build.version.release",
                                                               stdout=asyncio.subprocess.PIPE)
                    sec = await asyncio.create_subprocess_exec(getprop, "ro.build.version.security_patch",
                                                               stdout=asyncio.subprocess.PIPE)
                    sdks, unused = await sdk.communicate()
                    vers, unused = await ver.communicate()
                    secs, unused = await sec.communicate()
                    if sdk.returncode == 0 and ver.returncode == 0 and sec.returncode == 0:
                        reply += "\n" + self.strings["android_sdk"].format(sdks.decode("utf-8").strip())
                        reply += "\n" + self.strings["android_ver"].format(vers.decode("utf-8").strip())
                        reply += "\n" + self.strings["android_patch"].format(secs.decode("utf-8").strip())
                        done = True
            if not done:
                reply += "\n" + self.strings["unknown_distro"]
        reply += "\n" + self.strings["python_version"].format(utils.escape_html(sys.version))
        reply += "\n" + self.strings["telethon_version"].format(utils.escape_html(telethon.__version__))
        await utils.answer(message, reply)
