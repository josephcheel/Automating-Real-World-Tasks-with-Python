#!/usr/bin/env python3
import os
import re
import requests
import json

path_data = "./supplier-data/descriptions/"
path = "http://34.67.144.204/fruits/"

post_dict = {
     "name"			:	"",
     "weight"		:	0,
     "description"	:	"",
     "image_name"	:	""
}

for filename in os.listdir(path_data):
    with open(path_data + filename, "r") as data:
        structured_data = data.read().split("\n")
        post_dict["name"] = structured_data[0]
        post_dict["weight"] = int(re.sub(r"\D", "", structured_data[1]))
        post_dict["description"] = structured_data[2]
        root, _ = os.path.splitext(filename)
        renamed =  root  + ".jpeg"
        post_dict["image_name"] = renamed
        post_json = json.dumps(post_dict, indent=2)
        print(post_json)
        headers = {"Content-Type": "application/json"}
        requests.post(path, data=post_json, headers=headers)