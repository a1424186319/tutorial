while True:
    kilometre_number = input('请输入公里数')
    kilometre_number = int(kilometre_number)
    a = 8
    b = 8+1.2*(12-2)
    c = 8+1.2*(12-2)+1.5*(kilometre_number-12)
    if 0 < kilometre_number <= 2:
        print('你的费用为{}元'.format(a))
    elif 2 < kilometre_number <= 12:
        print('你的费用为{}元'.format(b))
    elif kilometre_number > 12:
        print('你的费用为{}元'.format(c))



# #用户输入
# km = input('输入公里数：')
# km = int(km)
# pay = 0  # 花费
# if 0 <= km <= 2:
#     pay = 8
# elif 2 < km <= 12:
#     pay = 8+(km-2)*1.2
# elif km > 12:
#     pay = 8+10*1.2+(km-12)*1.5
# else:
#     print('输入不合法')
# print('你的费用为'+str(pay)+'元')