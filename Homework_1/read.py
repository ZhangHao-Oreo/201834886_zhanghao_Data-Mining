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
path = "E:\new1" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          f = open(path+"/"+file); #打开文件
          iter_f = iter(f); #创建迭代器
          str = ""
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              str = str + line
          s.append(str) #每个文件的文本存到list中
print(s) #打印结果




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