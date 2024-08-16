import math
def regle(item):
    for i in range (len(item)):
        #print(it)
        print(str(item[i])+'-->'+str(item[0:i]+(item[i+1:len(item)])))
        if len(item)>2:
            j=len(item)-1
            l=i
            while l<len(item)-1 and i<=1:
                k=i
                ite=[]
                while k<len(item):
                    if k!=j:
                        ite.append(item[k])
                    k=k+1
                
                if len(ite)==len(item)-1:
                   print(str(ite)+'-->'+str(item[j]))
                   l=l+1
                j=j-1
file=open('weather.nominal.arff')
lignes=file.readlines()
data=[]
head=[]
l=0
for ligne in lignes:
    l=l+1
    ligne =ligne.split(",")
    for i in range(len(ligne)):
        ligne[i]=ligne[i].strip("\n")
    for i in range(len(ligne)):
        if l==1:
            head.extend(ligne)
        if l>1:
            ligne[i]=head[i]+"="+ligne[i]
    data.append(ligne)
init=[]
for i in data:
    for q in i:
        if(q not in init):
            init.append(q)
init = sorted(init)
lent=len(data)-1
from collections import Counter
c = Counter()
cprec=Counter()
min=1
max=0
indice={}
for i in init:
     
    indi=0
    ind=[]
    for d in data:
        if(i in d):
            c[i]+=1
            ind.append(indi)
        indi=indi+1
    ind=','.join(str(x) for x in ind)
    indice[str(i)]=ind
    c[i]=c[i]/lent
    if c[i]>max :
        max=c[i]
    if c[i]<min:
        min=c[i]
"""if choix==0:
    s=(max+min)/2
if choix==1:
    s=math.sqrt(max*max+min*min)/4
if choix==2:
    s=(max*max+min*min)/4"""
cprec=c
s=s=(max*max+min*min)/4
#s=0.15
print(s)
l = Counter()
for i in c:
    if(c[i] >= s):
        l[str([i])]+=c[i]
pl = l
pos = 1
print("Result: ")
rule1={}
for count in range (2,2000):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i]+(temp[j])
            t=t.replace('[',',')
            t=t.replace(']','')
            t=t[1::]
            print(t)
            if(len(t) == count and  len(temp[i].symmetric_difference(temp[j]))>=count-1):
                nc.add(t)
                lis=list(t)
                k1=str([lis[0]])
                ver=0
                while ver <count:
                   k1=k1.union([lis[i+1]])
                rule1[t]=k1
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        ind=[]
        indi=0
        for q in data:
            temp = set(q)
            if(i.issubset(temp)):
                c[i]+=1
                ind.append(indi)
            indi=indi+1
        ind=','.join(str(x) for x in ind)
        if c[i]!=0:
           indice[i]=ind
        c[i]=c[i]/lent
    l = Counter()
    close=Counter()
    for i in c:
        if(c[i] >= s and  indice[i]!=indice[rule1[i]]):
            l[i]+=c[i]
        elif(c[i] >= s and indice[i]==indice[rule1[i]]):
            close[i]+=c[i]
    if(len(l) == 0):
        break
    pl =close
    pos = count
    for i in pl:
      print(str(list(i))+": "+str(pl[i]))
      #regle(list(i))
    #print()