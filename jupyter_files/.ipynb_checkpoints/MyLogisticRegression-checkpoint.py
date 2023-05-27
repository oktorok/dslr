#!/usr/bin/ python
import numpy as np
from sklearn.metrics import accuracy_score
from MyGradientDescendent import mygradientdescendent

class mylogisticregression:
    def __init__(self, gradientdescendent=None):
        self.gd = gradientdescendent
        if not gradientdescendent:
            self.gd = mygradientdescendent(self._cost, self._gradient, self._sigmoid)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-1 * x))

    def _cost(self, predictions, y):
        if not isinstance(predictions, np.ndarray):
            if predictions == 1:
                predictions = 0.999
        else:
            predictions[predictions == 1] = 0.999
        if not isinstance(y, np.ndarray):
            m = 1
        else:
            m = len(y)
        error = -y * np.log(predictions) - (1 - y) * np.log(1 - predictions)
        if not isinstance(error, np.ndarray):
            return error / m
        return sum(error) / m

    def _gradient(self, X, predictions, y):
        if not isinstance(y, np.ndarray):
            m = 1
        else:
            m = len(y)
        return X.T.dot(predictions - y) / m

    def fit(self, X, y):
        x = np.array(X)
        self.y = np.array(y)
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y sets have not the same length")
        self.X = np.ones(shape=(x.shape[0], x.shape[1] + 1))
        self.X[:, 1:] = x

    def train(self, numlabels, iterations=50, alpha=0.1, initial_theta=None, gd_mode=None, batch_size=5, tolerance=0.005):
        self.classifiers = np.zeros(shape=(numlabels, self.X.shape[1]))
        if not gd_mode:
            gd_mode = "gd"
        if not initial_theta:
            self.initial_theta = np.zeros(shape=(numlabels, self.X.shape[1]))
        else:
            initial_theta = np.array(initial_theta)
            if initial_theta[0] != self.X.shape[0]:
                raise ValueError("X and initial_theta have not the same length")
        for c in range(0, numlabels):
            label = (self.y == c).astype(int)
            if gd_mode == "gd":
                self.classifiers[c, :] = self.gd.gd(X=self.X, theta=self.initial_theta[c], y=label, alpha=alpha, iterations=iterations, tolerance=tolerance)
            elif gd_mode == "sgd":
                self.classifiers[c, :] = self.gd.sgd(X=self.X, theta=self.initial_theta[c], y=label, alpha=alpha, iterations=iterations, tolerance=tolerance)
            elif gd_mode == "sgdmb":
                self.classifiers[c, :] = self.gd.sgdmd(X=self.X, theta=self.initial_theta[c], y=label, alpha=alpha, iterations=iterations, batch_size=batch_size)

    def get_accuracy(self, hypothesis=None):
        if not hypothesis:
            hypothesis = self._sigmoid
        elif not callable(hypothesis):
            raise TypeError("hypothesis must be a callable function")
        classProbabilities = hypothesis(self.X.dot(self.classifiers.T))
        predictions = classProbabilities.argmax(axis=1)
        return accuracy_score(self.y, predictions)
    
    def predict(self, X, theta=None, hypothesis=None):
        if not isinstance(theta, np.ndarray) and not theta:
            theta = self.classifiers
        if not hypothesis:
            hypothesis = self._sigmoid
        elif not callable(hypothesis):
            raise TypeError("hypothesis must be callable")
        theta = np.array(theta)
        probs = hypothesis(X.dot(theta.T))
        predictions = probs.argmax(axis=1)
        return predictions