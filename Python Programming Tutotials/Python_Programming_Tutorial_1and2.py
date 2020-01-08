# import libraries#
import pandas as pd
import matplotlib as plt
# reading the data
df = pd.read_csv(r'C:\Users\Anushka\Desktop\TestGit\Datasets\avocado.csv')
# adding r is very important#
df["Date"]=pd.to_datetime(df["Date"])
print(df)
print(df.head(3))
print(df.tail(5))
df.tail(5)
df["AveragePrice"].head()
albany_df = df[df['region'] == "Albany"]
albany_df.head()
#albany_df = albany_df.set_index("Date")
albany_df.set_index("Date",inplace = True)
albany_df.head()
albany_df.plot()
albany_df["AveragePrice"].plot()
albany_df["AveragePrice"].rolling(25).mean().plot()
albany_df.index
#sorting the index#
albany_df.sort_index(inplace=True)
albany_df["AveragePrice"].rolling(25).mean().plot()
albany_df.index
# adding a new column of moving averagenamed price25ma#
albany_df["price25ma"]=albany_df["AveragePrice"].rolling(25).mean()
albany_df.head(30)
# To remove na values#
albany_df.dropna().head(3)
# since we are making changes in Data Frame, Hence make a 
#copy of it and do the operations, compare it with line 13#
albany_df = df.copy()[df["region"]== "Albany"]
albany_df.set_index("Date",inplace = True)
albany_df.sort_index(inplace = True)
albany_df["price25ma"]=albany_df["AveragePrice"].rolling(25).mean()
albany_df.head(30)
df.values
df["region"].values
# To get unique values use the following #
df["region"].unique()




# Now if we want to organize the data region wise (region in columns 
# and corresponding moving average, and date, we need to remove oneof
# the categories which are organic and conventional so we will just take
# organic so we will redo the entire thing)

# import libraries#
import pandas as pd
import matplotlib as plt
# reading the data
df = pd.read_csv(r'C:\Users\Anushka\Desktop\TestGit\Datasets\avocado.csv')
# adding r is very important#

# subset it for organic by creating a copy#
df=df.copy()[df["type"]=="organic"]
# now convert date string as date and time
df["Date"]=pd.to_datetime(df["Date"])
df.head(30)
# Now we can sort it using a new command, sort.values#

df.sort_values(by="Date",ascending = True, inplace = True)
# Now we need to rearrange the data where regions are column headers 
#and we have moving average values along with dates#

# iniialize the data frame#
graph_df =pd.DataFrame()
# Now will use for loop to extract region wise data and add the moving
# averagevalue column

for region in df["region"].unique():
    region_df = df.copy()[df["region"]== region]
    region_df.set_index("Date",inplace = True)
    region_df.sort_index(inplace = True)
    # adding the moving avg column#
    region_df[f"{region}_price25ma"]=region_df["AveragePrice"].rolling(25).mean()
    
    # Now using If Command to get the region wise MA data#
    
    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]
        
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])
        
    
graph_df.tail(5)
# Let us plot it#

graph_df.plot(figsize=(8,5),legend = False)  

# To remove the gap#
graph_df.dropna().plot(figsize=(8,5),legend = False)

    
    
    






















