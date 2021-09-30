# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:48:27 2020
@author: User
"""

import re
fi=open('regex_sum.txt')
lst=list()
for line in fi:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    if len(stuff) > 0:
        for i in range(len(stuff)):
            numb=int(stuff[i])
            lst.append(numb)
print(sum(lst))

    