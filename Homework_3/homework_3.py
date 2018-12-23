# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:11:11 2018

@author: zh_14
"""


import os
import nltk
import string
from nltk.corpus import stopwords     #使用nltk提供的的stopwords
from nltk.stem.porter import PorterStemmer        # 提取词干
import math
import re
import numpy as np
import time
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN
from sklearn import  metrics

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

"""
name:get_tokens
input:text [str]
去除给定text的大小写以及标点符号
output:tokens [list]
"""
def get_tokens(text):
    lowers = text.lower()   #大小写
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


def process_text(text_):
    vec_tmp = []
    for text in text_:
        tokens = get_tokens(text)
        stemmed = stem_tokens(tokens, PorterStemmer() )
        text = remove_stopwords(stemmed)
        vec_tmp.append(text)
    return vec_tmp


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString)) 
"""
name:build_dict
input:text [str] 输入单个文本全部内容  texts [list]   所有文档
构建词典
output:dict_tmp [str] 
"""
def build_dict(texts_):
    dict_tmp = []
    #words_list = str.split(text)
    for text in texts_:      
        words_list = text
        for words in words_list:    
            if hasNumbers(words) == False :
                #        print ( hasNumbers(words))
                #    for w in words:
                length_words = len(words)
                if length_words > 2 and length_words < 17:
                    #if text.count(words) > 3:
                    #    if word_in_file_num(texts,words) > 5:
                    if words not in dict_tmp:
                        dict_tmp.append(words)
                        #print (words)
    return dict_tmp


def compute_tf(text,word):
    tf = text.count(word)
    if tf > 0:
        tf = 1 + math.log(tf)
    else:
        tf = 0
    return tf


"""
name:word_in_file_num
input:texts  [list]  所有文本  ,word   [str]  要查的词
统计出现某词的文档的个数
output:num  [int] 
"""
def word_in_file_num(texts,word):
    num = 0
    for text in texts:
        if text.count(word) >= 1:
            num += 1
    return num


def compute_idf(texts,word,Dict_full):
    idf = math.log(len(texts) / Dict_full[word])
    return idf



def compute_df(texts,Dict):
    Dict_full = dict()
#    i = 0
    for word in Dict:
#        print ("word_tf " ,i)
#        i += 1
        df = word_in_file_num(texts,word) 
        Dict_full[word] = math.log(len(texts) / df)
        
    return Dict_full



def compute_tf_idf(Dict,texts,Dict_full):
    print ("计算TF-IDF")
    star = time.time()
    vectors = []
    for text in texts:
        vector = []
        for word in Dict:
            tf = compute_tf(text,word)
            idf = Dict_full[word]
            tf_idf = tf * idf
            #tf_idf = int(tf_idf+0.5)
            vector.append(tf_idf)
        vectors.append(vector)
    end = time.time()
    print (end-star)
    print ("计算TF-IDF____OK")

    return vectors


texts,label =  read_text( "E:\\Tweets.txt")
text_1 = process_text(texts)
dict_1 = build_dict(text_1)  
Dict_full = compute_df(text_1,dict_1)

vec = compute_tf_idf(dict_1,text_1,Dict_full)

X = np.array(vec, dtype=float)
y = np.array(label)
k = len(set(label))



"""
name:kmeans_my
K-Means
"""
def kmeans_my(k,X,labels):
    clustering = KMeans(n_clusters=k).fit_predict(X)
    print (metrics.normalized_mutual_info_score(labels,clustering))
    
    
"""
name:AffinityPropagation
AffinityPropagation
"""
def affinitypropagation_my(X, labels):
    clustering = AffinityPropagation().fit_predict(X)
    print (metrics.normalized_mutual_info_score(labels,clustering))


"""
name:Mean-shift
Mean-shift
"""
def mean_shift_my(X, labels):
    clustering = MeanShift().fit_predict(X)
    print (metrics.normalized_mutual_info_score(labels,clustering))



"""
name:Spectral clustering
Spectral clustering
"""
def spectral_my(X, y, labels):
    clustering = SpectralClustering().fit_predict(X)
    print (metrics.normalized_mutual_info_score(labels,clustering))

"""
name:Ward hierarchical clustering
Ward hierarchical clustering
"""
def hierarchical_my(X, y, labels):
    clustering = AgglomerativeClustering(n_clusters=k).fit(X)
    print (metrics.normalized_mutual_info_score(labels,clustering.labels_))

"""
name:DBSCAN
DBSCAN
"""
def dbscan_my(X, labels):
    clustering = DBSCAN(eps=0.5).fit_predict(X)
    print (metrics.normalized_mutual_info_score(labels,clustering))

"""
name:Gaussian mixtures
Gaussian mixtures
"""
def gaussian_my(X, y, labels):
    clustering = GaussianMixture(n_components=k,covariance_type='diag').fit(X)
    clustering_labels_ = clustering.predict(X)
    print (metrics.normalized_mutual_info_score(labels,clustering_labels_))


print ("kmeans")
begin = time.time()
kmeans_my(k,X,label)
print (time.time() - begin)
print ("AffinityPropagation")
begin = time.time()
affinitypropagation_my(X, label)
print (time.time() - begin)
print ("Mean-shift")
begin = time.time()
mean_shift_my(X, label)
print (time.time() - begin)
print ("Spectral clustering")
begin = time.time()
spectral_my(X, y, label)
print (time.time() - begin)
print ("Ward hierarchical clustering")
begin = time.time()
hierarchical_my(X, y, label)
print (time.time() - begin)
print ("DBSCAN")
begin = time.time()
dbscan_my(X, label)
print (time.time() - begin)
print ("Gaussian mixtures")
begin = time.time()
gaussian_my(X, y, label)
print (time.time() - begin)