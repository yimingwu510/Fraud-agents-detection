import os

f_w=open(r"Fraud-agents-detection/Agent detecction model/Rule based Agent Detection/1-address book-lcs.txt",'w',encoding="utf-8")

def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  
    mmax = 0  
    p = 0  
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax  

with open(r"Fraud-agents-detection/Agent detecction model/Rule based Agent Detection/1-address book.txt",'r',encoding="utf-8") as f:
    lines=f.readlines()
    remarks=[]
    ls=[]
    for i in range(1,len(lines)):
        remarks.append(lines[i].split("||")[1])
    for i in remarks:
        for j in remarks:
            if i!=j:
                l=(find_lcsubstr(i,j))[0]
                l=l.replace(" ","")
                if len(l)>0:
                    ls.append(l)
    lsset=set(ls)
    for i in lsset:
        c=0
        for j in lines:
            if i in j:
                c=c+1
        if c>10:
            print(i)
            f_w.write(i)
            f_w.write("\n")
