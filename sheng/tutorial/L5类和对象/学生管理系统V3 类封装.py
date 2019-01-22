student_list = [
    {'name': '小明', 'age': 10, 'sex': 'male'},
    {'name': '小红', 'age': 12, 'sex': 'female'},
    {'name': '小李', 'age': 12, 'sex': 'male'}
]

class Student():
    # 暴露接口，操作变量student_list增删改查，只关注学生类的数据结构。不包含其余的业务逻辑。
    # 类方法或静态方法
    @classmethod
    def show_students(self):
        print('行号\t姓名\t年龄\t性别')
        print('---------------------------------')
        for i in range(0, len(student_list)):
            stu_dict = student_list[i]
            self.name = stu_dict['name']
            self.age = stu_dict['age']
            self.sex = stu_dict['sex']
            print('{:^4}{:^10}{:^4}{:^12}'.format(i + 1, self.name, self.age, self.sex))


    def __init__(self, name, age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def update(self):
        num = int(input('要修改第几个学生?:'))
        new_name = input('修改后的姓名是:')
        new_age = int(input('修改后的年龄是:'))
        new_sex = input('修改后的性别是:(male或female)')
        stu_dict = student_list[num - 1]
        stu_dict['name'] = new_name
        stu_dict['age'] = new_age
        stu_dict['sex'] = new_sex
        # print(stu_dict)
        print('修改成功！')

    @classmethod
    def delete(self):
        print(""" 删除> 请输入子操作编号:
                                   1) 按学生编号删除
                                   2) 删除全部学生（谨慎）
                       """)
        sub_num = int(input('请选择子操作：'))

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
while True:
    print("""
        欢迎使用学生管理系统
        1-查看学员姓名
        2-添加学员姓名
        3-修改学员姓名
        4-删除学员姓名
        0-退出程序
        """)
    num = int(input('请输入操作编号：'))
    if num == 1:
        Student.show_students()
    elif num == 2:
        student_dict = {}
        student_dict['name'] = input('请输入要添加的新姓名:')
        student_dict['age'] = input('请输入年龄:')
        student_dict['sex'] = input('请输入性别:(male或female)')
        student_list.append(student_dict)
        print('添加完毕！')
    elif num == 3:
        Student.update()
    elif num == 4:
        Student.delete()
    elif num == 0:
        print('退出成功，谢谢使用！')
        break