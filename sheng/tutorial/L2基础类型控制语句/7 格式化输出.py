#格式化输出
#简单输出
print('你好小明')
print('hello world')

# 带变量的输出 更有灵活性，易于维护,好处参考excercise 1-3
name='小明'
print(name)

#加号拼接字符串
pay = '8'
print('花费一共'+pay+'元')

#print 里用逗号打印多个变量
# name = '小明'
# score = '90'
# print(name,score)
# print('学生姓名:'+name+',学生成绩'+score+'。')

#变量多的情况,加号拼接字符串比较麻烦，
name = '小明'
score = 90
sex = 'male'
heigeht = 180
weight = 70
address = '郑州市'
phone = '1424186319'

#所以，我们用格式化输出字符串

#方法一： '姓名%s，成绩%s' % (变量1，变量2)
# %s 是占位符，将要被变量填充。
# %s 字符串， %d 整数，%f 浮点数
# C语言写法，并不推荐写法，但很多项目还在用这种写法，要求认识
print('学生姓名%s,成绩%d' % (name,score))

#（重点）方法二：format()
#优点：不用转型，使用自然。
print('学生姓名{},成绩{}'.format(name,score))
#其它不太常用的写法
print('学生姓名{stu_name}，成绩{stu_score}'.format(stu_name='小明',stu_score=90))

#format用法  https://www.cnblogs.com/chunlaipiupiupiu/p/7978669.html

#小数点精度
print('河南省面积{:.2f}'.format(190.5832))
#左对齐，右对齐
print('{:^20}'.format('居中对齐'))
print('{:<20}'.format('左对齐'))
print('{:>20}'.format('右对齐'))


# print()输出后不换行
'1，2'
print('1',end='，')    #光标就不会换行
print('2')


print('学生{},成绩{}'.format(name,score))
print('学生%s,成绩%d'%(name,score))


# 输出编号
for i in range(1,20):
    m = "%03d" % i
    print(m)