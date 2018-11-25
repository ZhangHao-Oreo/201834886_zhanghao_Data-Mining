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
import math

"""
dirs_path = "E:\\20news-18828"
file_dir_train = "E:\\data_set_2\\train_set\\"
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

def build_dict(texts):
    dict_all = [] 
    for texts_ in texts:
        dict_tmp = build_dict_text(texts_)
        dict_all.append(dict_tmp)
    return dict_all

def build_dict_count_text(texts,dict_):
    i = 0
    dict_tmp_count = []
    for texts_ in texts:
        dict_tmp_count.append(dict_count_text(texts_,dict_[i]))
        i += 1
    return dict_tmp_count



#dict_1 = build_dict_text(texts[1])

def build_dict_text(text_):
    dict_tmp = []
    words_list = str.split(text_)
    length_text = len(words_list)
    for words in words_list:    
        length_words = len(words)
        if hasNumbers(words) != 1:
            if length_words > 3 and length_words < 10:
                if words_list.count(words) > length_text*0.00002:
                    if words not in dict_tmp:
                        dict_tmp.append(words)
    return dict_tmp

def dict_count_text(text_,dict_):
    dict_c = {}
    words_list = str.split(text_)
    for dict_i in dict_: 
        dict_c[dict_i]=words_list.count(dict_i)
    return dict_c




def dict_marge(Dict_count):
#    dict_all_.remove("")
    dict_tmp = []
    for  Dict_count_i in Dict_count:
        for words in Dict_count_i:
            if Dict_count_i[words] > len(Dict_count_i)*0.00005:
                if words not in dict_tmp:
                    dict_tmp.append(words)
    return dict_tmp

def fin_dict(Dict_,Texts_):
    din_dict_tmp = []
    for text_ in Texts_:
        dict_tmp = []
        dict_tmp = dict_count_text(text_,Dict_)
        din_dict_tmp.append(dict_tmp)
    return din_dict_tmp
    





if dict_c_1["scott1"] < 0 :
    print ("1")
else:
    print ("0")
"""
name:dirs_path [str]  根目录路径
遍历所有文件
input:i [int] 遍历文件数目
"""
def travel_all_file_label(Dirs_path):
    print (Dirs_path)
    start = time.time()
    texts =[]
    label = []
    print ("将规则化的词读入内存_并保存临时文件")
    i = 0
    for fullname in iterbrowse(Dirs_path):
        file_label = fullname.split("\\")
        file_label = file_label[(len(file_label)-1)-1]
        #text = read_txt(fullname)
        #tokens = get_tokens(text)
        #stemmed = stem_tokens(tokens, PorterStemmer() )
        #text = remove_stopwords(stemmed)
        #texts.append(text)
        label.append(file_label)
#        write_txt(text,fullname)        
        i=i+1
        print ("pre_text =",i)
    print ("________OK")
    end = time.time()
    print (end-start ,"s")
    return label


def travel_all_file(Dirs_path):
    print (Dirs_path)
    start = time.time()
    texts =[]
    label = []
    print ("将规则化的词读入内存_并保存临时文件")
    i = 0
    for fullname in iterbrowse(Dirs_path):
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






def P_count(P_Texts,P_Dict):
    C_dict = []
    for text_p in P_Texts:
        vector = []
        for word in P_Dict:
             vector.append(text_p.count(word))
        C_dict.append(vector)
    return C_dict

def p_h_compute(Label_):
    tmp = Label_[0]
    P_h = {}
    i = 0
    all_len = len(Label_)
    for label_i in Label_:
        if tmp == label_i :
            i += 1
        else:
            P_h[tmp] = i/all_len
            tmp = label_i
            i = 1
    P_h[tmp] = i/all_len
    return P_h

def count_all_words(Texts_):
    tmp = 0
    for Texts_i in Texts_:
        tmp = tmp + len(Texts_i)
    return tmp


def coupute_p_D_h(word_,Dict_fin_i_,count_,i_):
    try:
        num = Dict_fin_i_[word_]
    except KeyError:
        num = 0
#    return  (num+0.001)/(all_words_f+dict_f)
#    return  (num+0.00001)/(all_words_f+count_)
    return  (num+0.00001)/(len(Texts[i_])+count_)



def dict_map_num_name():
    tmp = {}
    i = 0
    for P_h_i in P_h:
        tmp[i] = P_h_i
        i += 1
    return tmp

def Find_Label_range(F_Label):
    FLabels = []
    c_label = F_Label[0]
    star = 0
    i = 0
    j = 0
    for label_f in F_Label:
        if c_label == label_f:
            i += 1
        else:
            FLabels.append([j,star,i-1])
            c_label = label_f
            star = i
            j += 1
            i += 1
    FLabels.append([j,star,i])        
    return FLabels

def test_label(Texts_test_  ,Dict_fin):
    tmp_dict = {}
    for i in range (len(Dict_fin)):
        tmp = 0
        for word_i in Texts_test_:
            tmp = tmp + math.log(coupute_p_D_h(word_i,Dict_fin[i],len(Texts_test_),i))
        tmp = tmp+math.log((P_h[dict_map[i]]))
        #tmp = tmp +  math.log(len(Texts_test_)) - math.log(all_words_f)
        tmp_dict[i] = tmp
    return max(tmp_dict,key=tmp_dict.get)

#test_label(Texts_test[1],Dict_fin)


test_rate(Texts_test)

def test_rate(Texts_test):
    tmp = 0
    for i in range(len(range_test)):
        for j in range (range_test[i][1],range_test[i][2]):
            if test_label(Texts_test[j],Dict_fin) == i:
                tmp += 1
    print (tmp/range_test[len(range_test)-1][2]*100,"%")            

#按照类型归类文本
Texts = travel_all_file_merge(file_dir_train)
wirte_csv("E:\\real\\Texts.csv" ,Texts)
#计算总词数
all_words_f = count_all_words(Texts)
#分别建立词典
Dict_all = build_dict(Texts)
#统计各词典词频
Dict_count = build_dict_count_text(Texts,Dict_all)
#建立统一词典
Dict = dict_marge(Dict_count)
wirte_csv("E:\\real\\Dict.csv" ,Dict)
del Dict_count
del Dict_all
Texts.remove("")
#统计统一词典词频
Dict_fin = fin_dict(Dict,Texts)
#词典大小
dict_f = len(Dict_fin[0])
#先验概率
P_h = p_h_compute(Label)
wirte_csv("E:\\real\\P_h.csv" ,P_h)
#建立词典字母与序号映射
dict_map = dict_map_num_name()
#读取测试集
Texts_test,Label_test = travel_all_file(file_dir_test)
#测试集范围
range_test = Find_Label_range(Label_test)





