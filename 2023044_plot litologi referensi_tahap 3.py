import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
import seaborn as sns 
from sklearn.neighbors import KNeighborsClassifier
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib as mpl
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

Data_Set = pd.read_csv('plot_litologi.csv')  
Data_Set = pd.DataFrame(Data_Set)
print(Data_Set)

Data_Set.describe()
Data_Set.info()

Data_Set['LITHOLOGY'].unique()
Data_Set['LITHOLOGY'].value_counts()

label = LabelEncoder()
Data_Set['LITHOLOGY'] = label.fit_transform(Data_Set['LITHOLOGY'])

print(label.classes_)

Facies_label = Data_Set['LITHOLOGY']
print(Facies_label)

facies_colors =['#A9A9A9','#FF00FF','#FFA500']
facies_labels = ['Sds', 'Sls', 'V']
#Sds = Sandstone
#Sls = Siltstone
#V = Volcanic

facies_color_map = {}
for ind, label in enumerate(facies_labels):
    facies_color_map[label] = facies_colors[ind]

print(facies_colors, facies_labels, facies_color_map)

def label_facies(row,labels):
    lithology = int(row['LITHOLOGY'])
    return labels[lithology]

Data_Set.loc[:,'FaciesLabels'] = Data_Set.apply (lambda row: label_facies(row, facies_labels), axis=1)

def make_facies_log_plot(logs, facies_colors):
    logs = logs.sort_values(by='DEPTH') 
    cmap_facies = colors.ListedColormap(facies_colors[0:len(facies_colors)], 'indexed')
    
    ztop =logs.DEPTH.min()
    zbot=logs.DEPTH.max()
        
    cluster = np.repeat(np.expand_dims(logs['LITHOLOGY'].values,1), 100,1)
    
    f, ax = plt.subplots(nrows=1, ncols=7, figsize=(8,10)) 
    ax[0].plot(logs.CALI, logs.DEPTH, '-', color='black')
    ax[1].plot(logs.DTCO, logs.DEPTH, '-', color='black')
    ax[2].plot(logs.GR, logs.DEPTH, '-', color ='black')
    ax[3].plot(logs.NPHI, logs.DEPTH, '-', color='black')
    ax[4].plot(logs.RHOB, logs.DEPTH, '-', color='black')
    ax[5].plot(logs.RESD, logs.DEPTH, '-', color='black')
    im= ax[6].imshow(cluster,interpolation='none',aspect='auto',cmap=cmap_facies, vmin=0, vmax=3)
   
    divider = make_axes_locatable(ax[6])
    cax= divider.append_axes("right", size="20%", pad=0.05)
    cbar=plt.colorbar(im,cax=cax)                   
    cbar.set_label((50*' ').join (['Sandstone', 'Siltstone', 'Volcanic']))
    cbar.set_ticks(range(0,1));
    cbar.set_ticklabels(' ')
        
    for i in range (len(ax)-1):
       ax[i].set_ylim(ztop,zbot)
       ax[i].invert_yaxis()
       ax[i].grid()
       ax[i].locator_params(axis='x', nbins=2)
    
    ax[0].set_xlabel('CALI')
    ax[0].set_xlim(logs.CALI.min(),logs.CALI.max())
    ax[1].set_xlabel('DTCO')
    ax[1].set_xlim(logs.DTCO.max(), logs.DTCO.min())
    ax[2].set_xlabel('GR')
    ax[2].set_xlim(logs.GR.min(),logs.GR.max())
    ax[3].set_xlabel('NPHI')
    ax[3].set_xlim(logs.NPHI.min(),logs.NPHI.max())
    ax[4].set_xlabel('RHOB')
    ax[4].set_xlim(logs.RHOB.min(),logs.RHOB.max())
    ax[5].set_xlabel('RESD')
    ax[5].set_xlim(logs.RESD.min(),logs.RESD.max())
    ax[6].set_xlabel('Actual litology')
   
    ax[1].set_yticklabels([]); 
    ax[2].set_yticklabels([]);
    ax[3].set_yticklabels([]);
    ax[4].set_yticklabels([]);
    ax[5].set_yticklabels([]);
    ax[6].set_yticklabels([]);

make_facies_log_plot(Data_Set, facies_colors)
plt.show()