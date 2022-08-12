import io, requests
import utils
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

class TextOnPhotoMod:
    strings = {'name': 'TextOnPhoto'}

    async def bottomcmd(self, message):
        """Используй: .bottom <реплай на картинку/стикер> <white/black>;ничего <текст>."""
        return await procces_img(message, 1)

    async def topcmd(self, message):
        """Используй: .top <реплай на картинку/стикер> <white/black>;ничего <текст>."""
        return await procces_img(message, 2)

    async def centercmd(self, message):
        """Используй: .center <реплай на картинку/стикер> <white/black>;ничего <текст>."""
        return await procces_img(message, 3)

async def procces_img(message, way):
    cols = {'white': 1, 'whit': 1, 'whi': 1, 'wh': 1, 'w': 1,
            'black': 2, 'blac': 2, 'bla': 2, 'bl': 2, 'b': 2}
    col = 1
    reply = await message.get_reply_message()
    txt = utils.get_args_raw(message)
    await message.edit("подождем...")
    
    if txt in cols:
        col = cols[txt]
        txt = None
    if not txt:
        txt = "я лошара."
    if not reply:
        await message.edit("нет реплая на картинку/стикер.")
        return
    if txt.split(" ")[0] in cols:
        col = cols[txt.split(" ")[0]]
        txt = " ".join(txt.split(" ")[1:])
    
    bytes_font = requests.get("https://github.com/Fl1yd/FTG-modules/blob/master/stuff/font3.ttf?raw=true").content
    bytes_back = await reply.download_media(bytes)
    font = io.BytesIO(bytes_font)
    font = ImageFont.truetype(font, 72)
    img = Image.open(io.BytesIO(bytes_back))
    
    W, H = img.size
    txt = txt.replace("\n", "𓃐")
    text = "\n".join(wrap(txt, 30))
    t = text
    t = t.replace("𓃐", "\n")
    
    draw = ImageDraw.Draw(img)
    w, h = draw.multiline_textsize(t, font=font)
    imtext = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(imtext)
    
    if col == 2:
        draw.multiline_text((10, 10), t, (0, 0, 0), font=font, align='center')
    else:
        draw.multiline_text((10, 10), t, (255, 255, 255), font=font, align='center')
    imtext.thumbnail((W, H))
    w, h = imtext.size
    
    if way == 1:
        img.paste(imtext, ((W - w) // 2, (H - h) // 1), imtext)
    if way == 2:
        img.paste(imtext, ((W - w) // 2, (H - h) // 15), imtext)
    if way == 3:
        img.paste(imtext, ((W - w) // 2, (H - h) // 2), imtext)
    
    output = io.BytesIO()
    output.name = "result.png"
    img.save(output, "png")
    output.seek(0)
    await message.client.send_file(message.to_id, output, reply_to=reply)
    await message.delete()