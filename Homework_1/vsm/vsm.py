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
#from nltk.stem.porter import *        # 提取词干
#------------------------


#--------other------------
text = ("My names is zhanghao ;';'';;' 2 dsdsd playing ")
filename = ("E:\mytest.txt")



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

def write_txt(text,filename):
    #写文件
    f = open(filename,'w',errors='ignore')
    str = " ".join(text)
    f.write(str)
    text = ""   #将text转化回str类型，并且重置
    f.close()



#--------------------------------------------------------

tokens = get_tokens(text)
stemmed = stem_tokens(filtered, PorterStemmer())
text = remove_stopwords(stemmed)
write_txt(text,filename)

