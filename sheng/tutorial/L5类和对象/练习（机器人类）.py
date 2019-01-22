# 类变量和静态方法练习
# 一、按要求写一个类。
# 1 定义一个机器人类 Robot
# 2类属性:
#     -name  'XR-01'
# 3类变量 人口 int:population整数类型

# 4 方法，构造函数__init__()  传值  print({}被制造出来了，self.name)；人口+1.
#     方法die()。print({}被销毁了 self.name);人口-1.
#         say_hi()  print(‘大家好’)
#         how_many()  返回人口  静态方法

class Robot():
    population = 0

    def __init__(self, name):
        self.name = name  # 属性，对象变量。
        Robot.population += 1

    def say_hi(self):
        print('大家好，我是{}'.format(self.name))

    @classmethod
    def how_many(cls):
        print('目前总人口', cls.population)

    def die(self):
        Robot.population -= 1


rob1 = Robot('XR-01')
rob1.say_hi()
Robot.how_many()
rob2 = Robot('XR-02')
Robot.how_many()
rob2.die()
Robot.how_many()

