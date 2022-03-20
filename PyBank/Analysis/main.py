import os
import csv


budget_data_csv = os.path.join('/Users/Harish/Desktop/python_challenge/PyBank/Resources/budget_data.csv')

months = []
profits =[]
change_profits =[]
change = 0
profits_int = []

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:

     months.append(row[0])
     profits.append(row[1])
    
    for x in profits:
        profits_int.append(int(x))


    no_months = len(months)
    total_profit = sum((profits_int))
    
    for i in range(no_months-1):
        change = (profits_int[i+1])-(profits_int[i])
        change_profits.append(change)

    average_change = sum(change_profits)/len(change_profits)
    greatest_gain = max(change_profits)
    greatest_loss = min(change_profits)

    greatest_gain_date = months[change_profits.index(greatest_gain)+1]
    greatest_loss_date = months[change_profits.index(greatest_loss)+1]

print(f"Total Months: {no_months}")
print(f"Total Profit: {total_profit}")
print(f"Average Profit: {average_change}")
print(f"Greatest Gain: {greatest_gain_date} ({greatest_gain})")
print(f"Greatest Loss: {greatest_loss_date} ({greatest_loss})")



