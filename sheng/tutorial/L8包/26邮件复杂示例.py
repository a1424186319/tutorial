import yagmail
import os

sender = '1106115374@qq.com'    # 发送人
password = 'hdujorbmnhfriicg'   # 邮箱授权码
target = '1424186319@qq.com'

html = """


"""
# attachment_path = os.path.join(os.path.dirname(__file__), 'demo.jpg')
contents = ['测试yagmial示例2', html]  # [邮件标题，正文，附件]

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', port=465, smtp_ssl=True)
yag.send(to=target, contents=contents)  # subject 邮件名
print('已发送')