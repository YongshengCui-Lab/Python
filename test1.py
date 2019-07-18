import smtplib
from email.mime.text import MIMEText
from email.header import Header

username = 'yocui@ucsc.edu'
password = 'King774891913'

to_addr = '1052093667@qq.com'
stmp_server = 'smtp.gmail.com'


msg = MIMEText('发送给小学鸡（test）','plain','utf-8')

msg['From'] = Header('要命的小崔')
msg['To'] = Header('小学鸡')
msg['Subject'] = Header('自动收发邮件测试')
#server.starttls()
#server = smtplib.SMTP_SSL(stmp_server)
server = smtplib.SMTP()
server.connect(stmp_server, 25)

server.login(username, password) 

server.sendmail(username, to_addr, msg.as_string()) 

server.quit()