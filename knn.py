from sklearn.base import BaseEstimator,ClassifierMixin
import scipy
import numpy as np

class kNN(BaseEstimator, ClassifierMixin):
    def __init__(self, n_neighbors:int = 3):
        self.n_neighbors = n_neighbors
    def fit(self, X, y):
        # TODO: complete
        self.X = np.copy(X)
        self.y = np.copy(y)
        return self
    def predict(self, X):
        # Note: You can use self.n_neighbors here
        predictions = None
        # TODO: compute the predicted labels (+1 or -1)
        dist_mat = scipy.spatial.distance.cdist(XA=X, XB=self.X)
        sort_dist_idx = np.argpartition(a=dist_mat, kth=self.n_neighbors, axis=1)
        pred_sum = np.sum(self.y[sort_dist_idx][:, 0:self.n_neighbors], axis=1)
        predictions = np.where(pred_sum>0, 1, -1)
        return predictions