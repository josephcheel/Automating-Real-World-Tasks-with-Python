#!/usr/bin/env python3
from email.message import EmailMessage
import mimetypes
import smtplib
import os


def generate_email(From, To, Subject, Body, Attachment):
    message = EmailMessage()
    message["From"] = From
    message["To"] = To
    message["Subject"] = Subject
    message.set_content(Body)
	
    mime_type, _ = mimetypes.guess_type(Attachment)
    mime_type, mime_subtype = mime_type.split("/")
    with open(Attachment, "rb") as report:
        message.add_attachment(report.read(), mime_type, mime_subtype, filename =os.path.basename(Attachment))
    return message

def send_email(message):
    mail_server = smtplib.SMTP("localhost")
    mail_server.set_debuglevel(1)
    mail_server.send_message(message)
    mail_server.quit()
    
   
