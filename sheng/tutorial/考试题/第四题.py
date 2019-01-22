year = int(input('请输入年份：'))
if year % 4 == 0:
    print('闰年')
else:
    print('不是闰年')


# n % 4 == 0 and not n%100==0 or n %400==0