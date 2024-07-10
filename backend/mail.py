# -*- coding: UTF-8 -*- #
"""
@filename:mail.py
@author:wdh
@time:2024-07-10

@description: smtplib
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

def send_email(subject: str, email_to: str, body: str):
    message = MIMEMultipart()
    message["From"] = settings.MAIL_FROM
    message["To"] = email_to
    message["Subject"] = subject

    # 添加邮件内容
    message.attach(MIMEText(body, "html"))

    # 创建SSL上下文并降低安全级别
    context = ssl.create_default_context()
    context.set_ciphers("DEFAULT:@SECLEVEL=1")

    try:
        with smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT, context=context) as server:
            server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
            server.sendmail(settings.MAIL_FROM, email_to, message.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")