#!/usr/bin/env python
import pandas
import math
import sys
import numpy

if __name__ == "__main__":
    sys.argv[1] = "datasets/dataset_train.csv"
    if len(sys.argv) < 2:
        print("USAGE: histogram.py <csv files>")
    else:
        df = pd.read_csv(sys.argv[1])
        # if all Houses 
        compare_between = df['Hogwarts House'].unique().tolist()
        compare_between.sort()
        if (compare_between != ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']):
            print("data is corrupted")


        
        # if all compare all notes subjects
        compare_by = ['Arithmancy', 'Astronomy', 'Herbology',
            'Defense Against the Dark Arts', 'Divination', 'Muggle Studies',
            'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions',
            'Care of Magical Creatures', 'Charms', 'Flying']

        new_index = pd.MultiIndex.from_product([compare_between, compare_by], names=["Index", "Subject"])

        # Create new table with just the data
        Pivot = data.melt(id_vars = ['Hogwarts House'], value_vars = subjects, var_name = 'Subject', value_name='Grades')


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
        