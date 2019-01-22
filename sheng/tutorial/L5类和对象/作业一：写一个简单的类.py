# 作业一:类知识
# ===
# 1.写一个'人类'的类。
#     1.类有以下属性，
#     -姓名
#     -人种（黄、白、黑）
#     -国家（中、美、韩）
#     -身高（180、160）
#     -体重（70）
#     2.方法功能
#     -打印这个人的基本信息
#     -打印这个人的BMI指数（体重kg/身高m的平方）


class Men():
    def __init__(self, name, race, country, height, weight):
        self.name = name
        self.race = race
        self.country = country
        self.height = height
        self.weight = weight

    def print_information(self):
        print('{}是{}种人,是{}国人,身高是{},体重是{}'.format(self.name, self.race, self.country, self.height, self.weight))

    def print_BMI(self):
        print(self.weight / (self.height / 100 * self.height / 100))


man1 = Men('小明', '黄', '中', 175, 70)
man2 = Men('麦克', '黑', '美', 180, 71)
man3 = Men('杰 西', '白', '韩', 170, 50)

Men.print_information(man1)
Men.print_BMI(man1)