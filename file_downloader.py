#!/usr/bin/env python 

import os , requests

def download(url):
    get_response = requests.get(url)
    filename=url.split("/")[-1]
    print(filename)
    with open(filename,"wb") as out_file:
    	out_file.write(get_response.content)

    print(get_response)
download("https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-600.exe")    