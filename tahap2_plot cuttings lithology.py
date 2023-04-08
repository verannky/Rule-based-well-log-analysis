import lasio
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

# Step 1: Read the LAS file
well_log_data = pd.read_csv("plot_litologi.csv")
print("Original number of rows:", len(well_log_data))

#Step 2: Create dataset
welldata = pd.DataFrame(well_log_data)

#Step 3: set column names
column_names = ['DEPTH', 'CALI', 'DTCO', 'DTSM', 'GR','NPHI', 'RHOB','RESD', 'LITHOLOGY']
welldata.columns = column_names

# Print the dataset raw data and cleaned data
print(welldata)

le = LabelEncoder()
welldata['LITHOLOGY_CODE'] = le.fit_transform(welldata['LITHOLOGY'])

# data info
welldata.info()

# Step 2: Identify missing values
print(welldata.isna().sum()) # to check the number of NaN values in each column
print(welldata.describe()) # to get summary statistics of the data


#Step : Plot data
plt.style.use('default')
fig, ax = plt.subplots(1, 8 , sharex='col', sharey='row' , gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(8,16) )

for a in ax:
    a.set_ylim(5281.2696,4731.2580)
    a.set_ylabel('DEPTH')

ax[0].plot(welldata['CALI'], welldata['DEPTH'],color='b')
ax[0].grid()
ax[0].set_title('CALIPER')

ax[1].plot(welldata['DTCO'] , welldata['DEPTH'],color='g')
ax[1].grid()
ax[1].set_xlim(welldata['DTCO'].max() , welldata['DTCO'].min())
ax[1].set_title('DTCO')

ax[2].plot(welldata['DTSM'] , welldata['DEPTH'],color='g')
ax[2].grid()
ax[2].set_xlim(welldata['DTSM'].max() , welldata['DTSM'].min())
ax[2].set_title('DTSM')

ax[3].plot(welldata['GR'] , welldata['DEPTH'],color='g')
ax[3].grid()
ax[3].set_xlim(welldata['GR'].max() , welldata['GR'].min())
ax[3].set_title('GR')

ax[4].plot(welldata['NPHI'] , welldata['DEPTH'],color='g')
ax[4].grid()
ax[4].set_xlim(welldata['NPHI'].max() , welldata['NPHI'].min())
ax[4].set_title('NPHI')

ax[5].plot(welldata['RHOB'] , welldata['DEPTH'],color='g')
ax[5].grid()
ax[5].set_xlim(welldata['RHOB'].max() , welldata['RHOB'].min())
ax[5].set_title('RHOB')

ax[6].plot(welldata['RESD'] , welldata['DEPTH'],color='g')
ax[6].grid()
ax[6].set_xlim(welldata['RESD'].max() , welldata['RESD'].min())
ax[6].set_title('RESD')

# Define custom colors for lithologies
colors = {
    0: 'gray',   # Unknown
    1: 'orange', # Sandstone
    2: 'blue',   # Shale
}

# Create a colormap with custom colors
cmap = colors.values()

# Plot lithology log
ax[7].fill_betweenx(welldata['DEPTH'], 0, welldata['LITHOLOGY_CODE'], 
                    where=welldata['LITHOLOGY_CODE'].notnull(),
                    facecolor=[colors[code] for code in welldata['LITHOLOGY_CODE']])
ax[7].set_xlim(0, len(welldata['LITHOLOGY_CODE'].unique()))
ax[7].set_ylim(5281.2696, 4731.2580)
ax[7].set_title('LITHOLOGY')
ax[7].set_xlabel('Lithology')
ax[7].set_yticklabels([])
ax[7].invert_yaxis()

# Add legend
handles = [plt.Rectangle((0,0),1,1, color=colors[code]) for code in colors]
labels = colors.keys()
ax[7].legend(handles, labels)

plt.show()

