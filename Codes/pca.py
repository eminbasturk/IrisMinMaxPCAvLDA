  
import numpy as np

class PCA:

    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # 1- Ortalamayı merkezleme
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        # 2- Kovaryans değerinin hesaplanması
        cov = np.cov(X.T)
        # 3- Özvektörler ve özdeğerler
        ozdegerler, ozvektorler = np.linalg.eig(cov)
        # 4- Sıralama
        ozvektorler = ozvektorler.T
        idxs = np.argsort(ozdegerler)[::-1]
        ozdegerler = ozdegerler[idxs]
        ozvektorler = ozvektorler[idxs]
        # 5- İlk n özvektörünün saklanması
        self.components = ozvektorler[0:self.n_components]

    def transform(self, X):
        # projenin verileri
        X = X - self.mean
        return np.dot(X, self.components.T)
    
    
