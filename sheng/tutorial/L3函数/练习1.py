# a=0
# b=1
# while b < 100:
#     print(b)
#     a,b=b,a+b


print('1、','1、',end='')
a = 1
b = 1
for i in range(3,10) :
    c= a + b
    print(c,'、',end = '')
    a = b
    b = c
print(c)

