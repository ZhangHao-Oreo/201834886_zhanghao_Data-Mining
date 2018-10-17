# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:14:12 2018

@author: zh_lab
"""

from textblob import TextBlob
from textblob import Word
wiki = TextBlob("Python is a high-level, general-purpose programming language.In the bin packing problem, objects of different volumes must be packed into a finite number of bins or containers each of volume V in a way that minimizes the number of bins used. In computational complexity theory, it is a combinatorial NP-hard problem.[1] The decision problem (deciding if objects will fit into a specified number of bins) is NP-complete.[2] There are many variations of this problem, such as 2D packing, linear packing, packing by weight, packing by cost, and so on. They have many applications, such as filling up containers, loading trucks with weight capacity constraints, creating file backups in media and technology mapping in Field-programmable gate array semiconductor chip design. The bin packing problem can also be seen as a special case of the cutting stock problem. When the number of bins is restricted to 1 and each item is characterised by both a volume and a value, the problem of maximising the value of items that can fit in the bin is known as the knapsack problem. Despite the fact that the bin packing problem has an NP-hard computational complexity, optimal solutions to very large instances of the problem can be produced with sophisticated algorithms. In addition, many heuristics have been developed: for example, the first fit algorithm provides a fast but often non-optimal solution, involving placing each item into the first bin in which it will fit. It requires Θ(n log n) time, where n is the number of elements to be packed. The algorithm can be made much more effective by first sorting the list of elements into decreasing order (sometimes known as the first-fit decreasing algorithm), although this still does not guarantee an optimal solution, and for longer lists may increase the running time of the algorithm. It is known, however, that there always exists at least one ordering of items that allows first-fit to produce an optimal solution.[3] A variant of bin packing that occurs in practice is when items can share space when packed into a bin. Specifically, a set of items could occupy less space when packed together than the sum of their individual sizes. This variant is known as VM packing[4] since when virtual machines (VMs) are packed in a server, their total memory requirement could decrease due to pages shared by the VMs that need only be stored once. If items can share space in arbitrary ways, the bin packing problem is hard to even approximate. However, if the space sharing fits into a hierarchy, as is the case with memory sharing in virtual machines, the bin packing problem can be efficiently approximated. Another variant of bin packing of interest in practice is the so-called online bin packing. Here the objects of different volume are supposed to arrive sequentially and the decision maker has to decide whether to select and pack the currently observed item, or else to let it pass. Each decision is without recall.")
set1 = set(wiki.words)
set4 = set("")
set1 = set(["apples","feet","zhanghao","loves"])
for d in set1:
   # print (d)
    w = Word(d)
    w.lemmatize()
    print (w)
    set4.add(w)







w = Word("feet","lists")
w.lemmatize()


from nltk.corpus import stopwords
set2 = set([stopwords.words('english')])
set3 = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

for d in set3:
    print (d)
