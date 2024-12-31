# import office
#
# office.image.img2Cartoon(path='Component 26 – 4.png',client_api='mniU1XIRVy001lUZBWCY0KU2', client_secret='qPZQ77qAqqcZAcFaNdbQK2ZcYK6eDZRX')

# import smtplib
# from email.mime.text import MIMEText
#
# # 设置邮件内容
# msg = MIMEText('123', 'plain', 'utf-8')
# msg['Subject'] = '测试邮件'
# msg['From'] = 'yysxiaohao201802@163.com'
# msg['To'] = 'ajh415@qq.com'
#
# server = smtplib.SMTP('smtp.163.com')
# try:
#     # 连接到SMTP服务器并登录
#     server.starttls()
#     server.login('yysxiaohao201802@163.com', 'TRRNKSJQSXZQOLAL')
#
#     # 发送邮件
#     server.sendmail(msg['From'], msg['To'], msg.as_string())
#     print("邮件已成功发送")
# except Exception as e:
#     print("发送邮件时出现错误:", str(e))
# finally:
#     # 关闭与SMTP服务器的连接
#     server.quit()

import yagmail

yag = yagmail.SMTP(user="ivazuxlm@gmail.com", password="xxew pjpa njtb ajpn")
contents = ['This is the body, and here is just text']
yag.send(to='ajh415@qq.com', subject="title", contents=contents)
