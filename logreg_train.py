#!/usr/bin/python3

import MyLogisticRegression as LR
import pandas
import describe
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--features', type=str, help='Which features do you want to use')
parser.add_argument('--data', type=str, required=True, help='Path to data')
parser.add_argument('--accuracy', action='store_true', help='Print Accuracy of the model')
args = parser.parse_args()
def normalize_data(df):
    for c in df.columns: #Normalize data
        describe_df = describe.describe(df, [c])
        m = describe_df.loc['mean'][0]
        std = describe_df.loc['std'][0]
        df[c] = df[c].apply(lambda x: (x - m)/std)
    return df

def prepare_data(dataset):
    labels = dataset['Hogwarts House'].unique().tolist()
    if args.features:
        features = args.features.split(',')
    else:
        features = dataset.columns[6:]
    trainset_df = dataset[features].fillna(0)
    trainset_df = normalize_data(trainset_df)
    trainset = trainset_df.to_numpy()
    real_values = dataset['Hogwarts House'].replace(labels, [0, 1, 2, 3]).to_numpy()
    return (trainset, real_values, labels)

if __name__ == "__main__":
    if args.data:
        dataset = pandas.read_csv(args.data)
        X, y, labels = prepare_data(dataset)
        lr = LR.mylogisticregression()
        lr.fit(X, y)
        lr.train(len(labels), iterations=10000, alpha=0.001, tolerance=0.00005)
        with open("weights.txt", "w") as f:
            for classifier in lr.classifiers:
                for classi in classifier:
                    f.write(f"{classi} ")
                f.write("\n")
        if args.accuracy:
            score = lr.get_accuracy()
            print(score)
            
            
