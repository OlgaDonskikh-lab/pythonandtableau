#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 17:28:08 2025

@author: olgadonskikh
"""

import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#method 1 to read json_data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#methid 2 to load json_data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()
 
#describe the data
loandata.describe()

#describe a data for speicfic column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to gt the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income


 
#FICO Score
fico = 250
 
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and fico < 400:
# fico >= 601 and ficoscore < 660: : 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# ico >= 780: 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat =  'Unknown'
print (ficocat)

fruits = ['apples', 'pear', 'banana', 'cherry']

for x in fruits:
    print(x)
    y = x+' fruit'
    print(y)
    
for x in range(0,4):
    y = fruits[x]+' for sale'
    print(y)
    
#applying for loops to loan data

#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category =  loandata['fico'][x] 
    
    try:
        if category >=300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category  < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'    
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error - Unknown'  
        
    ficocat.append(cat)
    
#convert it to series(=a colomn in a datafame )   
ficocat = pd.Series(ficocat)   

#create a new column on loandata
loandata['fico.category'] = ficocat 


#df.loc as conditional statement
#df.loc[df[colomnname] condition, newcolomnnname] = 'value if the condition is met'
    
# for interest rates,  a new column is wanted. if rate >0.12 then high, else low     

loandata.loc[loandata['int.rate'] > 0.12,'int.rate.type' ] = 'High'    
loandata.loc[loandata['int.rate'] <= 0.12,'int.rate.type' ] = 'Low'    
    

#matplotlib

#number of loans/ rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()
    
purposeplot = loandata.groupby(['purpose']).size()   
purposeplot.plot.bar   (color = 'red', width = 0.2)
plt.show()
    
#scatter plot

ypoint = loandata['annualincome']    
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index = True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











    