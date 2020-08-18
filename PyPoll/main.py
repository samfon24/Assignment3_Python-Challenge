import os
import csv

file_path = os.path.join('Resources','election_data.csv')

voter_id = []


with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        voter_id.append(row)

# Headers
print('Election Results')
print('-'*20 + '\n')

# Print the total voter count
print(f'(Total Votes: {len(voter_id)}')