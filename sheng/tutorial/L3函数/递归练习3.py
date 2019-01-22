# 斐波那契数列:1,1,2,3,5,8,13,21... →  F(n)=F(n-1)+F(n-2)
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n - 1) +f(n - 2)
for n in range(1,11):
       print(f(n))



