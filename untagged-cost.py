#!/usr/local/bin/python3

import pandas as pd

##Read the csv file into a data frame
data = pd.read_csv('Tags.csv')

##Find the columns that has the keyword 'No Tagkey'
columnToCheck = data.filter(regex='No Tagkey')
print('\n'"Below is the column that has lists the cost of untagged instances"'\n')
print(columnToCheck.to_string())

##Calculate and print the sum of data set of the filtered columns
data.loc['Total Cost Of Untagged'] = columnToCheck.sum()

totalNoTagCost = data[data.columns[1]].tail(1)
print('\n\n'"The total cost of all the instances which has no tags is as below")
print(totalNoTagCost.to_string())
print('\n')