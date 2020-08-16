import os
import csv

file_path = os.path.join('Resources','budget_data.csv')

contents = []
profit_loss_amt = []
profit_loss_diff_amt = []
total_amt = 0
avg_chng = 0

with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    # Exclude header
    header = next(csvreader)

    for row in csvreader:
        # Creates a list of all contents
        contents.append(row)
        # Counts the total amount per row
        total_amt += float(row[1])
        # Creates a list of just profit/loss
        profit_loss_amt.append(float(row[1]))

# The total number of months included in the dataset AKA last row not counting the header since we did next*
months = len(contents)
print(f'(Total Months: {months})'

# The net total amount of "Profit/Losses" over the entire period
print(round(total_amt))

# The avg of the changes in Profit/Losses over the entire period
for i in range(months-1):
    # Obtains total for changes between row 
    avg_chng += ((profit_loss_amt[i+1]) - (profit_loss_amt[i]))
    # Creates a list of every delta at each row
    profit_loss_diff_amt.append((profit_loss_amt[i+1]) - (profit_loss_amt[i]))
# Prints the average in changes for data set
print(round(avg_chng/float(months-1),2))
# Prints the Max of the profit/loss list 
print(max(profit_loss_diff_amt))
