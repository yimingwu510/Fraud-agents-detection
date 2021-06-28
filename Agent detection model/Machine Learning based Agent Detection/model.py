import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
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

file_p=open(r"C:\Users\wuyiming\Desktop\fa\code\agent_300k.txt",'r') #positive samples
file_n=open(r"C:\Users\wuyiming\Desktop\fa\code\other_borrowers.txt",'r') # negative samples
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
    for j in range(len(tests[i])):
        test_label.append(tests[i][j].split("||")[0])
        test_feature.append(tests[i][j].split("||")[2])


    test_labels.append(test_label)
    test_features.append(test_feature)


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
                f1.append(k)
        x_train.append(f1)
        y_train.append(train_labels[i][j])
        #print("&&",x_train)

    f = []
    for j in range(len(test_features[i])):
        f = test_features[i][j].split(" ")
        l = test_labels[i][j].split(" ")
        f1 = []
        l1 = []
        for k in f:
            if len(k) > 0:
                f1.append(k)
        x_test.append(f1)
        y_test.append(test_labels[i][j])


    clf = RandomForestClassifier(random_state=5)
    model = clf.fit(x_train, y_train)
    print(model.predict(x_test))

