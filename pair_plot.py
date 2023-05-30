import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import config

data = pd.read_csv(config.DATA_SRC+"/dataset_train.csv")
features =  ['Hogwarts House', 'Arithmancy', 'Astronomy', 'Herbology',
'Defense Against the Dark Arts', 'Divination', 'Muggle Studies',
'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions',
'Care of Magical Creatures', 'Charms', 'Flying']

sns.pairplot(data[features], vars=features[1:], 
             hue='Hogwarts House', palette='Set1')

plt.show()
