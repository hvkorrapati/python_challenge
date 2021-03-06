#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import unique
import os
import csv


# In[2]:


#set file path
election_data_csv = os.path.join('/Users/Harish/Desktop/python_challenge/PyPoll/Resources/election_data.csv')


# In[3]:


#define lists and empty variables
votes =[]
county = []
candidates = []

DeGette_total = 0
Doane_total = 0
Stockham_total = 0


# In[4]:


#open csv
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

#add votes and candidates to respective lists
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        
#calculate number of total votes and list of unique candidates
    total_votes = len(votes)
    unique_candidates = sorted(set(candidates))

#count votes for each candidate
    for i in range(len(candidates)):
        if candidates[i] == unique_candidates[1]:
            DeGette_total = DeGette_total + 1
        elif candidates[i] == unique_candidates[2]:
            Doane_total = Doane_total +1
        else: 
            Stockham_total = Stockham_total +1
            
    # Define percentage of vote received for each candidate
    DeGette_percentage = (DeGette_total/total_votes)*100
    Doane_percentage = (Doane_total/total_votes)*100
    Stockham_percentage = (Stockham_total/total_votes)*100
    
# Determine winner   
    if DeGette_percentage > Doane_percentage and DeGette_percentage > Stockham_percentage:
        winner = "Diana DeGette"

    elif Doane_percentage > DeGette_percentage and Doane_percentage > Stockham_percentage:
        winner = "Raymon Antony Doane"

    else: winner = "Charles Casper Stockham"


# In[5]:


# print results

print("Election Results")
print(f"--------------------------")
print(f"Total votes: {total_votes}")
print(f"--------------------------")
print(f"Diana DeGette: {DeGette_percentage}% ({DeGette_total})")
print(f"Raymon Anthony Doane: {Doane_percentage}% ({Doane_total})")
print(f"Charles Casper Stockham: {Stockham_percentage}% ({Stockham_total})")
print(f"--------------------------")
print(f"Winner: {winner}")


# In[ ]:




