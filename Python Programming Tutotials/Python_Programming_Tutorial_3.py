# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:16:42 2020

@author: Anushka
"""

# Import Libraries#
import pandas as pd

# Read the data#
df = pd.read_csv(r'C:\Users\Anushka\Desktop\TestGit\Datasets\Minimum Wage Data.csv')
# There is an error due to the type of data in the file, as pandas read files which have
# encoding as UTF 8, One way is to try encoding = latin#

df = pd.read_csv(r'C:\Users\Anushka\Desktop\TestGit\Datasets\Minimum Wage Data.csv', encoding ="latin")

# It makes sense to save this new file as csv with encoding as UTF-8 by using following command#

df.to_csv(r'C:\Users\Anushka\Desktop\TestGit\Datasets\minwage.csv',encoding ="utf-8")

# Now let us read this andcheck#

df =pd.read_csv(r'C:\Users\Anushka\Desktop\TestGit\Datasets\minwage.csv')

df.head()

# Now Let us group the data by state and have Year as Index by using pandas way#

gb = df.groupby("State")
gb.head()
# let us subset for Alabama#

gb.get_group("Alabama").set_index("Year").head()

# We can iterate over the Group  and create a DF where we have Year wise, State wise minimum wages#

# Let us initiatize the Data Frame#
act_min_wage =pd.DataFrame()

# let us put the iteration function using for 

for name,group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))
        
        act_min_wage.head()
        
# Now we can do aquick analysis of it by using describe function
        
act_min_wage.describe()

act_min_wage.corr().head()
df.head()
# let us check the values for zero or nan#
issue_df = df[df["Low.2018"]==0]
issue_df.head()
issue_df["State"].unique()
# We should eliminate all with no data, so let us install numpy#
import numpy as np
# replace 0 with NaN and get rid of columns containing these values, we use axis =1 for columns#
act_min_wage.replace(0,np.NaN).dropna(axis=1)

min_wage_corr =act_min_wage.replace(0,np.NaN).dropna(axis=1).corr()
for problem in issue_df["State"].unique():
    if problem in min_wage_corr.columns:
        print("Missing Values")
# Nothing gets printed so we are good














































