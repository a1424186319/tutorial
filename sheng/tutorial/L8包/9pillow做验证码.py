# pillow例子2 随机生成验证码
"""
(了解）RGB：red green blue 色光三原色，(11,225,5)

"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母
def random_char():
    return chr(random.randint(50,90))

def GB2312():
    return chr(random.randint(0x7684, 0x91cc))
# def rotate(a):
#     a = rotate(random.randint(0, 30), expand=0)
def rndRotate():
    return random.randint(-30, 30)


# 随机数字
def random_num():
    return random.randint(0, 9)


# 随机字体颜色 稍深
def random_color():
    return (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))


# 随机背景颜色
def random_color2():
    return (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))


# 生成空白背景图层
image = Image.new('RGB', size=(240, 60), color=(255, 255, 255))
# 生成绘制对象
# image = Image.ovpen('demo.jpg')



draw = ImageDraw.Draw(image)
# 字体对象 ，字体、字号
font = ImageFont.truetype('msyh.ttf',36)



for i in range(0,240):
    draw.point((random.randint(0, 240), random.randint(0, 60)),fill=random_color())

    # 循环像素点并填充颜色
for x in range(0, 240):
    for y in range(0, 60):
        draw.point(xy=(x, y), fill=random_color2())


# 生成文字
for t in range(0, 4):
    a = draw.text((60 * t + 20, random.randint(0, 15)), GB2312(), font = font,fill=random_color())             #2 Y轴随机

# 加模糊滤镜
draw.line((10, 30, 220, 25), fill="red")  # 1 前两个数是开始坐标,后两个数是结束坐标
draw.line((15, 40, 230, 20), fill="blue")
draw.line((8, 25, 210, 35), fill="red")
draw.line((15, 80, 100, 20), fill="blue")


# image = image.filter(ImageFilter.BLUR)



# 保存
image.save('demo4.jpg', 'jpeg')

"""
# 作业：追加需求 （锻炼查资料和自己摸索能力）
1. 在github上搜索关键字“生成验证码”，查看学习别人生成验证码的流程。拷贝一份别人的实现并成功运行。
2. 绘制文字时y坐标更凌乱（百度搜索 “验证码”）
3. 添加干扰斜线或曲线
4. 文字扭曲效果，猜测跟滤镜相关，百度“pillow 滤镜”“PIL 文字 扭曲" "正弦函数变形"
5. 背景干扰点
6. 文字为中文。C:/windows/fonts 文件夹下找找微软雅黑字体。
7. 字体粗细、大小混排。
8. 文字轻度旋转(-30度到30度)
9. 把一张风景图作为验证码的背景。
10. 文字、字母、数字中的两种混排
"""
