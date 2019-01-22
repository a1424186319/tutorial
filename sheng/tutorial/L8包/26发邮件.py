# coding=utf-8
import smtplib
from email.mime.text import MIMEText

msg_from = '1424186319@qq.com'  # 发送方邮箱
passwd = 'wcnwzcpjywtxidba'  # 填入发送方邮箱的授权码
msg_to = '3553974384@qq.com'  # 收件人邮箱
# IMAP/SMTP服务  wcnwzcpjywtxidba
# POP3/SMTP服务  phxnsgzimoecibdj
subject = "一个忠告"  # 主题
content = "答应我这节课不要睡觉好吗"  # 正文
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
except s.SMTPException as e:
    print("发送失败")
finally:
    s.quit()
