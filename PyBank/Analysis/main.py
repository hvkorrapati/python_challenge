#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import packages

import os
import csv


# In[2]:


# set file path

budget_data_csv = os.path.join('/Users/Harish/Desktop/python_challenge/PyBank/Resources/budget_data.csv')


# In[3]:


# set lists and empty variables

months = []
profits =[]
change_profits =[]
change = 0
profits_int = []


# In[4]:


# read csv 

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    
# add months and profits to lists

    for row in csvreader:
        months.append(row[0])
        profits.append(row[1])

        
# define profits as integers 

    for x in profits:
        profits_int.append(int(x))

        
# calculate number of months and total profit

    no_months = len(months)
    total_profit = sum((profits_int))

    
# calculate change in profits month-to-month

    for i in range(no_months-1):
        change = (profits_int[i+1])-(profits_int[i])
        change_profits.append(change)

        
# calculate metrics 

    average_change = sum(change_profits)/len(change_profits)
    greatest_gain = max(change_profits)
    greatest_loss = min(change_profits)

    greatest_gain_date = months[change_profits.index(greatest_gain)+1]
    greatest_loss_date = months[change_profits.index(greatest_loss)+1]


# In[5]:


# print results 

print(f"Total Months: {no_months}")
print(f"Total Profit: {total_profit}")
print(f"Average Profit: {average_change}")
print(f"Greatest Gain: {greatest_gain_date} ({greatest_gain})")
print(f"Greatest Loss: {greatest_loss_date} ({greatest_loss})")


# In[ ]:




