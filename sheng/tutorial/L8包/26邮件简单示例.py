import yagmail
import os

sender = 'chen454454545@foxmail.com'
password = 'wcnwzcpjywtxidba'

target = '3553974384@qq.com'

yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com',port='465',smtp_ssl=True)

contents = '一个秘密'

yag.send(to=target,subject='我想要两颗西柚',contents=contents)
print('发送成功')