#!/usr/bin/env python3
import os
import re
import emails 
import reports
import requests
from datetime import datetime

path_data = "./supplier-data/descriptions/"

From = "automation@example.com"
To = "student-03-899fd644f727@example.com"
Subject = "Upload Completed - Online Fruit Store"
Body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
Attachment = "/tmp/processed.pdf"

def processed_data():
    string = ""
    for filename in os.listdir(path_data):
        with open(path_data + filename, "r") as data:
                structured_data = data.read().split("\n")
                string += "name: " + structured_data[0] + "<br/>"
                string += "weight: " + structured_data[1]
                string += "<br/><br/>" 
    return string

if __name__ == "__main__":
    Para = processed_data()
    #print(type(Paragraph))
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    today = datetime.today()
    Title = "Processed Update on {} {}, {}".format(today.strftime("%B"), today.day, today.year)
    reports.generate_report(Attachment, Title, Para)
    message = emails.generate_email(From, To, Subject, Body, Attachment)
    emails.send_email(message)