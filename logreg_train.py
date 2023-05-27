#!/usr/bin/python3

import MyLogisticRegression as LR
import pandas
import describe
import sys

def normalize_data(df):
    for c in df.columns: #Normalize data
        describe_df = describe.describe(df, [c])
        m = describe_df.loc['mean'][0]
        std = describe_df.loc['std'][0]
        df[c] = df[c].apply(lambda x: (x - m)/std)
    return df

def prepare_data(dataset):
    labels = dataset['Hogwarts House'].unique().tolist()
    trainset_df = dataset[dataset.columns[6:]].fillna(0)
    trainset_df = normalize_data(trainset_df)
    trainset = trainset_df.to_numpy()
    real_values = dataset['Hogwarts House'].replace(labels, [0, 1, 2, 3]).to_numpy()
    return (trainset, real_values, labels)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: logreg_train.py <CSV FILE>")
    else:
        dataset = pandas.read_csv(sys.argv[1])
        X, y, labels = prepare_data(dataset)
        lr = LR.mylogisticregression()
        lr.fit(X, y)
        lr.train(len(labels), iterations=1000, alpha=0.01, tolerance=0.0005)
        with open("weights.txt", "w") as f:
            for classifier in lr.classifiers:
                for classi in classifier:
                    f.write(f"{classi} ")
                f.write("\n")
