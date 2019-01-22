def myday():
    print('起床')
    print('吃早餐')
    print('上班')
    print('下班')
    print('睡觉')
#一个参数的函数
def calculate_area(r):
    print('圆面积',3.14 * r * r)
calculate_area(5)
#多个参数的函数
def get_max(a,b,c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num
get_max(1,5,3)

#函数运行前需要告诉函数一些运行时需要的原料，数值，函数根据传入的参数参与内部的逻辑运算。
#形参：函数定义的时候，占位，将要传进的数值’形式上的代表‘。形参名可变，只关注形参的类型
#实参：函数调用的时候，传入函数的实际具体的数值，注意实参的值要与形参的个数保持一致。
#可能出现的错误：实参和形参个数或类型不一致报错。