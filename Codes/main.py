from sklearn import datasets 
import matplotlib.pyplot as plt


# Iris veri setini import etme işlemi
data = datasets.load_iris()
X = data.data
y = data.target


# Minimum - maximum normalizasyon işlemi
X_min_max = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))


fig, axes = plt.subplots(1,2)
axes[0].scatter(X[:,0], X[:,1], c=y)
axes[0].set_title("Gerçek Veri")
axes[1].scatter(X_min_max[:,0], X_min_max[:,1], c=y)
axes[1].set_title("Min-Max Norm. Veri")
plt.show()

# Verileri iki temel bileşen ile gösterme
from pca import PCA
pca = PCA(2)
pca.fit(X_min_max)
X_projected = pca.transform(X_min_max)

print('Min-Max Normalizasyonlu X:', X_min_max.shape) # (150, 4)
print('PCA Uygulanan X:', X_projected.shape) # (150, 2)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

plt.scatter(x1, x2,
        c=y, edgecolor='none', alpha=0.8,
        cmap=plt.cm.get_cmap('viridis', 3))

plt.xlabel('Temel Bileşen 1')
plt.ylabel('Temel Bileşen 2')
plt.colorbar()
plt.show()

# Verileri iki doğrusal diskriminant ile gösterme
from lda import LDA
lda = LDA(2)
lda.fit(X_min_max, y)
X_projected = lda.transform(X_min_max)

print('Min-Max Normalizasyonlu X:', X_min_max.shape) # (150, 4)
print('LDA Uygulanan X:', X_projected.shape) # (150, 2)
 
x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

plt.scatter(x1, x2,
        c=y, edgecolor='none', alpha=0.8,
        cmap=plt.cm.get_cmap('viridis', 3))

plt.xlabel('Doğrusal Diskriminant 1')
plt.ylabel('Doğrusal Diskriminant 2')
plt.colorbar()
plt.show()