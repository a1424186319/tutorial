# 手机销售系统
phone_list = [{'手机品牌': 'vivoX9', '手机价格': '2798'},
              {'手机品牌': 'mate20', '手机价格': '4000'},
              {'手机品牌': 'iphone', '手机价格': '8000'},
              ]


def show_phone():
    print('序号\t编号\t手机品牌\t手机价格')
    print('---------------------------------')
    for i in range(0, len(phone_list)):
        stu_dict = phone_list[i]
        pinpai = stu_dict['手机品牌']
        jiage = stu_dict['手机价格']
        m = "%03d" % (i + 1)
        print('{}\t\t{}\t\t{}\t\t{}'.format(i + 1, m, pinpai, jiage))


def add_phone():
    phone_dict = {}
    phone_dict['手机品牌'] = input('请输入要添加的新品牌:')
    phone_dict['手机价格'] = input('请输入新品的的价格:')
    phone_list.append(phone_dict)
    print('添加完毕！')


def update_phone():
    show_phone()
    s = int(input('要修改第几个？'))
    change_s = s - 1
    m = input('修改后的手机型号是:')
    n = input('修改后的手机价格是:')
    phone_list[change_s]['手机品牌'] = m
    phone_list[change_s]['手机价格'] = n
    print('修改成功！')


while True:
    print("""
        1-查看所有手机品牌
        2-添加新产品
        3-修改原有产品信息
        4-退出程序
        """)
    a = int(input('请选择操作:'))
    if a == 1:
        show_phone()
    elif a == 2:
        add_phone()
    elif a == 3:
        update_phone()
    elif a == 4:
        print('退出成功，谢谢使用！')
        break
