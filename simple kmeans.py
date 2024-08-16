import random
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
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
    # Sélection aléatoire des centroids initiaux
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
#data=[[1,2], [2,3],[4,7],[8,10]]
k=input('Donnez moi le nombre de clusters: ')
centroids, clusters_m = k_means(data,int(k))
print("Centroides finaux :")
for centroid in centroids:
    print(centroid)
print("\nClusters :")
for i, cluster_m in enumerate(clusters_m):
    print("Cluster", i+1, ":")
    for point in cluster_m:
        print(point)