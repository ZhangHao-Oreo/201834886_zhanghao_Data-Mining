# -*- coding: utf-8 -*-
"""

Created on Wed Oct 17 21:39:42 2018

@author: zh_lab
"""

"""
KNN 
对文档加标签存到矩阵中
"""

#--------使用的库----------
import sys 
sys.path.append('C:\\Users\\zh_lab\\Documents\\GitHub\\201834886_zhanghao_Data-Mining\\Homework_1\\vsm') 
import vsm 
import numpy as np
#from scipy.spatial.distance import pdist



dirs_path = "E:\\20news-18828"
file_dir_train = "E:\\data_set_1\\train_set"
file_dir_test = "E:\\data_set_1\\test_set"
file_w = 0.5

"""
dirs_path = "E:\\data_set_1\\train_set"
file_dir_train = "E:\\data_set_2\\train_set"
file_dir_test = "E:\\data_set_2\\test_set"
file_w = 0.7


dirs_path = "E:\\data_set_2\\test_set"
file_dir_train = "E:\\data_set_3\\train_set"
file_dir_test = "E:\\data_set_3\\test_set"
file_w = 0.7

"""

tmp_texts = "E:\\real\\Texts.csv"
tmp_label = "E:\\real\\Label.csv"
tmp_Dict = "E:\\real\\Dict.csv"
tmp_TF_IDF = "E:\\real\\TF_IDF.csv"
tmp_Label_test = "E:\\real\\Label_test.csv"
tmp_Texts_test = "E:\\real\\Tests_test.csv"
tmp_TF_IDF_test = "E:\\real\\TF_IDF_test.csv"
tmp_Dict_full = "E:\\real\\Dict_DF.csv"

                
Dict = []
Texts = []
Label = []
Vectors_TF_IDF = []
Vectors_TF_IDF_test = []
Dict_idf = []
Texts_test = []
Label_test = []
Dict_full = []
Knn_out = []

"""
欧几里得距离(Euclidean Distance)
"""
def Euclidean_Distance(x,y):    
# solution1
    dist = np.linalg.norm( x - y ) 
# solution2
    #dist = np.sqrt(np.sum(np.square(x - y))) 
    return dist


"""
余弦距离
"""
def Cosine_Distance(x,y):     
    # solution1
    dist = 1 - np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))    
    # solution2
    #dist = pdist(np.vstack([x,y]),'cosine')
    return dist




def compute_tf_idf_test(Dict,texts,Dict_full):
    print ("计算测试集 TF-IDF")
    #star = time.time()
    vectors = []
    for text in texts:
        vector = []
        for word in Dict:
            tf = vsm.compute_tf(text,word)
            idf = Dict_full[word]
            tf_idf = tf * idf
            tf_idf = int(tf_idf+0.5)
            vector.append(tf_idf)
        vectors.append(vector)
    #end = time.time()
    #print (end-star)
    print ("计算测试集TF-IDF____OK")
    return vectors




def knn(train, train_label, test,k = 30):
#    print("KNN")
    tmp_list = []
    i = 0
    for train_v in train:
        dist = Cosine_Distance(test,train_v)
        tmp_list.append([Label[i],dist])
        i += 1
    tmp_list = sorted(tmp_list, key=lambda x: x[1], reverse=False)
    tmp_list = tmp_list[0:k]    
    Dict_list = []
    for i in range(len(tmp_list)):
        tmp_list[i][0]
        if tmp_list[i][0] not in Dict_list:
            Dict_list.append(tmp_list[i][0])
    top_label = Dict_list[0]
    top_num = 0
    for Dict_list_i in Dict_list:
        if tmp_list.count(Dict_list_i) > top_num:
            top_label = Dict_list_i
    return top_label


        
"""
train = []
train_label = []
test = []
test_label = []
train[0:20] = Vectors_TF_IDF [0:20]
train_label[0:20] = Label [0:20]
test = Vectors_TF_IDF [15:25]
test_label[0:20] = Label [15:25]
"""



def judge_dataset(train, train_label, test,test_label):
    knn_out = []
    num_test = 0
    for test_i in test:
        print (num_test)
        tmp_label_knn = knn(train, train_label, test_i,k = 30)
        knn_out.append(tmp_label_knn)   
        num_test += 1
    if len(test_label) == len(knn_out):
        error_num = 0
        for i in range(len(test_label)):
            if test_label[i]!=knn_out[i]:
                error_num += 1
                i += 1
            else:
                i += 1
        print ("正确率 = ",(1-(error_num/len(test_label))))
        return (1-(error_num/len(test_label))) ,knn_out
    else:
        print ("计算错误_!!!!!!!!!")
        return 2,knn_out

if __name__ == '__main__':


    
#划分数据集
#    init_set(dirs_path,file_w)    
#规则化每个文本
    Texts,Label = vsm.travel_all_file(file_dir_train)
    vsm.record ("path","Label",Label)
    vsm.record ("path","Texts",Texts)
#    Texts = read_csv(tmp_texts)
#    Label = read_csv(tmp_label)
#    Label = vsm.process_str(Label)    
#建立词典
    Dict = vsm.travel_all_file_build_dict(Texts)
    vsm.record ("path","Dict",Dict)
#    Dict = vsm.read_csv(tmp_Dict)
#    Dict = vsm.process_str(Dict)
#计算TF-IDF
    Dict_full = vsm.compute_df(Texts,Dict)
    vsm.record (tmp_Dict_full,"Other",Dict_full)
#    Dict_full = read_csv(tmp_Dict_full)   
    Vectors_TF_IDF = vsm.compute_tf_idf(Dict,Texts,Dict_full)
    vsm.record ("path","TF_IDF",Vectors_TF_IDF)
#    Vectors_TF_IDF = read_csv(tmp_TF_IDF)
#规则话测试集
    Texts_test,Label_test = vsm.travel_all_file(file_dir_test) 
    vsm.record ("path","Texts_test",Texts_test)
    vsm.record ("path","Label_test",Label_test)
#    Texts_test = read_csv(tmp_Texts_test)
#    Label_test = read_csv(tmp_Label_test)
#    Label_test = vsm.process_str(Label)
#计算test_TF_IDF
    Vectors_TF_IDF_test = compute_tf_idf_test(Dict,Texts_test,Dict_full)
    vsm.record (tmp_TF_IDF_test,"Other",Vectors_TF_IDF_test)
#    Vectors_TF_IDF_test = read_csv(tmp_TF_IDF_test)

#KNN
    Correct,Knn_out = judge_dataset(Vectors_TF_IDF, Label,Vectors_TF_IDF_test,Label_test)

