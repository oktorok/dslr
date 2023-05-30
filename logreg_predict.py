#!/usr/bin/env python

import pandas
import sys
from describe import describe
import numpy as np
import MyLogisticRegression as LR
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--features', help='Which features do you want to use')
parser.add_argument('--data', type=str, required=True, help='Path to data')
parser.add_argument('--weights', type=str, required=True, help='Path to weights')
args = parser.parse_args()

def normalize_data(df):
    for c in df.columns: #Normalize data
        describe_df = describe(df, [c])
        m = describe_df.loc['mean'][0]
        std = describe_df.loc['std'][0]
        df[c] = df[c].apply(lambda x: (x - m)/std)
    return df

def prepare_data(dataset):
    labels = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']
    if args.features:
        features = args.features.split(',')
    else:
        features = dataset.columns[6:]
    test_df = dataset[features].fillna(0)
    test_df = normalize_data(test_df)
    test = test_df.to_numpy()
    X = np.ones(shape=(test.shape[0], test.shape[1] + 1))
    X[:, 1:] = test
    return (X, labels)

def get_theta_from_file(filename):
    with open(filename, "r") as f:
        weights = f.read()
    theta = np.zeros(shape=(len(labels), X.shape[1]))
    for idx1, label_weights in enumerate(weights.strip().split("\n")):
        for idx2, w in enumerate(label_weights.strip().split(" ")):
            theta[idx1][idx2] = w
    return theta

if __name__ == "__main__":
    if args.data and args.weights:
        dataset = pandas.read_csv(args.data)
        X, labels = prepare_data(dataset)
        theta = get_theta_from_file(args.weights)
        lr = LR.mylogisticregression()
        y = lr.predict(X, theta)
        data = {
            "Hogwarts House":[]
        }
        for i in y:
            data['Hogwarts House'].append(labels[i])
        houses = pandas.DataFrame(data)
        houses.to_csv("houses.csv", index_label="Index")
