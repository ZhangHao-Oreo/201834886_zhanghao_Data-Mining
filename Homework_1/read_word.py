# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:14:12 2018

@author: zh_lab
"""


f = open('E:\mytest.txt','r',errors='ignore')
text = f.read()
#str(text, encoding = "utf-8")
text = text.replace('\r','').replace('\n','').replace('\t','')
#text.replace("\n","")
f.close()










from textblob import TextBlob
from textblob import Word
wiki = TextBlob(text)
set1 = set(wiki.words)
set4 = set("")
set1 = set(["apples","feet","pigs","loves"])
for d in set1:
   # print (d)
    w = Word(d)
    print (w)
    set4.add(w.lemmatize())







w = Word("feet")
w.lemmatize()


from nltk.corpus import stopwords
set2 = set([stopwords.words('english')])
set3 = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

for d in set3:
    print (d)
