import math
import random
def choix_de_k(seuil,data):
    clusters=[]
    choix=random.choice(data)
    clusters.append(choix)
    for i in range (len(data)-2):
        min_dis=math.inf
        data.remove(choix)
        data1=data
        choix=random.choice(data1)
        for cluster in clusters:
            distances=0
            for j in range(len(cluster)):
               distances=distances+abs(cluster[j]-choix[j])
            if distances<min_dis:
                min_dis=distances
                min_cluster=cluster
        if min_dis<seuil:
            c=clusters.index(min_cluster)
            for j in range(len(cluster)):
               clusters[c][j]=(clusters[c][j]+choix[j])/2
        else:
            clusters.append(choix)
    return len(clusters)
def distance(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5
def assigner_points_aux_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = [distance(point, centroid) for centroid in centroids]
        closest_centroid_index = distances.index(min(distances))
        clusters[closest_centroid_index].append(point)
    return clusters
def recalculer_centroids(clusters):
    return [list(map(lambda x: sum(x) / len(x), zip(*cluster))) for cluster in clusters]
def k_means(data, k, max_iterations=100):
    centroids = random.sample(data, k)
    for _ in range(max_iterations):
        clusters = assigner_points_aux_clusters(data, centroids)
        new_centroids = recalculer_centroids(clusters)
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters, centroids
file=open('ex-data.txt')
lignes=file.readlines()
data=[]
l=0
for ligne in lignes:
    l=l+1
    ligne =ligne.split(",")
    for i in range(len(ligne)):
        ligne[i]=float(ligne[i].strip("\n"))
    data.append(ligne)
# Exemple d'utilisation
data1=data.copy()
print(data)
c=input('Voulez vous automatiser le seuil?(1 pour oui ,0 Sinon): ')
if int(c)==0:
#data=[[1,2], [2,3],[4,7],[8,10]]
   k=input('Donnez moi le seuil de clusters: ')
   nb= choix_de_k(int(k),data1)
else:
    nb=0
    minl=min(data)
    sec_min=sorted(data)
    sec_min =sec_min[1]
    min_dis=0
    for i in range(len(minl)):
        min_dis=min_dis+(sec_min[i]-minl[i])
    for i in range(len(data)-1):
        for j in range(len(data[0])):
          nb=nb+abs((data[i][j]-data[i+1][j]))
        nb=(nb-min_dis)/2
    nb=int(nb/len(data))
    if nb>len(data):
        nb=len(data)
print(nb)
centroids, clusters_m = k_means(data,nb)
print("Centroides finaux :")
for centroid in centroids:
    print(centroid)
print("\nClusters :")
for i, cluster_m in enumerate(clusters_m):
    print("Cluster", i+1, ":")
    for point in cluster_m:
        print(point)
