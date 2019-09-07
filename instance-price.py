#!/usr/local/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##Read csv as data frame
data = pd.read_csv('ri-instanceTypes.csv')

data = data[data['On-Demand Hours'] != 0]

##Calculate per hour cost
new_data = data.assign(Hourly_Cost = lambda x: data['On-Demand Cost']/data['On-Demand Hours'])

##Find the max and the min priced instances based on hourly cost
mostExpensive = new_data.loc[new_data['Hourly_Cost'].idxmax()]
print('\n'"------- Most Expensive Instance --------"'\n')
print(mostExpensive.to_string())

leastExpensive = new_data.loc[new_data['Hourly_Cost'].idxmin()]
print('\n'"------- Least Expensive Instance --------"'\n')
print(leastExpensive.to_string())

##Finding the highest and least priced instance in every region and process the data frame for graph plot
grouped = new_data.groupby('Region')
idx = new_data.groupby(['Region'])['Hourly_Cost'].transform(max) == new_data['Hourly_Cost']
idn = new_data.groupby(['Region'])['Hourly_Cost'].transform(min) == new_data['Hourly_Cost']
print('\n\n\n')

filtered1 = pd.DataFrame(new_data[idx], columns=['Region', 'Instance Type', 'Hourly_Cost'])
filtered2 = pd.DataFrame(new_data[idn], columns=['Region', 'Instance Type', 'Hourly_Cost'])

frame1 = filtered1.sort_values('Region', ascending=True)
frame2 = filtered2.sort_values('Region', ascending=True)

print('\n\n')

##Plot the graph using the pre-processed data above
fig, ax = plt.subplots()

frame1Plot = ax.bar(frame1['Region'], frame1['Hourly_Cost'], label='Most Expensive', color='Orange')
frame2Plot = ax.bar(frame2['Region'], frame2['Hourly_Cost'], label='Least Expensive', color='Green')

plt.xlabel('AWS Regions')
plt.ylabel('Price Per Hour')
plt.legend()
ax.set_title('Most and least expensive instance in every AWS region')
plt.show()
plt.savefig('price-of-instances.jpg')
