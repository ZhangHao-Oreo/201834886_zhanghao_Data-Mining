# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:34:03 2018

@author: zh_lab
"""

f = open('E:\mytest.txt','r',errors='ignore')
text = f.read()
#str(text, encoding = "utf-8")
text = text.replace('\r','').replace('\n','').replace('\t','')
#text.replace("\n","")
f.close()


import os

def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)


for fullname in iterbrowse("E:\\new"):
    #fullname是绝对路径
    #print fullname 
    filename=os.path.basename(fullname)
    #filename是目录下的所有文件名
    print (filename)






class dict:
    def __init__(self):
        self.name = '';
        self.l_num = 0;
        self.g_num  = 0;

n1 = dict()


set1 = set(["apples","feet","pigs","loves"])
for d in set1:
   # print (d)
    n1 = dict()
    
    
array = [('the', 6,1), ('python', 5), ('a', 5), ('and', 4), ('films', 3), ('in', 3), 
('madefortv', 2), ('on', 2), ('by', 2), ('was', 2)]




monty = TextBlob("We feet no longer the Knights who say Ni. "
                   "We are now the Knights who say Ekki ekki ekki PTANG.")
monty.word_counts['foot']