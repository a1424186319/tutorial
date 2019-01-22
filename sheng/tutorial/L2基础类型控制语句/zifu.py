str1 = input('请输入一个字符串')
str_sum = 0
dig_sum = 0
spa_sum = 0
other_sum = 0
for i in str1:
    if i.isalpha():
        str_sum += 1
    elif i.isdigit():
        dig_sum += 1
    elif i.isspace():
        spa_sum += 1
    else:
        other_sum += 1
print('字符：%d'%str_sum)
print('数字：%d'%dig_sum)
print('空格：%d'%spa_sum)
print('其它：%d'%other_sum)
# print('字母{}，数字{}，空格{}，其它{}'.format(str_sum,dig_sum,spa_sum,other_sum))