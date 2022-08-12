import logging
import os
import utils
from telethon.tl.types import Message
from telethon.tl.custom import Message as CustomMessage

logger = logging.getLogger(__name__)
media_chat = os.environ.get('MEDIA_CHAT')


def register(cb):
    cb(NotesMod())


class NotesMod:
    """Stores global notes (aka snips)"""
    strings = {"name": "Notes",
               "what_note": "**What note should be retrieved?**",
               "no_note": "**Note not found**",
               "save_what": "**You must reply to a message to save it to a note, or type the note.**",
               "what_name": "**You must specify what the note should be called?**",
               "saved": "**Note saved**",
               "notes_header": "**Saved notes:**\n\n",
               "notes_item": "**➤** `{}`",
               "delnote_args": "**What note should be deleted?**",
               "delnote_done": "**Note deleted**",
               "delnotes_none": "**There are no notes to be cleared**",
               "delnotes_done": "**All notes cleared**",
               "notes_none": "**There are no saved notes**",
               "error": "**Something wrong...**",
               "already": "**Note already exist**"}
    
    def __init__(self, client, db):
        self._client = client
        self._db = db
        self._assets = None
    

    def config_complete(self):
        self.name = self.strings["name"]
    
    async def find_asset_channel(self):
        async for dialog in self._client.iter_dialogs(None, ignore_migrated=True):
            if dialog.name == f"{media_chat}" and dialog.is_channel:
                members = await self._client.get_participants(dialog, limit=2)
                if len(members) != 1:
                    continue
                logger.debug(f"Found asset chat! It is {dialog.id}.")
                return dialog.entity
    
    async def store_asset(self, message):
        if not self._assets:
            self._assets = await self.find_asset_channel()
        return ((await self._client.send_message(self._assets, message)).id
                if isinstance(message, (Message, CustomMessage)) else
                (await self._client.send_message(self._assets, file=message, force_document=True)).id)

    async def fetch_asset(self, id):
        if not self._assets:
            self._assets = await self.find_asset_channel()
        if not self._assets:
            return None
        ret = (await self._client.get_messages(self._assets, limit=1, max_id=id + 1, min_id=id - 1))
        if not ret:
            return None
        return ret[0]

    async def notecmd(self, message, table):
        """Gets the note specified"""
        args = utils.get_args(message)
        if not args:
            await utils.answer(message, self.strings["what_note"])
            return
        asset_id = self._db.get(args[0], table)
        logger.debug(asset_id)
        if asset_id is None:
            await utils.answer(message, self.strings["no_note"])
            return
        await utils.answer(message, await self.fetch_asset(asset_id))


    async def delallnotescmd(self, message, table):
        """Deletes all the saved notes"""
        if not self._db.get_all(table):
            await utils.answer(message, self.strings["delnotes_none"])
            return
        if self._db.del_all(table):
            await utils.answer(message, self.strings["delnotes_done"])
        else:
            await utils.answer(message, self.strings["error"])


    async def savecmd(self, message, table):
        """Save a new note. Must be used in reply with one parameter (note name)"""
        args = utils.get_args(message)
        if not args:
            await utils.answer(message, self.strings["what_name"])
            return
        if not message.is_reply:
            if len(args) < 2:
                await utils.answer(message, self.strings["save_what"])
                return
            else:
                message.entities = None
                message.message = args[1]
                target = message
                logger.debug(target.message)
        else:
            target = await message.get_reply_message()

        if self._db.noted(args[0], table):
            await utils.answer(message, self.strings["already"])
            return
        asset_id = await self.store_asset(target)
        if self._db.save(args[0], asset_id, table):
            await utils.answer(message, self.strings["saved"] + f" as: `{args[0]}`")
        else:
            await utils.answer(message, self.strings["error"])


    async def delnotecmd(self, message, table):
        """Deletes a note, specified by note name"""
        args = utils.get_args(message)
        if not args:
            await utils.answer(message, self.strings["delnote_args"])
            return
        if not self._db.noted(args[0], table):
            await utils.answer(message, self.strings["no_note"])
            return
        if self._db.deln(args[0], table):
            await utils.answer(message, self.strings["delnote_done"])
        else:
            await utils.answer(message, self.strings["error"])


    async def notescmd(self, message, table):
        """List the saved notes"""
        if not self._db.get_all(table):
            await utils.answer(message, self.strings["notes_none"])
            return
        header = self.strings["notes_header"]
        if table == 'Vault':
            header = "**Vault notes:**\n\n"
        await utils.answer(message, header
                           + "\n".join(self.strings["notes_item"].format(el[0])
                           for el in self._db.get_all(table)).replace(' ', ''))

