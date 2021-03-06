# 抛异常
# 引题：
# 例2 比如电商公司发快递，路上出现突发的龙卷风，然后快递上天了找不到，最后客户投诉。客服人员将这个之前从未有过的状况报告公司。
# 例4 公司里出现一个问题，基层员工没有权利决定，他就叫来了部门经理，部门经理也没有解决，就上报更上一级的领导。
# 例5 一个代码项目比较大，几十个模块但比较相似，如果用户表单输入错误 需要补货异常打印信息。但每个模块都写提示信息的话重复累。可以抛异常给上层函数，最终由专门的异常处理函数打印信息。

# 所以，代码中遇到问题有时主动抛出异常，交给上层函数处理。遇到新问题需要自定义异常。错误可控，有点小问题就可以主动抛异常 终止程序运行。
class DivisionError(ValueError):    # 自定义异常类
    pass

def foo(num):
    if num == 0:
        # raise Exception
        # raise ValueError('除数不能为0')
        # raise ZeroDivisionError('除数不能为0')
        raise DivisionError('除数不能为0')
    # print(10/num)
foo(1)
foo(2)
foo(0)

# 自定义异常信息，中文或跟项目相关信息。  raise ValueError('除数不能为0')
# 可以自定义异常类，自定义类可以继承系统内置异常类。
# 错误类的父子关系   Exception → ArithmeticError → ZeroDivisionError
# 抛异常好处：自定义；把问题集中处理。