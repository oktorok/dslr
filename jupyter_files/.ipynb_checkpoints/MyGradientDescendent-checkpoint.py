#!/usr/bin/ python
import numpy as np
import random

class mygradientdescendent:
    def __init__(self, cost, gradient, hypothesis):
        if not callable(cost):
            raise TypeError("cost must be a callable function")
        if not callable(gradient):
            raise TypeError("gradient must be a callable function")
        if not callable(hypothesis):
            raise TypeError("hypothesis must be a callable function")
        self.cost = cost
        self.gradient = gradient
        self.h = hypothesis

    def gd(self, X, theta, y, alpha=0.1, iterations=100, tolerance=0.005):
        for iteration in range(iterations):
            predictions = self.h(X.dot(theta))
            total_error = self.cost(predictions, y)
            gradient = self.gradient(X, predictions, y)
            diff = -alpha * gradient
            if np.all(np.abs(diff) <= tolerance):
                break
            theta += diff
        return theta

    def sgd(self, X, theta, y, alpha=0.1, iterations=100, tolerance=0.05):
        for iteration in range(iterations):
            random_idx = random.sample(range(0, X.shape[0]), 1)[0]
            predictions = self.h(X[random_idx].dot(theta))
            total_error = self.cost(predictions, y[random_idx])
            gradient = self.gradient(X[random_idx], predictions, y[random_idx])
            diff = -alpha * gradient
            if np.all(np.abs(diff) <= tolerance):
                break
            theta += diff
        return theta

    def sgdmb(self, X, theta, y, alpha=0.1, iterations=100, tolerance=0.005, batch_size=5):
        for iteration in range(iterations):
            random_idx = random.sample(range(0, X.shape[0]), batch_size)[0]
            predictions = self.h(X[random_idx].dot(theta))
            total_error = self.cost(predictions, y)
            gradient = self.gradient(X[random_idx], predictions, y[random_idx])
            diff = -alpha * gradient
            if np.all(np.abs(diff) <= tolerance):
                break
            theta += diff
        return theta

