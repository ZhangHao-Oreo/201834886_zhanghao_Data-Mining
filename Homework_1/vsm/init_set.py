# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:40:34 2018

@author: zh_lab
"""

#用于划分数据集和测试集




#遍历每一个文件夹下文件
import os

#-----other-----
dirs_path = ("E:\\new1")
"""
name:iterbrowse
文件夹路径
input:path [str]
"""
def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)
"""
name:dirs_path [str]  根目录路径
遍历所有文件
input:i [int] 遍历文件数目
"""
def travel_all_file(dirs_path):
    i = 0
    for fullname in iterbrowse(dirs_path):
        #fullname是绝对路径
        #print fullname 
        filename=os.path.basename(fullname)
        #filename是目录下的所有文件名
        print (filename)
        i=i+1
    return i