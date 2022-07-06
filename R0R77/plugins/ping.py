import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://i2.wp.com/saji0.com/wp-content/uploads/2019/09/36939.jpg?resize=1024%2C576&ssl=1"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@r15x5"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/invietamino")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
