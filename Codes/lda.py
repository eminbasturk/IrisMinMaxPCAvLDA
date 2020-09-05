
import numpy as np

class LDA:

    def __init__(self, n_components):
        self.n_components = n_components
        self.linear_discriminants = None

    def fit(self, X, y):
        n_features = X.shape[1]
        class_labels = np.unique(y)

        # 1- SW ve SB değerlerinin hesaplanması
        mean_overall = np.mean(X, axis=0)
        SW = np.zeros((n_features, n_features))
        SB = np.zeros((n_features, n_features))
        for c in class_labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            
            # (4, n_c) * (n_c, 4) = (4,4) -> transpose'unu almak
            SW += (X_c - mean_c).T.dot((X_c - mean_c))

            # (4, 1) * (1, 4) = (4,4) -> reshape'ini almak
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(n_features, 1)
            SB += n_c * (mean_diff).dot(mean_diff.T)

        # 2- SW^-1 * SB denkleminin hesaplanması
        A = np.linalg.inv(SW).dot(SB)
        # Denklemden özdeğerleri ve özvektörleri alma işlemi
        ozdegerler, ozvektorler = np.linalg.eig(A)
        # 3- Sıralama
        ozvektorler = ozvektorler.T
        idxs = np.argsort(abs(ozdegerler))[::-1]
        ozdegerler = ozdegerler[idxs]
        ozvektorler = ozvektorler[idxs]
        # 4- İlk n özvektörünün saklanması
        self.linear_discriminants = ozvektorler[0:self.n_components]

    def transform(self, X):
        # project data
        return np.dot(X, self.linear_discriminants.T)
    
    
    
    