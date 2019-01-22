from PIL import Image,ImageDraw,ImageFont
font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf",16)
im = Image.open("E:/表情图/4.jpg")
draw = ImageDraw.Draw(im)
draw.text((30,150),'  我刚才仿佛听见有人喊我\n爸爸,不过他已经撤回了.', fill=(0,0,0),font=font)
im.show()
