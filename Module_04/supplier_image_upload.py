#!/usr/bin/env python3
import requests
import os

folder_path = "./supplier-data/images/"
url = "http://104.198.65.218/upload/"


for filename in os.listdir(folder_path):
	file = os.path.join(folder_path, filename)
	#print(file)
	if ".jpeg" == os.path.splitext(file)[1].lower():
		print(file)
		with open(file, "rb") as opened:
			r = requests.post(url, files={"file": opened})
			r.raise_for_status()
