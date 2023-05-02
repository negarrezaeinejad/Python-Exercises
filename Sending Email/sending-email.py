from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib
import config

templ=Template(Path('template.html').read_text())
body=templ.substitute({'name':'Alex'})

message=MIMEMultipart()
message['from']='negarrezayinejad@gmail.com'
message['to']='ncgarrezaei@yahoo.com'
message['subject']='test'
message.attach(MIMEText(body,'html'))

message.attach(MIMEImage(Path('Figure_1.png').read_bytes()))
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config.username,config.password)
    smtp.send_message(message)
    print('message has been sent...')
