#from email.MINEText import MINEText
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email import encoders
import smtplib  
import os

import getpass
#msg = MINEText("hello ,I am buqing.wang,ussing python to send sn email","plain",'utf-8')


from_addr = input("input your email address :")
#隐藏密码，密码保护
from_addr_pad = getpass.getpass("input your password :")  
#print (from_addr_pad) for debug use


msg = MIMEMultipart()
msg['Subject'] = '这里是主题...'  
content1 = MIMEText('这里是正文！', 'plain', 'utf-8')  
msg.attach(content1)
s=smtplib.SMTP('smtp.yeah.net')
s= login(from_addr,from_addr_pad)
s.sendmail(from_addr,"joymine2012@yeah.net",msg.as_string())
