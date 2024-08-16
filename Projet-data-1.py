import math
def confiance(minconf,rule1,rule2):
    res=rule1/rule2
    if res<minconf:
        return False
    else:
        return True
def regle(minconf,rule1,item):
    for i in range (len(item)):
        it=frozenset({(item[i])})
        rule2=pl1[it]
        if (minconf<=confiance(minconf,rule1,rule2)):
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
                   it=frozenset({(ite[0])})
                   for i in range(len(ite)-1):
                      it=it.union({ite[i+1]})
                      rule2=ple[len(item)-3]
                      rule2=rule2[it]
                   if (minconf<=confiance(minconf,rule1,rule2)):
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
min=1
max=0
for i in init:
    for d in data:
        if(i in d):
            c[i]+=1
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
s=(max*max+min*min)/4
print(s)
l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]
pl = l
pl1=pl
pos = 1
print("Result: ")
ple=[]
for count in range (2,2000):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        for q in data:
              temp = set(q)
              if(i.issubset(temp)):
                c[i]+=1
        c[i]=c[i]/lent
    l = Counter()
    for i in c:
        if(c[i] >= s):
            l[i]+=c[i]
    if(len(l) == 0):
        break
    pl = l
    pos = count
    #print("L"+str(pos)+":")
    for i in pl:
      #print(str(list(i))+": "+str(pl[i])) 
      regle(0.9,pl[i],list(i))
    ple.append(pl)
    print()

