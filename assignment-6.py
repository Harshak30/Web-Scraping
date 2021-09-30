# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:26:17 2020

@author: User
"""

import json
import urllib.request,urllib.parse,urllib.error

url=input("Enter: ")
data=urllib.request.urlopen(url).read().decode()
info = json.loads(data)
print('User count:', len(info))
sum=0
for i in range(0,len(info["comments"])):
    sum=sum+int(info["comments"][i]["count"])
print(sum)