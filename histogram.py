#!/usr/bin/env python
import pandas
import math
import sys
import numpy
from describe.py import describe 



def myvar(col):
    mean = mymean(col)
    c = mycount(col)
    if not c or c < 2:
        return numpy.nan

    for e in col:
        mysum += e - mean
    return mysum/(c - 1)


def create_histogram(data, count_value):
    return "titi"

if __name__ == "__main__":
    sys.argv[1] = "datasets/dataset_train.csv"
    if len(sys.argv) < 2:
        print("USAGE: histogram.py <csv files>")
    else:
        df = pd.read_csv(sys.argv[1])
        houses = df['Hogwarts House'].unique().tolist()
        houses.sort()
        if (houses != ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']):
            print("data is corrupted")
        
        house_data = {}
        for house in houses:
            data = df.loc[df['Hogwarts House'] == house]
            numeric_features = []
            for c in data.columns:
                col_type = data[c].dtype
                if col_type == float or col_type == int:
                    numeric_features.append(c)
            describe_df = describe(house_data, numeric_features)
            house_data[house] = [describe_df]
        