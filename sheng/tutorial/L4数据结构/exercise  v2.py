student_list = [{'name': '小明', 'age': '10', 'sex': 'male'},
                {'name': '小红', 'age': '12', 'sex': 'female'},
                {'name': '小李', 'age': '12', 'sex': 'male'}
                ]


def show_students():
    """打印学生列表"""
    print('行号\t姓名\t年龄\t性别')
    print('---------------------------------')
    for i in range(0,len(student_list)):
        stu_dict = student_list[i]
        name = stu_dict['name']
        age = stu_dict['age']
        sex = stu_dict['sex']
        print('{:^4}{:^10}{:^4}{:^12}'.format(i+1,name,age,sex))
def add_student():
    """添加学生"""
    student_dict = {}
    student_dict['name'] = input('请输入要添加的新姓名:')
    student_dict['age'] = input('请输入年龄:')
    student_dict['sex'] = input('请输入性别:(male或female)')
    student_list.append(student_dict)
    print('添加完毕！')
    # new_name = input('请输入要添加的学生的新姓名:')
    # new_age = int(input('请输入年龄:'))
    # new_sex = input('请输入要添加的学生的性别:')
    # new_stu_dict = {'name':new_name,'age':new_age,'sex':new_sex}
    # student_list.append(new_stu_dict)
    # print('添加成功')

def update_student():
    """修改学生"""
    show_students()
    # s = int(input('要修改第几个学生:'))
    # change_s = s - 1
    # m = input('修改后的姓名是:')
    # n = input('修改后的年龄是:')
    # x = input('修改后的性别是:(male或female)')
    # student_list[change_s]['name'] = m      ★★★建议这种，不会引发逻辑上的错误★★★
    # student_list[change_s]['age'] = n
    # student_list[change_s]['sex'] = x
    # print('修改成功！')
    num = int(input('要修改第几个学生?:'))
    new_name = input('修改后的姓名是:')
    new_age = int(input('修改后的年龄是:'))
    new_sex = input('修改后的性别是:(male或female)')
    stu_dict =student_list[num - 1]
    stu_dict['name'] = new_name
    stu_dict['age'] = new_age
    stu_dict['sex'] = new_sex
    print(stu_dict)
    print('修改成功！')

def delete_student():
    """删除学生"""
    print(""" 删除> 请输入子操作编号:
                            1) 按学生编号删除
                            2) 删除全部学生（谨慎）
                """)
    sub_num = int(input('请选择子操作：'))
    show_students()
    if sub_num == 1:
        student_list.pop(int(input('要删除第几个学生？')) - 1)
        print('删除成功！')
    elif sub_num == 2:
        confirm = input('确认删除全部?(Y/N)')
        if confirm == 'Y' or confirm == 'y':
            student_list.clear()
            print('删除全部成功！ ')
        elif confirm == 'N' or confirm == 'n':
            print('取消删除全部')
        else:
            print('输入错误，请重新输入')


def main():
    # 主程序入口，程序入口
    while True:
        print("""
            1-查询学员姓名
            2-添加学员姓名
            3-修改学员姓名
            4-删除学员姓名
            0-退出程序
            """)
        a = int(input('请选择操作:'))
        if a == 1:
            show_students()
        elif a == 2:
            add_student()
        elif a == 3:
            update_student()
        elif a == 4:
            delete_student()
        elif a == 0:
            print('退出成功，谢谢使用！')
            break


# main()
if __name__ == '__main__':
    main()