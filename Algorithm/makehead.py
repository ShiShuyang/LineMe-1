# -*- coding: utf-8 -*- 

from PIL import Image,ImageDraw
from PIL import ImageFont
import random

def NameCardImg(username='Shuyang Shi'):
    word = ''.join(map(lambda x: x[0].upper(), username.split(' ')))
    beautifulRGB = ((245, 67, 101),
                    (252, 157, 154),
                    (249, 205, 173),
                    (131, 175, 155),
                    (6, 128, 67),
                    (38, 157, 128),
                    (137, 157, 192))
    font = ImageFont.truetype('simhei.ttf'.decode('utf8'), 250)
    img = Image.new('RGB', (400,400), random.choice(beautifulRGB))
    draw = ImageDraw.Draw(img)
    if len(word) >= 2:
        draw.text( (80,75), word[:2], (255,255,255),font=font)
    if len(word) == 1:
        draw.text( (150,75), word, (255,255,255),font=font)
    img.save(username + '.png')
    return

if __name__ == '__main__':
    NameCardImg('123 fh')
