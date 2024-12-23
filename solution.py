import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate a dataset with 4 clusters
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Set the number of clusters
k = 4
kmeans = KMeans(n_clusters=k, random_state=0)

# Fit the model to the data and predict clusters
y_kmeans = kmeans.fit_predict(X)

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Plotting the centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroids')

plt.title(f'K-means Clustering with k={k}')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
