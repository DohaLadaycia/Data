import numpy as np
from sklearn.cluster import KMeans

# Générer des données aléatoires
X = np.random.rand(100, 2)

# Appliquer l'algorithme K-means
kmeans = KMeans(n_clusters=3)
print(X)
kmeans.fit([[1.25, 1.2], [1.0, 0.6]
[5.0, 8.0]
[1.0, 2.0]
[8.0, 8.0], [9.0, 11.0]])

# Obtenir la distance inter-cluster (inertie)
distance = kmeans.inertia_
print(distance)