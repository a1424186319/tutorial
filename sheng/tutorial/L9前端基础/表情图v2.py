from PIL import Image,ImageDraw,ImageFont
font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf",30)
im = Image.open("E:/表情图/4.jpg")

draw = ImageDraw.Draw(im)
draw.text((65,150),'且随疾风', fill=(0,0,0),font=font)
im.show()