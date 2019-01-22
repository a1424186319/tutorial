# sqlite示例
import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()
cursor.execute("""
    SELECT id,name from student;
""")
student_list = cursor.fetchall()
print(student_list)


cursor.execute("""
    SELECT * FROM student WHERE name = '小明';       
""")
student = cursor.fetchone()
print(student)

cursor.execute("""
    SELECT * FROM student WHERE id=0;
""")
student2 = cursor.fetchone()
print(student2)

cursor.execute("""
    SELECT * FROM student WHERE id>0;
""")
# student3= cursor.fetchall()
student3_list = cursor.fetchone()
# print(student3)
print(f'学生姓名是{student3_list[1]}')


cursor.execute("""
      update student SET name="大红" WHERE id=3;
""")
connect.commit()
cursor.execute("""select * from student;""")
print(cursor.fetchall())

cursor.close()
connect.close()

"""
cursor.fechall()    取回结果集,形如[(1,'小王'),(2,'小明')]大列表,列表中的每一项是元组,是一行,元组的每一项对应每一列的值.
cursor.fetchone()   取回一条数据,形如(2,'小明').结果空返回None类型.如果select符合多条,返回多条结果里的第一条.
cursor.fechaxxx() 方法为了节省内存和速度采用了生成器结构,只能取一次.
"""

"""
sql基础语法补充:
一张表一般都有一列主键,主键primary key一般名叫 id,字段类型一般为自增整数.当insert行内容时,sql语句可以不插入id列,数据库会帮你自动插入并自增.
主键不能重复.主要好处是确保数据一致性,方便查询. 如果一列为主键,那么必然非空not[1],和唯一unique.

如果工作中一个数据库连接实例下有多个库,那么表名要带上命名空间,例如main,student.

丢弃表 drop.跟delete关键字相比更为严重,delete删除某行或清空表内容 表结构还在.而drop是完全删除丢弃整个表,内容和结构都删除.drop table[表名].

字段被双引号括住,形如SELECT 'id','name'FROM student;,结果一样

数据库概念补充:
索引:index,目录.索引会占据一定存储空间,在数据库中以二叉树型数据结构存储,建立的是目录到硬盘的数据映射.创建主键的那一列会自动创建索引.一般在查询经常比较的字段上创键索引.(如id列.phone列).优点大幅提高select的查询效率.缺点,占据更多的存储空间.
事务:transaction. 有多句sql语句时,列入sqll 插入银行交易表一行数据金额为100元.sql2 修改刚才插入数据的金额为98元,但执行sqll的时候由于用户拥堵等原因导致执行失败,这时再执行sql2必然错误或修改其它正常数据.为了避免这种情况,把这两句sql都放入一个事务执行,只要一个事务中任意一条sql执行失败,那么其它已执行的sql会回到修改前的状态(回滚rolling),只有当所有sql都执行成功,才会一起commit生效.简单来说,事务要么都执行,要么出错都不执行.优点:保持数据一致性.缺点:效率略慢.
"""

