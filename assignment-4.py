# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:12:08 2020

@author: User
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input("Enter position:"))-1
count = int(input("Enter count:"))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
   # print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])
