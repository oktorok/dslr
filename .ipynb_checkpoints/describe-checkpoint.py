#!/usr/bin/env python
import pandas
import math
import sys
import numpy

pandas.set_option("max_columns", 100)

def mymean(col):
    mysum = 0
    c = mycount(col)
    if not c:
        return numpy.nan
    for e in col:
        mysum += e
    return mysum/c

def mymin(col):
    if not mycount(col):
        return numpy.nan
    m = col.iloc[0];
    for e in list(col):
        if e < m:
            m = e
    return m

def mymax(col):
    if not mycount(col):
        return numpy.nan
    m = col.iloc[0]
    for e in list(col):
        if e > m:
            m = e
    return m

def mycount(col):
    count = 0;
    for e in col:
        count += 1;
    return count

def myvariance(col):
    m = mymean(col);
    v = 0
    for e in list(col):
        v += (e - m) * (e - m)
    c = mycount(col)
    if not c:
        return numpy.nan
    v /= mycount(col)
    return v

def mystd(col):
    v = myvariance(col)
    std = math.sqrt(v)
    return std

def describe(df, fields):
    index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'variance']
    data = {}
    for field in fields:
        col = df[field].dropna()
        data[field] = [mycount(col), mymean(col), mystd(col), mymin(col), mypercentile(col, 25), mypercentile(col,50), mypercentile(col, 75), mymax(col), myvariance(col)]
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



