# 判断类型
a = 1
b = 'hello'
class Student():
    pass
c = Student()
d = True



print(type(a))                         # <class 'int'>
print(isinstance(1,int))               #True
print(isinstance(c,Student))
print(type(c))
# 学过类后对这两个函数更加理解。type()返回的是类型,isinstance判断第一个参数是不是第二个参数实例。

# 2 @property装饰器，语法糖  getter setter函数，具体见2私有属性一节。

# 3 dir()  列出一个类中的所有方法，返回列表。
class Men():
    def __init__(self, name, race, country):
        self.name = name
        self.race = race
        self.country = country
    def run(self):
        print('人在跑')
print(dir(Men))


# 4形如 __xxx__这些名字的函数都与偶特殊用途。
# __class__  可以获取到类自己  __doc__文档  __reper__  __str__类名信息


# 5 slot  插槽
# 由于python是动态语言，类在运行的时候可能会被攻击者添加、删除新的属性，存放恶意信息，导致安全问题. 所以__slots__ = （属性1，属性2，...）确定了类中可以有多少属性，配置中未列出的，在程序运行时，往类中添加新属性就会报错，如果新添加的属性不在__slots定义当中，就会报错。从而确保类属性不能被随意修改，确保安全。
class Stundent():
    __slots__ = ('name','score')
    def __init__(self,name,score):
        self.name = name
        self.score = score

xiaoming = Student('小明',59)
xiaoming.score = 80
xiaoming.score1 = 'eval("python xx.py")'
print(xiaoming.score1)

# 6多重继承
#  一个子类具备多个父类的特征
class Animal(object):
    pass
class Cartoon(object):
    pass
class Dog(Animal):
    pass
class HelloKitty(Animal,Cartoon):               #逗号分割多个父类，有几个写几个。
    pass


# 7 枚举类
# Enum
#  8 基类
#  基类是生成普通类的类，它是普通类的爸爸。

#  9 软件设计模式https://www.cnblogs.com/microsoft-zyl/p/6279176.html

# 工厂模式、单例模式
# 面试题：什么是单例模式？用Python实现一个单例模式。
# 什么是单例模式？用python实现一个单例模式类。
# http://www.runoob.com/design-pattern/design-pattern-intro.html
# https://www.cnblogs.com/Liqiongyu/p/5916710.html