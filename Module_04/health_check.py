#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails

From = "automation@example.com"
To = ""

def report_cpu():
    Subject = "Error - CPU usage is over 80%"
    Body = "Please check your system and resolve the issue as soon as possible"
    message = emails.generate_email(From, To, Subject, Body,None)
    emails.send_email(message)

def report_available_disk():
    Subject = "Error - Available disk space is less than 20%%"
    Body = "Please check your system and resolve the issue as soon as possible"
    message = emails.generate_email(From, To, Subject, Body,None)
    emails.send_email(message)
    
def report_less_than_500():
    Subject = "Error - Available memory is less than 500MB"
    Body = "Please check your system and resolve the issue as soon as possible"
    message = emails.generate_email(From, To, Subject, Body,None)
    emails.send_email(message)

def report_localhost():
    Subject = "Error - localhost cannot be resolved to 127.0.0.1"
    Body = "Please check your system and resolve the issue as soon as possible"
    message = emails.generate_email(From, To, Subject, Body, None)
    emails.send_email(message)


if __name__ == "__main__":
    # print(psutil.cpu_percent())
    # print(psutil.disk_usage("/").percent) #percent
    # print(psutil.disk_usage("/").free / (1024 * 1024)) #percent
    # print(socket.gethostbyname("localhost"))
    if psutil.cpu_percent() > 80:
        report_cpu()
    if psutil.disk_usage("/").percent > 80:
        report_available_disk()
    if psutil.disk_usage("/").free < 500:
        report_less_than_500()
    if socket.gethostbyname("localhost") != "127.0.0.1":
        report_localhost()
	