import pymysql.cursors

connection = pymysql.connect(host = '127.0.0.1',
                             user = 'root',
                             password = '123',
                             db = 'test',
                             port = 3306,
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor
                             )
try:
    with connection.cursor() as cursor:
        sql = """select * from shirt"""
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
except Exception as a:
    print(a)
finally:
    cursor.close()



try:
    with connection.cursor() as cursor:
        sql1 = """select id from preson where name='小李';"""
        cursor.execute(sql1)
        res1 = cursor.fetchone()
        print(res1)
        xiaohong_id = res1['id']


        sql = """update shirt set color="黄色" where person_id=%s and style='裙子';"""
        cursor.execute(sql,(xiaohong_id))
        sss = cursor.fetchall()
        print(sss)
    connection.commit()
except Exception as a:
    print(a)
finally:
    cursor.close()





