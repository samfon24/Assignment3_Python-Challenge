import os
import csv

# Paths
file_path = os.path.join('Resources','budget_data.csv')
txt_file_path = os.path.join('Analysis', 'Pybank_Analysis.txt')

# Lists
contents = []
dates = []
profit_loss_amt = []
profit_loss_diff_amt = []

# Variables
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
        # Creates a list of all dates
        dates.append(row[0])

# Open txt file
txt_file = open(txt_file_path, 'w')

#Header
print('Financial Analysis')
print('-'*20)
txt_file.write('Financial Analysis \n')
txt_file.write('-'*20 + '\n')

# The total number of months included in the dataset AKA last row not counting the header since we did next*
months = len(contents)
print(f'Total Months: {months}')
txt_file.write(f'Total Months: {months} \n')

# The net total amount of "Profit/Losses" over the entire period
print(f'Net Total for Data Set Period: ${round(total_amt)}')
txt_file.write(f'Net Total for Data Set Period: ${round(total_amt)} \n')

# The avg of the changes in Profit/Losses over the entire period
for i in range(months-1):
    # Obtains total for changes between row 
    avg_chng += ((profit_loss_amt[i+1]) - (profit_loss_amt[i]))

    # List of Dates
    date = dates[i+1]

    # Creates a list of every delta at each row
    delta_chng = (profit_loss_amt[i+1]) - (profit_loss_amt[i])
    profit_loss_diff_amt.append((delta_chng))
# Inserting a 0 to the list so it matches the lenght of other lists
profit_loss_diff_amt.insert(0, 0)

for index, pnl in enumerate(profit_loss_diff_amt):
    if profit_loss_diff_amt[index] == max(profit_loss_diff_amt):
        print(f'Greatest Increase in Profits: {dates[index]} ${round(pnl)}')
        txt_file.write(f'Greatest Increase in Profits: {dates[index]} ${round(pnl)} \n')
    elif profit_loss_diff_amt[index] == min(profit_loss_diff_amt):
        print(f'Greatest Decrease in Profits: {dates[index]} ${round(pnl)}')
        txt_file.write(f'Greatest Decrease in Profits: {dates[index]} ${round(pnl)} \n')
