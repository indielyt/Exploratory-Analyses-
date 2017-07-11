# Import Plotting Modules
import matplotlib.pyplot as plt
import pandas as pd
from textwrap import wrap

# Read in the file: df1
df = pd.read_csv('C:\DanielProjects\STREAM_WORK\PROJECTS\TO4-FMCC\Bid_Analysis\FMCC_BidAnalysis_unitcosts.csv',header=0,index_col=0)
# print (df.info())

# Confirm import by printing head, index, and columns
# print(df.head())
# print(df.index.values)
# print(df.columns.values)

# transpose and confirm column names, indexes
df2 = df.transpose()
# print (df2)

# Pull the unit/quantityt, Baker estimates, and Contractor estimates apart into new dataframes
df_unitqty = df2.iloc[:3]
# print (df_unitqty.head())
# print (df_unitqty.iloc[1])
df_baker = pd.DataFrame(df2.iloc[3])
# print (df_baker.head())
# df_baker.info()
df_contractors = pd.DataFrame(df2.iloc[4:])
# print (df_contractors.head())

# These are the bid item numbers
columns = df2.columns.values # Extract df columns (item numbers) into pandas series - works
descriptions = df2.iloc[0] # Extract the first column of item descriptions into pandas series for plot titles - works
# print (columns)
units = df_unitqty.iloc[1]
# print (units)


for i in range(41):
	plt.subplot(6,7,i+1) # Set up the plotting grid - works
	column = columns[i] # step through the columns list, using "column" variable to later identify which column of df to plot
	df_contractors[column].plot.box()
	plt.xticks(fontsize = 6) # Reduce default tick label size
	plt.yticks(fontsize = 6) # Reduce default tick label size
	plt.title("\n".join(wrap(descriptions[i],40)), fontsize=8) # create title by wrapping at designated character length
	plt.autoscale(enable=True,axis='y')
	plt.ylabel(units[i],fontsize=8)

plt.show()





