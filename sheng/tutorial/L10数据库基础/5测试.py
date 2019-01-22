import sqlite3
connect = sqlite3.connect('testsqlite.db')
cursor = connect.cursor()
# 假性删除,为了防止数据误删方便找回.专门新建一个标识字段表示用户状态(正常.注销)
cursor.execute("""
    update employee set del_flag=1 where name="小红";  
""")
connect.commit()
cursor.execute("""
    select * from employee where del_flag=0;
""")
connect.close()
