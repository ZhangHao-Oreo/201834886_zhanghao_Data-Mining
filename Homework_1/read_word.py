# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:14:12 2018

@author: zh_lab
"""
import nltk
import string
from textblob import TextBlob
from textblob import Word
from collections import Counter
from nltk.corpus import stopwords

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

#读文件
f = open('E:\mytest.txt','r',errors='ignore')
text = f.read()
#str(text, encoding = "utf-8")
text = text.replace('\r','').replace('\n','').replace('\t','')
#text.replace("\n","")
f.close()

#规则化全文
context = TextBlob(text)

tokens = get_tokens(text)
count = Counter(tokens)
print (count.most_common(10))
tokens = get_tokens(text)
filtered = [w for w in tokens if not w in stopwords.words('english')]
count = Counter(filtered)
print (count.most_common(10))


for d in tokens:
   # print (d)
    w = Word(d)
    print (w)
    set4.add(w.lemmatize())
