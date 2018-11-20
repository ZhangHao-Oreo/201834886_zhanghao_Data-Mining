# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:29:16 2018

@author: zh_14
"""

#--------使用的库----------
import nltk
import string
from nltk.corpus import stopwords     #使用nltk提供的的stopwords
from nltk.stem.porter import PorterStemmer        # 提取词干
import os
import csv
import time
import re


"""
dirs_path = "E:\\20news-18828"
file_dir_train = "E:\\data_set_3\\train_set\\"
file_dir_test = "E:\\data_set_3\\test_set\\"


tmp_texts = "E:\\real\\Texts.csv"
tmp_label = "E:\\real\\Label.csv"
tmp_Dict = "E:\\real\\Dict.csv"

tmp_Label_test = "E:\\real\\Label_test.csv"
tmp_Texts_test = "E:\\real\\Tests_test.csv"


Dict = []
Texts = []
Label = []
"""

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
def stem_tokens(tokens,Stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(Stemmer.stem(item))
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
    text = text.replace('\r',' ').replace('\n',' ').replace('\t',' ')
    f.close()
    return text


def wirte_csv(path,text):
    csvFile = open(path, "w",newline='')  # newline=''  存在换行符号问题
    try:
        writer = csv.writer(csvFile)
        writer.writerows(text)
    except Exception :
        print("WRITE ERROR")
    finally:
        csvFile.close()
    return     



        
def read_csv(path):
    csvFile = open(path,'r',encoding="gbk")# 读取以utf-8
    try:
        context = csvFile.read() # 读取成str
        text_line = context.split("\n")#  以回车符\n分割成单独的行
        #每一行的各个元素是以【,】分割的，因此可以
        length = len(text_line)
        for i in range(length):
            text_line[i-1] = text_line[i-1].split(",")
    finally:
        csvFile.close()  
    return text_line
     

"""
name:process_str
input: List [list]  待处理的字符
output: 
"""


def process_str(List):
    for i in range (len(List)):
        tmp_str = str(List[i])
        tmp_str = tmp_str.replace(',','').replace('[','').replace(']','').replace('\'','').replace(' ','')
        List[i] = tmp_str
    return List




def read_csv_dict(path):
    csvFile = open(path,'r',encoding="gbk")# 读取以utf-8
    try:
        context = csvFile.read() # 读取成str
        text_line = context.split("\n")#  以回车符\n分割成单独的行
        #每一行的各个元素是以【,】分割的，因此可以
    finally:
        csvFile.close()  
    return text_line


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
def travel_all_file(Dirs_path):
    print (Dirs_path)
    start = time.time()
    texts =[]
    label = []
    print ("将规则化的词读入内存_并保存临时文件")
    i = 0
    for fullname in iterbrowse(Dirs_path):
        #fullname是绝对路径
        #print fullname 
        #filename=os.path.basename(fullname)
        #filename是目录下的所有文件名
        #print (filename)
        #读文件
        file_label = fullname.split("\\")
        file_label = file_label[(len(file_label)-1)-1]
        text = read_txt(fullname)
        tokens = get_tokens(text)
        stemmed = stem_tokens(tokens, PorterStemmer() )
        text = remove_stopwords(stemmed)
        texts.append(text)
        label.append(file_label)
#        write_txt(text,fullname)        
        i=i+1
        print ("pre_text =",i)
    
    print ("________OK")
    end = time.time()
    print (end-start ,"s")
    return texts,label

"""
name:记录数据
input:path [str]  文件路径  flag [str] 操作类型  content  [list]  输入内容 
"""
def record (path,flag,content):
    if flag == "Texts":
        wirte_csv(tmp_texts ,content)
        print ("写入 Tests 成功 ")
    if flag == "Label":
        wirte_csv(tmp_label ,content)
        print ("写入 Label 成功 ")
    if flag == "Dict":
        wirte_csv(tmp_Dict ,content)
        print ("写入 Dict 成功 ")
    if flag == "TF_IDF":
        wirte_csv(tmp_TF_IDF,content)
        print ("写入 TF_IDF 成功 ")
    if flag == "Texts_test" :
        wirte_csv(tmp_Texts_test ,content)
        print ("写入 Tests_test 成功 ")
    if flag == "Label_test":
        wirte_csv(tmp_Label_test ,content)
        print ("写入 Label_test 成功 ")
    if flag == "Other":
        wirte_csv(path ,content)
        print ("写入 Other 成功 ")


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))   

"""
name:build_dict
input:text [str] 输入单个文本全部内容  texts [list]   所有文档
构建词典
output:dict_tmp [str] 
"""
def build_dict(text,dict_tmp,texts):
    #words_list = str.split(text)
    words_list = text
    for words in words_list:    
        if hasNumbers(words) == False :
    #        print ( hasNumbers(words))
    #    for w in words:
            length_words = len(words)
            if length_words > 3 and length_words < 14:
                if text.count(words) > 3:
                #    if word_in_file_num(texts,words) > 5:
                    if words not in dict_tmp:
                        dict_tmp.append(words)
                    #print (words)
    return dict_tmp




"""
name:texts [list]  所以文件
遍历所有文件构建词典
input:i [int] 遍历文件数目
"""
def travel_all_file_build_dict(texts):
    start = time.time()
    i = 0  
    dict_tmp = []
    for text in texts:
        dict_tmp = build_dict(text,dict_tmp,texts)
        i += 1
        print ("build_dict =",i)
#    print ("\n SUCCESS travel_all_file_build_dict number =",i)
    end = time.time()
    print ("构建词典____ok")
    print (end-start ,"s")
    return dict_tmp

"""    
    for fullname in iterbrowse(dirs_path):
        #fullname是绝对路径
        #print fullname 
        #filename=os.path.basename(fullname)
        #filename是目录下的所有文件名bn 
        #print (filename)
        #读文件
        text = ""
        text = read_txt(fullname)
        dict = build_dict(text,dict,texts)
        i=i+1
        print ("build_dict =",i)
        # (dict)
"""

P_count


Texts,Label = travel_all_file(file_dir_train)
record ("path","Label",Label)
record ("path","Texts",Texts)    
Dict = travel_all_file_build_dict(Texts)
record ("path","Dict",Dict)

