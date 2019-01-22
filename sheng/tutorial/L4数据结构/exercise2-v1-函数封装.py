#学生管理v1-函数封装
#之前的非函数版本，打印学生列表代码重复，如果要修改需要处处修改，while、if、嵌套代码 越来越长，不容易维护。所以我们封装成函数版。函数封装将大问题分解成小问题
student_list = ['小王', '小红', '小李']

def show_students():
    """打印学生列表"""
    print('行号\t\t姓名')
    print('-----------------')
    for i in range(0, len(student_list)):
        print(i + 1, '\t\t', student_list[i])


def add_student():
    """添加学生"""
    student_list.append(input('请输入要添加的新姓名:'))
    print('添加完毕！')


def update_student():
    """修改学生"""
    show_students()

    # b = int(input('要修改第几个学生？'))
    # c = input('修改后的姓名是：')
    student_list[int(input('要修改第几个学生？')) - 1] = input('修改后的姓名是：')
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
        d = int(input('要删除第几个学生？'))
        student_list.pop(d - 1)
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
if __name__=='__main__':
    main()