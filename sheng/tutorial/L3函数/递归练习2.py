# 计算1+2+3 ....+99+100
def f(n):
    if  n >= 0:
        return f(n - 1)+n
    else:
        return 0
print(f(100))

# 高斯算法公式n*（1+n）/2

def f(n):
    if n == 1:
        return 1
    return f(n - 1)+n
print(f(100))
