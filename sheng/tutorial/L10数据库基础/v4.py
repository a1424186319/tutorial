import sqlite3
conn = sqlite3.connect('testsqlite.db')
cursor = conn.cursor()
# def create_table():
#     cursor.execute("""
#         create table  student0(
#           id integer primary key autoincrement ,
#           name text not null,
#           sex text,
#           age integer,
#           phone text
#         )
#     """)
#     conn.commit()
#     cursor.close()
#     conn.close()
def show_students():
    cursor.execute(""" select * from student0;""")
    student_list = cursor.fetchall()
    for s in student_list:
        print(f'{s[0]}\t\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}')
def append_data():
    name = input('请输入新学生的姓名:')
    age = input('请输入新学生的年龄:')
    sex = input('请输入新学生的性别:')
    phone = input('请输入新学生的电话:')
    insert_sql = "insert into student0(name,age,sex,phone)VALUES ('%s','%s','%s','%s')" % (name, age,sex,phone)
    cursor.execute(insert_sql)
    conn.commit()
    print('添加成功!')

def update_date():
    show_students()
    select_number = int(input('请输入要修改的学员的编号：'))
    # 知道了要修改的学员的编号，然后进行修改。
    new_name = input('请输入修改后的姓名:')
    new_age = input('请输入修改后的年龄：')
    new_sex = input('请输入修改后的性别：')
    new_phone = input('请输入修改后的电话：')
    # update_sql = "update student0 set name='%s',age= '%s',sex= '%s',phone = '%s' where id=%d" % (new_name, new_age, new_sex,new_phone, select_number)
    update_sql = f"update student0 set name='{new_name}',age= '{new_age}',sex= '{new_sex}',phone = '{new_phone}' where id='{select_number}'"
    cursor.execute(update_sql)
    conn.commit()
    print("修改成功")
def delete_data():
    id1 = int(input("请输入要删除的学生id："))
    sqlStr = f"select * from student0 where id = {id1};"
    conn.execute(sqlStr)
    s = input("请确认删除(如果删除请输入'Y',不删除请输入'N'):")
    if s == 'Y' or s =='y':
        sqlStr = f"delete from student0 where id = {id1}"
        conn.execute(sqlStr)
        conn.commit()
        print("删除成功")
    elif s == 'N' or s =='n':
        print('取消删除全部')

def main():
    while True:
        print("""
                    1-查询学员姓名
                    2-添加学员姓名
                    3-修改学员姓名
                    4-删除学员姓名
                    0-退出程序
                    """)
        choice = int(input("请输入你的选择:"))
        if choice == 0:
            conn.close()
            print('退出成功,感谢您的使用')
            break
        elif choice == 1:
            show_students()
        elif choice == 2:
            append_data()
        elif choice == 3:
            update_date()
        elif choice == 4:
            delete_data()

if __name__ == '__main__':
    # create_table()
    main()

