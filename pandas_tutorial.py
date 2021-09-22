#!/usr/bin/env python
# coding: utf-8

# In[11]:


#python pandas tutorial
#
import pandas as pd

#dataframe = pd.read_csv('smFISH_BC.csv')
#dataframe = pd.read_csv('smFISH_BC.csv', chunksize=10)
#dataframe = pd.read_excel('smFISH_BC.xlsx')
#dataframe = pd.read_csv('philip_avg.5k.txt', delimiter=' ')
#print(dataframe.head(5))
#print(dataframe.tail(5))

#read headers
#print(dataframe.columns)

#read columns, rows and specific location
#print(dataframe[['Time','Slide']][0:3])
#print(dataframe.iloc[1:4])
#print(dataframe.iloc[2,2])

#iterate along a row
#for index, row in dataframe.iterrows():
#    print(index, row[['Time','Slide']])

#find location depending on specific info 
#dataframe.loc[dataframe['Slide']==2]

#describe, sort etc.
#dataframe.describe()
#dataframe.sort_values(['Time','Counts Bmal1'], ascending=[1,1])

#making changes to the data
#dataframe["Total"]=dataframe.iloc[:,2:4].sum(axis=1)
#dataframe=dataframe.drop(columns=['Total'])
#cols=list(dataframe.columns)
#dataframe=dataframe[cols[0:2] + [cols[5]] + cols[2:5]]

#saving data
#dataframe.to_csv('modified.csv', index=False)
#dataframe.to_csv('modified.txt', index=False, sep='\t')

#fitering data
#new_df=dataframe.loc[(dataframe['Time']>24) & (dataframe['Slide']==2)] 
#new_df.reset_index(drop=True, inplace=True)
#to filter using a string
#df.loc[df['name'].str.contains('this')]
#~ == not containing
#df.loc[~df['name'].str.contains('this')]
#print(new_df)



# In[1]:


#fitering using regular expression
import re

#df.loc[df['column name'].srt.contains('this|that', regex=True)]
#df.loc[df['column name'].srt.contains('^a[a-z]*',flags=re.I regex=True)]


#conditional changes
#df.loc[df['column name'] == 'old name', 'column name'] = 'new name'
#df.loc[df['column 1'] > 500, ['column 2', 'column 3']] = ['new 1','new2']


#Aggregate statistics using groupby

#df.groupby(['column1']).mean()
#df.groupby(['column1']).mean().sort('sort by this column', ascending=False)
#df.groupby(['column1']).sum()
#df.groupby(['column1']).counts()
#df.groupby(['column1','column2']).counts()

#read data by chinks and append the results into a new dataframe
#create an empty dataframe with same columns as your input file
#new_df = pd.DataFrame(columns = df_input.columns)

#for df in pd.read_csv('datasheet.csv', chunksize = 10):
#    results = df.groupby(['column name']).count()
#    new_df = pd.concat([new_df, results]) 


# In[ ]:




