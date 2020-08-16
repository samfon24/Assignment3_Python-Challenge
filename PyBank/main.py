import os
import csv
import pandas as pd

file_path = os.path.join('Resources','budget_data.csv')

contents = []
profit_loss_amt = []
profit_loss_diff_amt = []

total_amt = 0

avg_chng = 0

with open(file_path, 'r') as csvfile:

    #panda reader?
    # df = pd.read_csv('budget_data.csv')
    # df.head()

    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        contents.append(row)
        total_amt = total_amt + float(row[1])
        profit_loss_amt.append(float(row[1]))

# The total number of months included in the dataset AKA last row not counting the header since we did next*
months = len(contents)
print(months)

# The net total amount of "Profit/Losses" over the entire period
print(total_amt)

# The avg of the changes in Profit/Losses over the entire period
for i in range(months-1):
    avg_chng = (profit_loss_amt[i+1]) - (profit_loss_amt[i])/
    profit_loss_diff_amt.append(avg_chng)
print(len(profit_loss_diff_amt))