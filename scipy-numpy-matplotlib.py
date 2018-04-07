import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

# generate two clusters: a with 100 points, b with 50:
np.random.seed(4711)

a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
X = np.concatenate((a, b),)
print(X.shape) # 150 samples with 2 dimensions
plt.scatter(X[:,0], X[:,1])
#plt.show()

Z = linkage(X,'single') #complete, single, average, cityblock, Euclidean, cosine

# Print the full dendrogram
plt.figure(figsize=(25,10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.show()