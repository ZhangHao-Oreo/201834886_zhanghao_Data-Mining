# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:11:11 2018

@author: zh_14
"""



import os


dirs_path = "E:\\Tweets.txt"




"""
name:read_text
读取信息
"""
def read_text(dirs_path):
    vectors = []
    label = []
    f = open(dirs_path, 'r')
    line = f.readline()
    while line:        
        label.append(int(line[line.rfind("\"cluster\"")+11:line.rfind("}")]))
        vectors.append(line[line.find("\"text\"")+9:line.rfind(",")-1])
        line = f.readline()
    return vectors, label


texts,label =  read_text( "E:\\Tweets.txt")