import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
import argparse
import config

similar_courses = ['Defense Against the Dark Arts', 'Astronomy']

data = pd.read_csv(config.DATA_SRC+'/dataset_train.csv')
features = similar_courses
rows = 1
fig, axs = plt.subplots(1)

#Dropping not complete data
#cdata = data[features].dropna() 

#Take only the relevant data
cdata = data[features + ['Hogwarts House']]

houses_color = {'Gryffindor': "#CD373C", 
                'Hufflepuff': "#ecb939", 
                'Ravenclaw': "#21a8d5",
                'Slytherin': "#1a472a" }

if rows == 1:
    # Create the scatter plot
    for house in houses_color:
        axs.scatter(cdata[cdata['Hogwarts House']==house][features[0]], 
                    cdata[cdata['Hogwarts House']==house][features[1]], 
                    color=houses_color[house], label=house)

    #create legend's informations
    axs.set_title(features[1])
    axs.set_ylabel(features[0])    
    handles, labels = axs.get_legend_handles_labels()

else:
    # Create all the scatter plot for all the combination of the caracterisc.
    for i in range(rows):
        for j in range(rows):
            # Taking out duplicate graphics
            if j + 1 > rows - i : 
                fig.delaxes(axs[i, j]) 
            else:
                # Obtener las características actuales para el scatter plot
                feature1 = features[i]
                feature2 = features[rows - j]

                # Create the scatter plot in the subplt correspondent
                for house in houses_color:
                    axs[i, j].scatter(cdata[cdata['Hogwarts House']==house][feature1], 
                                      cdata[cdata['Hogwarts House']==house][feature2], 
                                      color=houses_color[house], label=house)

                if i == 0:
                    axs[i, j].set_title(feature2)
                if j == 0:
                    axs[i, j].set_ylabel(feature1)
                
                axs[i, j].tick_params(axis='both', labelsize=12)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    #create legend's informations
    handles, labels = axs[0,0].get_legend_handles_labels()

fig.legend(handles, labels, loc='outside upper left')
fig.suptitle('Scatterplot of Hogwarts Courses\' by Scores')

plt.tight_layout()
plt.show()
