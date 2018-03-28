#-*- coding:utf-8 -*-
"""将data.txt中的文件写入VHSAdduser.xlsx中"""

from xlrd import open_workbook
from xlwt import Workbook
from xlwt import *
import os

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
DATA_PATH = os.path.join(BASE_PATH, 'data')

rb = open(DATA_PATH + '\\data.txt')
lines = rb.readlines()#wb = copy(rb)
lines.sort()
print( lines)

book = Workbook()
table = book.add_sheet('list')

#table = open(DATA)
ldata=[]
num = [a for a in lines]
num.sort()

for line in num:
    t = [int(line)]
    for a in lines[line]:
        t.append(a)
    ldata.append(t)

for i,p in enumerate(ldata):
    for j,q in enumerate(p):
        print(i,j,q)
        table.write(i,j,q)
file.save('demo.xls')

    
"""
    FirstName = line.split(',')[0]
    Phone = line.split(',')[1]
    AreaCode = line.split(',')[2]
    Email = line.split(',')[3]
    Password = line.split(',')[4]
    #UserType = line.split(',')[6】
    print(FirstName, LastName, Phone, AreaCode, Email, Password)
"""
