student_list = ['小王', '小红', '小李']
while True:
    print("""
    1-查询学员姓名
    2-添加学员姓名
    3-修改学员姓名
    4-删除学员姓名
    0-退出程序
    """ )
    a = int(input('请选择操作:'))
    if a == 1:
        print('行号\t\t姓名')
        print('-----------------')
        for i in range(0,len(student_list)):
            print(i+1,'\t\t',student_list[i])
    elif a == 2:
        student_list.append(input('请输入要添加的新姓名:'))
        print('添加完毕！')
    elif a == 3:
        b = int(input('要修改第几个学生？'))
        c = input('修改后的姓名是：')
        student_list[b-1] = c
        print('修改成功！')
    elif a == 4:
        #删除
        print(""" 删除> 请输入子操作编号:
                    1) 按学生编号删除
                    2) 删除全部学生（谨慎）
        """)
        sub_num = int(input('请选择子操作：'))
        if sub_num == 1:
            d = int(input('要删除第几个学生？'))
            student_list.pop(d - 1)
            print('删除成功！')
        elif sub_num == 2:
            confirm = input('确认删除全部?(Y/N)')
            if confirm == 'Y' or confirm == 'y':
                student_list.clear()
                print('删除全部成功！')
            elif confirm == 'N' or confirm =='n':
                print('取消删除全部')
            else:
                print('输入错误!')
    elif a == 0:
        print('谢谢使用！')
        break
    else:
        print('输入错误，请重新输入！')
