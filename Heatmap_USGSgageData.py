###  Works! 7/6/2017
import pandas as pd
import numpy as np
import csv
import datetime

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm



# csv has been cleaned of usgs information, only the gage records are included here
csv = r"P:\Studies\137708_COPitkin_ErosionHazard\Working\USGS Gage Data\RoaringFork_DailyQ_USGSgage_09073300.csv"

# Read csv into pandas Dataframe
df = pd.read_csv(csv,header = None)
# print (df.head())

# convert dates to pandas datetime object
df[2] = pd.to_datetime(df[2])
print (df[2].dtype)

# drop unnecessary columns
df = df.drop([0,1,4],1)

# create new column for day of year
df['day'] = 0
df['year'] = 0
df.rename(columns={3:'cfs'}, inplace=True)

# convert datetimes to day of year
length = len(df)
print (length)
for i in range(length):
	df.loc[i,'day'] = df.loc[i,2].dayofyear
	df.loc[i,'year'] = df.loc[i,2].year


# drop original datatime objects now that day of year is defined
df = df.drop([2],1)
# print (df.tail())





### 2-d histogram from <https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram2d.html>

# Define mins and maxs for the data
yr_min = df['year'].min()
yr_max = df['year'].max()
day_min = df['day'].min()
day_max = df['day'].max()
cfs_min = df['cfs'].min()
cfs_max = df['cfs'].max()
# print (yr_max-yr_min,day_max-day_min,)

# Produce arrays that will define axes in colormesh plot
x = np.arange(day_min,day_max+1)
y = np.arange(yr_min, yr_max+1)

# Define X and Y by meshgrid
X,Y = np.meshgrid(x,y)
print (X.shape)

# Define histogram values (raster colors)
z = df['cfs'].values

# Create new Z dataframe with same shape as X,Y - important!!!
Z= pd.DataFrame(0,index=y,columns=x)
print (Z.shape)

# The Z values must be in a dataframe of the same shape as x and y
# Fill in new dataframe by stepping line through line in the gage data
# and writing it into the Z dataframe
for i in range(length):
	day = df.ix[i,'day'] 
	year = df.ix[i,'year']
	cfs = df.ix[i, 'cfs']
	# print (day, year, cfs)
	Z.ix[year,day] = cfs
print (Z.shape)

# Plotting, note colors are logNorm for greater effect
plt.figure()
plt.pcolormesh(X,Y,Z, norm=LogNorm(vmin=cfs_min, vmax=cfs_max),cmap='Blues')

# Colorbar
clb = plt.colorbar()
clb.ax.set_title('CFS')

if True:
	# Contour of Bankfull (385cfs)
	CS = plt.contour(X,Y,Z,levels=[385],colors='k',linewidths=(1,))
	plt.clabel(CS,fmt = '%2.1d',colors='k',fontsize=8)

# Add titles, labes, and xticks
plt.title('Raster Hydrograph - USGS Gage 9073300')
plt.xlabel('Time of Year')
plt.ylabel('Year of Record')

ticks = np.arange(day_min,day_max,30.5)
labels = ['January','February','March','April','May','June','July','August','September','October','November','December']
plt.xticks(ticks,labels)
plt.xticks(rotation=45)

# Show plot
plt.show()







