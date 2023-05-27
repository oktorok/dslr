import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys

similar_courses = ['Defense Against the Dark Arts', 'Astronomy']

parser = argparse.ArgumentParser()
parser.add_argument('--full', action='store_true', help='Show All Scatter Plots')
args = parser.parse_args()

data = pd.read_csv('datasets/dataset_train.csv')
if not args.full:
    features = similar_courses
    cdata = data[features].dropna()
    fig, axs = plt.subplots(1)
    axs.scatter(data[features[0]], data[features[1]])
    axs.set_title(features[1])
    axs.set_ylabel(features[0])
else:
    features =  ['Arithmancy', 'Astronomy', 'Herbology',
'Defense Against the Dark Arts', 'Divination', 'Muggle Studies',
'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions',
'Care of Magical Creatures', 'Charms', 'Flying']
    cdata = data[features].dropna()
    fig, axs = plt.subplots(len(features), len(features),figsize=(20, 10))

    # Iterar sobre las combinaciones de características y crear los scatter plots correspondientes
    for i in range(len(features)):
        for j in range(len(features)):
            # Obtener las características actuales para el scatter plot
            feature1 = features[i]
            feature2 = features[j]
            # Crear el scatter plot en el subplt correspondiente
            if i != j:
                axs[i, j].scatter(data[feature1], data[feature2], s=2)
            if i == 0:
                axs[i, j].set_title(feature2, fontsize=5)
            if j == 0:
                axs[i, j].set_ylabel(feature1, fontsize=5)
            axs[i, j].tick_params(axis='both', labelsize=2)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

plt.tight_layout()
plt.show()