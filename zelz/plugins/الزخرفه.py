# 𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
# الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙏𝙝𝙤𝙣

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock

from ..core.managers import edit_or_reply
from . import zedub


@zedub.zed_cmd(pattern="زخرفة ?(.*)")
async def zilzal(event):
    card = event.pattern_match.group(1)
    chat = "@ZZ_ARBot"
    await reply_id(event)
    zed = await edit_or_reply(event, "**- ارسـل (.زخرفه) + اسمـك بالانكلـش**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("ZZ_ARBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="زغرفه ?(.*)")
async def zelzal(event):
    card = event.pattern_match.group(1)
    chat = "@Z_ENBot"
    await reply_id(event)
    zed = await edit_or_reply(event, "**- ارسـل (.زخرفه) + اسمـك بالانكلـش**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("Z_ENBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()
