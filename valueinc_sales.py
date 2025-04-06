#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 21:00:05 2025

@author: olgadonskikh
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <--- format for read.csv
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

#working with calculations

#defining variables 

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11- 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem

CostPerTransacton = CostPerItem * NumberofItemsPurchased
SellingProceperTransaction = SellingPricePerItem * NumberofItemsPurchased

#Cost per transaction column calculation

#CostPerTransacton = CostPerItem * NumberofItemsPurchased 
#varuable = dataframe['columnt_name']

CostPerItem = data['CostPerItem']
NumberofItemsPerchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPerchased

#adding a new  column to a dataframe

data['CostPerTransaction'] = CostPerTransaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales per transaction
data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

#profit per transaction calcualation
data['ProfitPerTransaction'] = data['SalesPerTransaction']  - data['CostPerTransaction']

#markup calculation
data['Markup'] = (data['SalesPerTransaction']  - data['CostPerTransaction']) / data['CostPerTransaction']

data['ProfitPerTransaction']

#rounding Marking
roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#combining data fields
my_date ='Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'

#checking columns data type
print(data['Day'].dtype)

#change column type
day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-'+year

data['date'] = my_date

#using iloc to view specific column/rows
data.iloc[0]  #views the row with index=0
data.iloc[0:3]   #first 3 rows
data.iloc[-5:]   #last 5 lows

data.head(5)   #brings in first 5 rows

data.iloc[:,2]  #brings in all rows on the 2nd column

data.iloc[4,2]  #brings in the 4th row 2nd column

#using split to split the clients key words
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',',expand=True)

#creating new columns for the split colimns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]


#using the replace function 
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using the lower finction to change item to lowcase
data['ItemDescription'] = data['ItemDescription'].str.lower() 

#how to merge files 

#bringing a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merged files: 
#merge_df = pd.merge(df_old, sd_new, on = 'key')

data = pd.merge(data,seasons, on = 'Month')

#droping columns
# df = df.drop('columnname', axis =1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop ('Day', axis = 1)

data  = data.drop(['Year', 'Month'],axis = 1 )


#export into a CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)

















