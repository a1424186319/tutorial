# PEP8代码风格指导

"""
python官方第八号文件，这个文件说明了Python语言代码应该怎么去书写，指导了书写风格。当你的代码没有做到文件要求的时候，pycharm会报灰线轻度提示。没有完全遵守规则不影响代码执行。但建议遵守。
"""
# 操作符前后应该有一个空格
a = 3
a = 3


#  方法与方法之间有两个空行。
def foo():
    pass


def boo():
    pass

# 类中的方法相隔一行
class Stundent(object):
    def foo(self):
        pass

    def boo(self):
        pass
#类与类之间空两行。
# 如果没有父类不谢括号。
# 类名应该用驼峰风格。
class foo():
    pass
class boo():
    pass

# 方法名、类名不要重复使用。
def boo():
    pass
#两个条件有时可以写成链式的。
if 1<a and a<2:
    pass
if 1 < a < 2:
    pass
# 不建议代码写的过长，79个字符。pycharm的提示灰线在120个字符。  注释不超过72.
# 文件末尾代码结束时，另起一个新行。
print('end')

# https://www.python.org/dev/peps/pep-0008/
# https://blog.csdn.net/ratsniper/article/details/78954852

"""
paycharm有关代码风格操作
1.界面右下角图标点击，调节提示出现的级别（不图示、语法、拼写）。
2.格式化代码。界面左上菜单code/reformat code。
"""