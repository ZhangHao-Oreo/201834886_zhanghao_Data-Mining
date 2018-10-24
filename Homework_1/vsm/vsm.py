# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 00:50:41 2018

@author: zh_lab
"""

"""
规则化
1.大小写统一
2.单复数
3.词性(ing ed)
4.去标点符号
5.(去数字)——需要实验验证，可能数字信息不太能表述文章信息   ++++++
"""
#--------使用的库----------
import nltk
import string
from nltk.corpus import stopwords     #使用nltk提供的的stopwords
from nltk.stem.porter import PorterStemmer        # 提取词干
import os

#------------------------


#--------other------------
#text = ("My names is zhanghao ;';'';;' 2 dsdsd playing is zhanghao names name ")
#filename = ("E:\mytest.txt")
dirs_path = ("E:\\20news-18828")      #   E:\\new1
dict = []


#--------------------

#-----------------------functions-------------------

"""
name:get_tokens
input:text [str]
去除给定text的大小写以及标点符号
output:tokens [list]
"""
def get_tokens(text):
    lowers = text.lower()   #大小写
                            #去除标点符号    
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


"""
name:stem_tokens
input:tokens [list]  
提取词干
output:stemmed [list]
"""
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed



"""
name:remove_stopwords
input:tokens [list]  
过滤stopwords
output:filtered [list]

"""
def remove_stopwords(tokens):
    filtered = [w for w in tokens if not w in stopwords.words('english')]   #过滤stopwords
    return filtered


def read_txt(filename):
    #读文件
    f = open(filename,'r',errors='ignore')
    text = f.read()
    #去除读取文件后的格式（换行 缩进）
    text = text.replace('\r','').replace('\n','').replace('\t','')
    f.close()
    return text

def write_txt(text,filename):
    #写文件
    f = open(filename,'w',errors='ignore')
    str = " ".join(text)
    f.write(str)
    text = ""   #将text转化回str类型，并且重置
    f.close()


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
        #print (filename)
        #读文件
        text = read_txt(fullname)
        tokens = get_tokens(text)
        stemmed = stem_tokens(tokens, PorterStemmer())
        text = remove_stopwords(stemmed)
        write_txt(text,fullname)        
        i=i+1
        print ("pre_text =",i)
    print ("SUCCESS file_number =",i)
    return i




"""
name:build_dict
input:text [str] 输入单个文本全部内容
构建词典
output:dict [str] 
"""
def build_dict(text,dict):
    words_list = str.split(text)
    for words in words_list:
    #    for w in words:
        if words not in dict:
            dict.append(words)
    return dict




"""
name:dirs_path [str]  根目录路径
遍历所有文件构建词典
input:i [int] 遍历文件数目
"""
def travel_all_file_build_dict(dirs_path):
    i = 0
    dict = []
    for fullname in iterbrowse(dirs_path):
        #fullname是绝对路径
        #print fullname 
        filename=os.path.basename(fullname)
        #filename是目录下的所有文件名
        #print (filename)
        #读文件
        text = ""
        text = read_txt(fullname)
        dict = build_dict(text,dict)
        i=i+1
        print ("build_dict =",i)
        # (dict)
    print ("\n SUCCESS travel_all_file_build_dict number =",i)
    return dict





#--------------------------------------------------------

#规则化每个文本
travel_all_file(dirs_path)

dict = travel_all_file_build_dict(dirs_path)#dirs_path