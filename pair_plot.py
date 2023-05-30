import seaborn as sns
import pandas as pd

data = pd.read_csv("datasets/dataset_train.csv")
features =  ['Hogwarts House', 'Arithmancy', 'Astronomy', 'Herbology',
'Defense Against the Dark Arts', 'Divination', 'Muggle Studies',
'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions',
'Care of Magical Creatures', 'Charms', 'Flying']

sns.pairplot(data[features], vars=features[1:], 
             hue='Hogwarts House', palette='Set1')