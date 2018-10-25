# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:40:34 2018

@author: zh_lab
"""

#用于划分数据集和测试集




#遍历每一个文件夹下文件
import os
import shutil  #用于拷贝文件
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





"""
name:
input:dirs_path  [str]   所有数据根目录
划分数据集
"""
def init_set(dirs_path='E:\\20news-18828'):
    for dirs in os.listdir(dirs_path):
        files_path = os.path.join(dirs_path, dirs)
        os.makedirs('E:\\train_set\\' + dirs)
        os.makedirs('E:\\test_set\\' + dirs)
        i = 0
        for file in os.listdir(files_path):
            if i < len(os.listdir(files_path)) * 0.9:
                train_file = os.path.join('E:\\train_set\\' + dirs, file)
                shutil.copyfile(os.path.join(files_path, file),train_file)
            else:
                test_file = os.path.join('E:\\test_set\\' + dirs, file)
                shutil.copyfile(os.path.join(files_path, file), test_file)
            i += 1
    
    
    
    
    
    
    
    