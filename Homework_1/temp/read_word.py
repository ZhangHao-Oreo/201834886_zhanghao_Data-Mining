# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:14:12 2018

@author: zh_lab
"""

#读文件
f = open('E:\mytest.txt','r',errors='ignore')
text = f.read()
#str(text, encoding = "utf-8")
text = text.replace('\r','').replace('\n','').replace('\t','')
#text.replace("\n","")
f.close()


import os

def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)






import nltk
import string
import math
from textblob import TextBlob
from textblob import Word
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *
#from sklearn.feature_extraction.text import TfidfVectorizer




def get_tokens(text):
    lowers = text.lower()   #大小写
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tf(word, count):
    return count[word] / sum(count.values())

def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)




#规则化全文
#context = TextBlob(text)

#tokens = get_tokens(text)
#count = Counter(tokens)
#print (count.most_common(10))
#tokens = get_tokens(text)
#filtered = [w for w in tokens if not w in stopwords.words('english')]
#count = Counter(filtered)
#print (count.most_common(10))
tokens = get_tokens(text3)
filtered = [w for w in tokens if not w in stopwords.words('english')]
stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count3 = Counter(stemmed)
#print (count.most_common(10))
#count1 = Counter(stemmed)
#print(count)


countlist = [count1, count2, count3]
for i, count in enumerate(countlist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, count, countlist) for word in count}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
countlist=[]
i = 0
for fullname in iterbrowse("E:\\20news-18828"):
    #fullname是绝对路径
    #print fullname 
    filename=os.path.basename(fullname)
    #filename是目录下的所有文件名
    print (filename)
    f = open(fullname,'r',errors='ignore')
    text = f.read()
    text = text.replace('\r','').replace('\n','').replace('\t','')
    f.close()
    tokens = get_tokens(text)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    locals()['count%d'%i] = Counter(stemmed)
    countlist.insert(i,locals()['count%d'%i])
    i=i+1
 #   print(count)



for i, count in enumerate(countlist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, count, countlist) for word in count}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
