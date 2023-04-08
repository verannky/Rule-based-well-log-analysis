import lasio
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt

# Step 1: Read the LAS file
well_log_data = pd.read_csv("Kronos1.csv")
print("Original number of rows:", len(well_log_data))

#Step 2: Create dataset
raw_welldata = pd.DataFrame(well_log_data)

#Step 3: set column names
column_names = ['DEPTH','CALI', 'DTCO', 'DTSM', 'GR','NPHI', 'RHOB','RESD']
raw_welldata.columns = column_names

#Step 4: Remove ADJS, DTCO2 column
welldata = raw_welldata.dropna()
print("drop nan data number of rows:", len(welldata))

# Print the dataset raw data and cleaned data
print(raw_welldata)
print(welldata)

# data info
welldata.info()

# Step 2: Identify missing values
print(welldata.isna().sum()) # to check the number of NaN values in each column
print(welldata.describe()) # to get summary statistics of the data

# Step 4: Clean the data
# Fill missing values with the mean of each column
imputed_well_log_data = well_log_data.fillna(welldata.mean())
print(imputed_well_log_data)

# Step 6: Normalize or standardize the data
scaler = MinMaxScaler()
normalized_well_log_data = pd.DataFrame(scaler.fit_transform(welldata), columns=welldata.columns)

# Step 7: Standardize the data using z-score normalization
standard_scaler = StandardScaler()
standardized_well_log_data = pd.DataFrame(standard_scaler.fit_transform(welldata), columns=welldata.columns)

# Step 7: Perform exploratory data analysis
# Histograms of each feature
welldata.hist(bins=20, figsize=(15, 15))
plt.show()

#Step : Plot data
plt.style.use('default')
fig, ax = plt.subplots(1, 7 , sharex='col', sharey='row' , gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(8,16) )

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

ax[2].plot(welldata['DTSM'] , welldata['DEPTH'], color='g')
ax[2].grid()
ax[2].set_title('DTSM')

ax[3].plot(welldata['GR'] , welldata['DEPTH'], color='g')
ax[3].grid()
ax[3].set_title('GAMMA RAY')

ax[4].plot(welldata['NPHI'] , welldata['DEPTH'], color='g')
ax[4].grid()
ax[4].set_title('NPHI')

ax[5].plot(welldata['RHOB'] , welldata['DEPTH'], color='g')
ax[5].grid()
ax[5].set_title('RHOB')

ax[6].plot(welldata['RESD'] , welldata['DEPTH'], color='g')
ax[6].grid()
ax[6].set_title('RESD')

#save file
welldata.to_csv("clean_well_log_data.csv", index=False)