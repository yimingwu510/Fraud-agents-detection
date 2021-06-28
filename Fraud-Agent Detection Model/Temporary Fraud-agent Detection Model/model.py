import pandas as pd
import numpy as np
import xgboost as xgb
import pickle
import random
import random
import os
import math
import numpy as np

def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

def txt2list(array):
    arrayb=[]
    for i in array:
        arrayb.append(i.strip("\n"))
    return arrayb


file_p=open(r"Fraud-agents-detection/Fraud-Agent Detection Model/Temporary Fraud-agent Detection Moderl/groundtruth.txt",'r') 
# positive samples - groundtruth. 3326 fraud-agents
file_n=open(r"Fraud-agents-detection/Fraud-Agent Detection Model/Temporary Fraud-agent Detection Moderl/all_agents.txt",'r') 
# negative samples - all detected agents. 300k agents
file_result=open(r"Fraud-agents-detection/Fraud-Agent Detection Model/Temporary Fraud-agent Detection Moderl/expanded_agents.txt",'w')
p_lines=file_p.readlines()
n_lines=file_n.readlines()

p_lines=txt2list(p_lines)
n_lines=txt2list(n_lines)

len_p=len(p_lines)
len_n=len(n_lines)
m=math.ceil(len_n/len_p)

random.shuffle(n_lines)

negative=[]
m1=1
negatives = list_split(n_lines, len_p)


slices=[]
tests=[]
for i in range(len(negatives)):
    slice=[]
    slice=p_lines+negatives[i]
    slices.append(slice)
    test = []
    for j in range(len(negatives)):
        if i!=j:
            for k in range(len(negatives[j])):
                test.append(negatives[j][k])
    tests.append(test)
#print(slices)

train_labels=[]
train_features=[]
test_labels=[]
test_features=[]
test_phones=[]
for i in range(len(slices)):
    train_label=[]
    train_feature=[]
    for j in range(len(slices[i])):
        train_label.append(slices[i][j].split("||")[0])
        train_feature.append(slices[i][j].split("||")[2])

    train_labels.append(train_label)
    train_features.append(train_feature)

for i in range(len(tests)):
    test_label = []
    test_feature = []
    test_phone=[]
    for j in range(len(tests[i])):
        test_label.append(tests[i][j].split("||")[0])
        test_feature.append(tests[i][j].split("||")[2])
        test_phone.append(tests[i][j].split("||")[1])


    test_labels.append(test_label)
    test_features.append(test_feature)
    test_phones.append(test_phone)

params = {
    'n_estimators': 100,
    'colsample_bytree': 0.8,
    'max_depth': 7,
    'min_child_weight': 1,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'num_class': 2,
    'eta': 0.2
}

for i in range(len(train_features)):
    f=[]
    x_train=[]
    y_train=[]
    x_test = []
    y_test = []
    for j in range(len(train_features[i])):
        f=train_features[i][j].split(" ")
        l=train_labels[i][j].split(" ")
        f1 = []
        l1=[]
        for k in f:
            if len(k)>0:
                f1.append(int(k))
        x_train.append(f1)
        y_train.append(int(train_labels[i][j]))
        #print("&&",x_train)

    f = []
    p_test=[]
    for j in range(len(test_features[i])):
        f = test_features[i][j].split(" ")
        l = test_labels[i][j].split(" ")
        p= test_phones[i][j].split(" ")
        f1 = []
        l1 = []
        for k in f:
            if len(k) > 0:
                f1.append(int(k))
        for o in l:
            if len(o) > 0:
                l1.append(o)
        for t in p:
            if len(t)>0:
                p_test.append(t)
        x_test.append(f1)
        y_test.append(int(test_labels[i][j]))

    print(x_train)
    print(y_train)

    dtrain = xgb.DMatrix(np.array(x_train), np.array(y_train))
    dtest = xgb.DMatrix(np.array(x_test))

    model = xgb.XGBClassifier(
        params=params,
        dtrain=dtrain,
        num_boost_round=500,
        nfold=5,
        early_stopping_rounds=100
    )

    model = xgb.XGBClassifier()
    final_gb = xgb.train(params, dtrain)
   # model.fit(np.array(x_train), np.array(y_train))

  #  dtrain_predprob = alg.predict_proba(dtrain[predictors])[:, 1]
    pre_test = final_gb.predict(dtest)
   # pre_test=model.predict(np.array(x_test))
    print(pre_test.tolist())


    for q in range(len(pre_test.tolist())):
        file_result.write(p_test[q])
        file_result.write(",")
        file_result.write(str(int(pre_test[q])))
        file_result.write("\n")



