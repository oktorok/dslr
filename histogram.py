#!/usr/bin/env python
import pandas
import math
import sys
import numpy
from describe.py import describe 

def observed_table(df, fields, houses, type_calc):
    observed = {}
    row = {}
    row['Total Courses'] = [0] * (len(houses)+1)
    for field in fields[2:]:
        sum = 0
        observed[field] = []
        for house in houses:
            sum += df[house][field][type_calc]
            observed[field].append(df[house][field][type_calc])    
        observed[field].append(sum)
        row['Total Courses'] = [row['Total Courses'][i] + observed[field][i] for i in range(len(observed[field]))]
    
    observed['Total Courses'] = row['Total Courses']
    observed_df = pd.DataFrame(observed)
    observed_df.index = houses + ['Total Students']
    return (observed_df)


def expected_table(df):
    expected = df;
     
    max_col = len(df.iloc[0]) - 1
    max_row = len(df[0]) - 1
    expected = [[df.iloc[max_row, j] * df.iloc[i,max_col] / df.iloc[max_row,max_col] for j in range(max_col)]
            for i in range(max_row)]

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
        homogeneity_data = {}
        for house in houses:
             homogeneity_data[house] = df.loc[df['Hogwarts House'] == house]
             numeric_features = []
             for c in df.columns:
                 col_type = df[c].dtype
                 if col_type == float or col_type == int:
                     numeric_features.append(c)
             describe_df = describe(homogeneity_data[house], numeric_features)
             house_data[house] = describe_df
        
        #Total all house:
        numeric_features = []
        for c in df.columns:
            col_type = df[c].dtype
            if col_type == float or col_type == int:
                numeric_features.append(c)
        describe_df = describe(df, numeric_features)
        house_data['Total Student'] = describe_df
        
        observed_df = observed_table(house_data, numeric_features, houses, 'sum')
        