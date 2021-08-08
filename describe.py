#!/usr/bin/env python
import pandas
import math
import sys
import numpy

pandas.set_option("max_columns", 100)

# The sum of a data set 
# adding all the numbers
def mysum(col):
    mysum = 0
    for e in col:
        mysum += e
    return mysum

# The average of a data set 
# adding all the numbers and dividing
def mymean(col):
    mysum = 0
    c = mycount(col)
    if not c:
        return numpy.nan
    for e in col:
        mysum += e
    return mysum/c

# The minimum data of a data set
def mymin(col):
    if not mycount(col):
        return numpy.nan
    m = col.iloc[0];
    for e in list(col):
        if e < m:
            m = e
    return m

# The maximum data of a data set
def mymax(col):
    if not mycount(col):
        return numpy.nan
    m = col.iloc[0]
    for e in list(col):
        if e > m:
            m = e
    return m

# The total number of data set
def mycount(col):
    count = 0;
    for e in col:
        count += 1;
    return count

# Standard Deviation of a data set
def mystd(col):
    m = mymean(col);
    m2 = 0
    for e in list(col):
        m2 += (e - m) * (e - m)
    c = mycount(col) #(not n - 1 ?)
    if not c:
        return numpy.nan
    m2 /= mycount(col) 
    std = math.sqrt(m2)
    return std

def describe(df, fields):
    index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'sum']
    data = {}
    for field in fields:
        col = df[field].dropna()
        data[field] = [mycount(col), mymean(col), mystd(col), mymin(col), mypercentile(col, 25), mypercentile(col,50), mypercentile(col, 75), mymax(col), mysum(col)]
    describe_df = pandas.DataFrame(data)
    describe_df.index = index
    return describe_df

def mypercentile(col, percentile):
    if not mycount(col):
        return numpy.nan
    col_sorted = list(col.sort_values())
    i = (percentile * (mycount(col) - 1))/100
    if i.is_integer():
        p = col_sorted[int(i)]
    else:
        il = col_sorted[math.floor(i)]
        ih = col_sorted[math.ceil(i)]
        p = ih * (i - int(i)) + il * (1 - (i - int(i)))
    return p

if __name__ == "__main__":
    sys.argv[1] = "datasets/dataset_test.csv"
    if len(sys.argv) < 2:
        print("USAGE: describe.py <csv files>")
    else:
        df = pandas.read_csv(sys.argv[1])
        numeric_features = []
        for c in df.columns:
            col_type = df[c].dtype
            if col_type == float or col_type == int:
                numeric_features.append(c)
        describe_df = describe(df, numeric_features)
        print(describe_df)



