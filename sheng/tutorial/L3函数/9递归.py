## 递归
##计算10的阶乘
#非递归写法
# a = 1
# for i in range(1,11):
#    a = a * i
# print(a)

#换一种思路
# 例如要计算5！
# 5！ = （1*2*3*4）*5 = 4！*5
# 4！ = （1*2*3）*4 = 3！*4
# 3！ = （1*2）*3 = 2！*3
# 2！ =  1！* 2
# 所以 5！ = （（（1！* 2）*3）*4）*5
# n! = (n-1)! * n  (n>=2)
# 结论：f(n) =  f(n-1) * n  （n>=2）

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

a = factorial(5)
print(a)
# f(1)

# 分析：当factorial（5）开始调用时
# 第一次函数返回值 f(4)*5
# 第二次函数返回值 (f(3)*4)*5
# 第三次函数返回值 ((f(2)*3)*4)*5
# 第四次函数返回值 (((f(1)*2)*3)*4)*5
# 第五次函数返回值 (((1*2)*3)*4) * 5

# 递归深度：递归需要函数调用自身，调用一次递归函数实际会调用多次函数，每调用一次成为深度+1，每调用一次函数，都会增加系统内存的开支，所以Python解释器规定了最大的深度998.