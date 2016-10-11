#-*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw 

def genErrImg(text="No further info"):
    img = Image.open("dynimg/static/dynimg/img/Error.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("dynimg/static/dynimg/font/ubuntu.ttf", 15)
    draw.text((0, 235), "Err: " + text, (20, 20, 20), font=font)
    img.save("dynimg/static/dynimg/img/" + text + '.png')
