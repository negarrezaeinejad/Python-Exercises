# Sending Email

This Python code sends an email with an HTML body and an image attachment. It makes use of the `email.mime` and `smtplib` libraries for constructing and sending the email, and `config` module to store email credentials.

## Usage

1. Update the `config.py` file with your email username and password.
2. Update the recipient's email address in the `message['to']` field.
3. Update the message subject and body content in the `message['subject']` and `body` variables.
4. Attach an image or file by providing the file path in `Path('file_path').read_bytes()` line of code.
5. Run the script.

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib
import config

# Read HTML template and substitute values
templ=Template(Path('template.html').read_text())
body=templ.substitute({'name':'Alex'})

# Construct message object
message=MIMEMultipart()
message['from']='sender@gmail.com'
message['to']='recipient@gmail.com'
message['subject']='test'
message.attach(MIMEText(body,'html'))

# Attach image to the message
message.attach(MIMEImage(Path('Figure_1.png').read_bytes()))

# Send email using SMTP
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config.username,config.password)
    smtp.send_message(message)
    print('message has been sent...')
```

## Example Output

The above code sends an email with an HTML body and an image attachment to the recipient's email address. The email should appear in the recipient's inbox with the specified subject, body content, and attached image. The message "message has been sent..." is printed to the console to confirm that the email was sent successfully.