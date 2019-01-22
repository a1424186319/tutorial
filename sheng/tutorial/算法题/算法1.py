#   A有一些石子,A扔掉一颗并把剩余数量的一半给了B,B扔掉一颗并剩余数量的一半给C,C扔掉一颗后剩下4颗,A最初拥有几颗石子?


# A = n
# B = (A-1)/2
# C = (((A-1)/2)-1)/2
# C = 5
#

# A = (C*2+1)*2+1
# B = C*2+1
# C = 5
# f(n)=(n*2+1)*2+1
# f(n) = 4n+3

# f(n-1) = 19     4
# f(n-2) = 15     3
# f(n-3) = 11     2
# f(n-4) = 7      1



# import sys
# sys.setrecursionlimit(1000000)
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 4

print(f(5))
