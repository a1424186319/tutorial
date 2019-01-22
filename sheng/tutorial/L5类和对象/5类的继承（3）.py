#继承>重写
#引题1：比如一个计算机系有 电商方向、软件方向，它们的课程70%一样（数学英语C语言），其它30%不一样（电商seo优化、软件方向XX编程框架）。子类跟父类方法部分相同。而上节课的run方式是子类完全重写覆盖掉父类的方法。
#引题2:5类的继承.py一节中的学生、老师类例子用继承方式写出来。
class People(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say_hi(self):
        print('hello')

    def work(self,time):
        if time < 8 :
            print('正常上班')
        elif time > 8 :
            print('加班时间')
class Student(People):
    def __init__(self,name,age,sex):
        # self.name = name
        # self.age = age
        # self.sex = sex
        super()

    def work(self,time):
        print('学生不用工作')

class Teachre(People):
    def __init__(self,name,age,sex,salary,class_number):
        #1>一个一个的写构造函数
        # self.name = name
        # self.age = age
        # self.sex = sex
        #2> 类名.方法名
        #People.__init__(name,age,sex)
        # 3>super()
        # super(Teachre,self).__init__(name, age, sex)
        #4省略参数的super()
        super().__init__(name,age,sex)
        self.salary = salary
        self.class_number = class_number





stu1 = Student('小明',10,'male')
stu1.say_hi()
stu1.work(time=8)
tea1 = Teachre('杨老师',27,'male',10000,314)
tea1.say_hi()

"""
完全重写：子类重写父类方法，完全覆盖原方法内容，像上一节的例子，Cat类的run()方法完全替代了父类Animal类中的run()的内容。
吧
部分重写：子类重写父类方法，继承了父类方法中一部分内容，又有自己个性化的部分。
super():调用父类。重用父类属性或方法，减少了代码量，转为继承设计。子类调用完父类相同之处后，个性化的东西可以另外写。
语法：原始语法super(子类名，子类实例)，省略参数的写法super（）。
优点：方便调用父类中的东西；代码复用；父类名变化时子类不用过多的修改，好维护。
"""





