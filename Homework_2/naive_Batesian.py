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
from _collections import defaultdict


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

def travel_all_file_merge(Dirs_path = "E:\\tmp\\"):          
        texts = []
        tmp_label = " "     
        text_ = ""
        for fullname in iterbrowse(Dirs_path):      
            file_label = fullname.split("\\")
            file_label = file_label[(len(file_label)-1)-1]
            text = read_txt(fullname)
            tokens = get_tokens(text)
            stemmed = stem_tokens(tokens, PorterStemmer() )
            text = remove_stopwords(stemmed)
            text = " ".join(text)
            if tmp_label == file_label:
                text_ = text_+ text + " "
            else:
                texts.append(text_)
                tmp_label = file_label
                text_ = ""
                text_ = text_+ text + " "
        texts.append(text_)
        return texts
    
texts = travel_all_file_merge(file_dir_train)



dict_all = [] 
for texts_ in texts:
    dict_tmp = build_dict_text(texts_)
    dict_all.append(dict_tmp)


dict_tmp_count = build_dict_count_text(texts,dict_all)
def build_dict_count_text(text_,dict_):
    i = 0
    dict_tmp_count = []
    for texts_ in texts:
        dict_tmp_count.append(dict_count_text(texts_,dict_[i]))
        i += 1
    return dict_tmp_count



dict_1 = build_dict_text(texts[1])

def build_dict_text(text_=texts[1]):
    dict_tmp = []
    words_list = str.split(text_)
    length_text = len(words_list)
    for words in words_list:    
        length_words = len(words)
        if length_words > 3 and length_words < 10:
           if words_list.count(words) > length_text*0.0001:
               if words not in dict_tmp:
                   dict_tmp.append(words)
    return dict_tmp

def dict_count_text(text_,dict_):
    dict_c = {}
    words_list = str.split(text_)
    for dict_i in dict_: 
        dict_c[dict_i]=words_list.count(dict_i)
    return dict_c

dict_c_1 = dict_count_text(texts[1],dict_1)



if dict_c_1["scott1"] < 0 :
    print ("1")
else:
    print ("0")
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


def Find_Label(F_Label):
    FLabels = []
    c_label = F_Label[0]
    i = 0
    for label_f in F_Label:
        if c_label == label_f:
            i += 1
        else:
            FLabels.append([c_label,i-1])
            c_label = label_f
            i += 1
    FLabels.append([c_label,i-1])
    return FLabels



def P_count(P_Texts,P_Dict):
    C_dict = []
    for text_p in P_Texts:
        vector = []
        for word in P_Dict:
             vector.append(text_p.count(word))
        C_dict.append(vector)
    return C_dict

def NBC(C_dict,FLabels):
    vector = []
    h = 0
    for i  in range( len(FLabels)):
        vectors = []
        vectors = C_dict[h]
        for j in range (h +1 ,FLabels[i][1]):
            h += 1
            for k in range(0,len(C_dict[j])):
                vectors[k] += C_dict[j][k]                
        vector.append(vectors)



def NBC(Texts_,FLabels):
    vector = []
    h = 0
    for i  in range( len(FLabels)):
        vectors = []
        for j in range (h +1 ,FLabels[i][1]):
            h += 1
            for k in range(len(Texts_)):
                vectors[k] += C_dict[j][k]                
        vector.append(vectors)


Texts,Label = travel_all_file(file_dir_train)
record ("path","Label",Label)
record ("path","Texts",Texts)
#    Texts = read_csv(tmp_texts)
#    Label = read_csv(tmp_label)
#    Label = process_str(Label) 
Texts_test,Label_test = travel_all_file(file_dir_test)


Dict = travel_all_file_build_dict(Texts)

#    Dict = read_csv(tmp_Dict)
#    Dict = process_str(Dict)
record ("path","Dict",Dict)
C_dict = P_count(Texts,Dict)
FLabels = Find_Label(Label)






try:
    num = dict_c_1["scott1"]
except KeyError:
    num = 0
    print(num) 
else:
    print(num) 