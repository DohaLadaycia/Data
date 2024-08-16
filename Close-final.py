import math
def regle(item):
    for i in range (len(item)):
        it=frozenset({(item[i])})
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
#exemple:
"""data=[['A','B','C','D','E'],
      ['A','B'],
      ['C','E'],
      ['A','B','D','E'],
      ['A','C','D']]"""
init=[]
for i in data:
    for q in i:
        if(q not in init):
            init.append(q)
init = sorted(init)
lent=len(data)
from collections import Counter
c = Counter()
min=1
max=0
indice={}
for i in init:
    indi=0
    ind=[]
    for d in data:
        if(i in d):
            c[frozenset([i])]+=1
            ind.append(indi)
        indi=indi+1
    ind=','.join(str(x) for x in ind)
    indice[frozenset([i])]=ind
    c[frozenset([i])]=c[frozenset([i])]/lent
    if c[frozenset([i])]>max :
        max=c[frozenset([i])]
    if c[frozenset(i)]<min:
        min=c[frozenset([i])]
"""if choix==0:
    s=(max+min)/4
if choix==1:
    s=math.sqrt(max*max+min*min)/4
if choix==2:
    s=(max*max+min*min)/4"""
# exemple:
s=math.sqrt(max*max+min*min)/4
print(s)
l = Counter()
close_ferm=Counter
close={}
for i in c:
    if(c[i] >= s):
        l[i]+=c[i]
pl = l
pos = 1
print("Result: ")
ple=[]
for count in range (2,2000):
    nc = set()
    temp = list(l)
    temp1=list(l)
    close_ferm=Counter()
    for i in range(0,len(temp1)):
        close[temp1[i]]=temp1[i]
        for j in range(0,len(temp1)):
            clos=True
            for indice_i in indice[temp1[i]]:
                if indice_i not in indice[temp1[j]]:
                    clos=False
            if ((clos or indice[temp1[i]]==indice[temp1[j]]) and temp1[i]!=temp1[j]):
                tempj=list(temp1[j])
                for k in range (len(temp1[j])):
                   close[temp1[i]]=close[temp1[i]].union([tempj[k]])
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if ((t.issubset(close[temp[j]]) or t.issubset(close [temp[i]]))):
                if (c[temp[i]]>=s and(t==(close[temp[j]]) or t==(close [temp[i]]))):
                  close_ferm[t]=str(temp[i])+','+str(temp[j])
            elif(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = Counter()
    #print(close_ferm)
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
        indice[i]=ind
        c[i]=c[i]/lent
    l = Counter()
    for i in c:
        if(c[i] >= s):
            l[i]+=c[i]
    if(len(l) == 0 and len(close_ferm)==0):
        break
    pl = close_ferm
    pos = count
    #print("L"+str(pos)+":")
    for i in pl:
      print(str(list(i)))
      #regle(0.9,pl[i],list(i))
    print()
