#私有属性

#1引题
class Student():
    def __init__(self,name,score,sex):
        self.name = name
        self.score = score
        self.sex = sex

    def print_score(self):
        print('{}的成绩是{}'.format(self.name,self.score))
    def print_sex(self):
        print('{}的性别是{}'.format(self.name,self.sex))
#实例化
stu_1 = Student('小明',90,'男')
stu_2 = Student('小红',100,'女')

#调用对象属性    对象.属性
print(stu_1.name)
print(stu_1.score)
print(stu_1.sex)
# 写属性
stu_1.score = 100
print(stu_1.score)

#上面的例子说明类的属性可以读也可以被修改，但是这样会导致安全问题，比如小明修改成绩。类内部保密只需要暴露跟外部通信的接口。外部不应该直接修改类的属性。

#2.私有变量
class Student2():
    def __init__(self,name,score,sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password = password

stu1 = Student2('小明',90,'男','12345')
# print(stu1.__password)

#双下划线开头的属性不能被直接访问，也不能被修改,从而确保安全性。
# 但是有的时候又想获取对象的信息。

#3.getter函数
class Student3():
    def __init__(self,name,score,sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password = password
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if score < 0 or score > 100:
            raise ValueError('分数输入错误！')
        self.__score = score

stu1 = Student3('小明',90,'男','12345')
print(stu1.get_score())
stu1.set_score(100)
print(stu1.get_score())

# stu1.score = 100 #私有属性不能直接被修改

# print(stu_1.get_score())     Java中每个属性都有getter setter 方法。
# getter和setter函数可以提供更精细的控制



# 4.property属性装饰器
# 因为上面的getter setter函数写起来比较麻烦，所以Python提供了属性装饰器。
class Student4():
    def __init__(self,name,score,sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password = password
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        if score < 0 or score > 100:
            raise ValueError('分数输入错误！')
        self.__score = score

stu1 = Student4('小明',90,'男','12345')