import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--full', action='store_true', help='Show All Histograms')
parser.add_argument('--statistics', action='store_true', help='Show ANOVA Statistics')
args = parser.parse_args()

homogenous_course = 'Care of Magical Creatures'

if args.full:
	courses =  ['Arithmancy', 'Astronomy', 'Herbology',
'Defense Against the Dark Arts', 'Divination', 'Muggle Studies',
'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions',
'Care of Magical Creatures', 'Charms', 'Flying']
	rows = math.ceil(len(courses)/2)
	fig, axs = plt.subplots(math.ceil(rows),2, figsize=(10,10))
else:
	courses = [homogenous_course]
	fig, axs = plt.subplots(len(courses))

houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw','Slytherin']
data = pd.read_csv('datasets/dataset_train.csv')

c = 0
for i, course in enumerate(courses):
	if i >= len(courses)//2:
		c = 1
	cdata = data.dropna(subset=[course])
	to_analyze = []
	for house in houses:
		to_analyze.append(cdata[cdata['Hogwarts House']==house][course])
	if args.statistics:
		statistic, p_value = f_oneway(to_analyze[0], to_analyze[1], to_analyze[2], to_analyze[3])
		print(f"{course} has a p_value = {p_value} and statistic of {statistic}")
	if not args.full:
		axs.hist(to_analyze, bins=10, alpha=0.7, label=houses)
		axs.set_xlabel(course)
	else:
		axs[i%rows,c].hist(to_analyze, bins=10, alpha=0.7, label=houses)
		axs[i%rows,c].set_xlabel(course)
fig.tight_layout()
plt.show()