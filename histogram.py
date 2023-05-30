import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
import argparse
import math
import config

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
	if len(courses)%2: 
		if rows == 1:
			fig.delaxes(axs[1])
		else :
			fig.delaxes(axs[rows - 1, 1])
else:
	courses = [homogenous_course]
	fig, axs = plt.subplots(len(courses))

houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw','Slytherin']
houses_color = ["#CD373C", "#ecb939", "#21a8d5", "#1a472a"]
data = pd.read_csv(config.DATA_SRC+'/dataset_train.csv')

for i, course in enumerate(courses):
	cdata = data.dropna(subset=[course])
	to_analyze = []
	for house in houses:
		to_analyze.append(cdata[cdata['Hogwarts House']==house][course])
	
	if args.statistics:
		statistic, p_value = f_oneway(to_analyze[0], to_analyze[1], to_analyze[2], to_analyze[3])
		print(f"{course} has a p_value = {p_value} and statistic of {statistic}")
	if not args.full:
		axs.hist(to_analyze, bins=10, alpha=0.7, label=houses, color=houses_color)
		axs.set_xlabel(course)
	elif rows == 1:
		axs[i%2].hist(to_analyze, bins=10, alpha=0.7, label=houses, color=houses_color)
		axs[i%2].set_xlabel(course)
	else:
		axs[i//2,i%2].hist(to_analyze, bins=10, alpha=0.7, label=houses, color=houses_color)
		axs[i//2,i%2].set_xlabel(course)
		
#creating legend entries
if args.full:
	if rows == 1:
		handles, labels = axs[0].get_legend_handles_labels()
	else:
		handles, labels = axs[0,0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='outside lower left')
else:
	fig.legend()

fig.supxlabel('Scores of Students by Classes')
fig.supylabel('Number of Students by Houses')
fig.suptitle('Histogram of Hogwarts Courses\' Score Distribution')

fig.tight_layout()
plt.show()
