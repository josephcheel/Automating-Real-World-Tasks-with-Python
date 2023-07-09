#! /usr/bin/env python3
import os
import json
import requests

origin_path = "/data/feedback/"

dictionary = { "title":     "",
                "name":     "",
                "date":     "", 
                "feedback": ""
        }

for review in os.listdir(origin_path):
    name, extension = os.path.splitext(review)
    if (extension == ".txt"):
        with open(origin_path + review, "r") as file_data:
            data = file_data.read().split("\n")
            for element, line in zip(dictionary, data):
                dictionary[element] = line
                #print(dictionary[element] + line)
        response = requests.post("http://146.148.99.46/feedback/", data=dictionary)
        response.raise_for_status()