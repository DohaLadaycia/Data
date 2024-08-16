#close
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
#s=(max+min)/4
s=(max*max+min*min)/4
print(s)
l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]
pl = l
pos = 1
print("Result: ")
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
    print("L"+str(pos)+":")
    for i in pl:
      print(str(list(i))+": "+str(pl[i]))
      
minconf=0,4
