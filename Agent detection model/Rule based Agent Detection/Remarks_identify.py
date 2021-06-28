import os

f_lcs=open(r"Fraud-agents-detection/Agent detecction model/Rule based Agent Detection/1-address book-lcs.txt",'r',encoding="utf-8")
lcs_lines=f_lcs.readlines()

f_w=open(r"Fraud-agents-detection/Agent detecction model/Rule based Agent Detection/2-address book-lcs.txt",'w',encoding="utf-8")

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

with open(r"Fraud-agents-detection/Agent detecction model/Rule based Agent Detection/2-address book.txt",'r',encoding="utf-8") as f:
    lines=f.readlines()
    remarks=[]
    all_remark=[]
    phone=[]
    for i in range(1,len(lines)):
       # print("&&",lines[i])
        lines[i]=lines[i].strip("\n")
        phone.append(lines[i].split("||")[0])
        phone_set=set(phone)
    all_remark=[]
    for j in range(len(phone_set)):
        remarks=[]
        for k in range(len(phone)):
            if list(phone_set)[j]==phone[k]:
                remarks.append(lines[k+1].split("||")[1])
        all_remark.append(remarks)

    ls=[]
    set_remark=[]

    for m in range(len(all_remark)):
        each_phone=[]
        c1 = 0
        c2=0
        ls=[]



        for n in all_remark[m]:
            remark=n
            for k in range(8):
                lcs_lines[k]=lcs_lines[k].strip("\n")
                f=lcs_lines[k].split(" ")[0]
                l=lcs_lines[k].split(" ")[1]
                if f in remark and l in remark:
               # print("**",lines[i],remark, c1)
                    remark=remark.replace(f,"")
                    remark = remark.replace(l, "")
            for k in range(8,98):
                lcs_lines[k]=lcs_lines[k].strip("\n")
                if lcs_lines[k] in remark:
                    c1=c1+1
                    remark= remark.replace(lcs_lines[k], "")
               # print("((", lcs_lines[k], remark, c1)

            if remark==n:
                c2=c2+1
        c1=len(all_remark[m])-c2
        set_remark.append(remark)

        if c1>c2:
           # print(c1,c2,m)
           # print(list(phone_set)[m])
           print(list(phone_set)[m])

