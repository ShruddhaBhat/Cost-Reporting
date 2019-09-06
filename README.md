# Cost-Reporting

A project that was created as part of SRE - Cost Engineer Assignment.

# What does it contain?

This project contains instance-price.py script written in python that calculates
  1. The least and most expensive AWS instance types given in ri-instanceTypes.csv file.
  2. The least and most expensive AWS instances in every region and plots them against their on-demand price-per-hour as a bar      graph.

It also contains another script untaagged-cost.py which reads from Tags.csv file, finds all those instances that does not have tags and calculates the total cost incurred by them.

On-Demand Cost Reduction Recommendations is a simple text file which gives few recommendations on how the on-demand costs can be reduced for the usage given in ri-instanceTypes.csv file.

# Pre-requisites

This program makes use of Pandas Library for analysing the data. Therefore, it is necessary to intall pandas and can be done using pip3.

`pip3 install pandas`

