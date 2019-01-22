while True:
    n = int(input('请输入一个数：'))
    if n > 1:
        for i in range(2,n):
            if n % i ==0:
                print('不是质数')
                break
        else:
            print('是质数')

for num in range (1,100):
    total = 0
    for i in range(1,num+1):
        if num % i == 0:
            total = total+1
    if total == 2:
        print(num,'质数')
    elif total > 2:
        print(num ,'不是质数')




