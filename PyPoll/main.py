import os
import csv

file_path = os.path.join('Resources','election_data.csv')

voter_id = []
candidate_votes = []

with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        voter_id.append(row)
        candidate_votes.append(row[2])

# Headers
print('Election Results')
print('-'*20)

# Print the total voter count
print(f'Total Votes: {len(voter_id)}')

khan_count = candidate_votes.count('Khan')
khan_percent = format((float(khan_count)/float(len(voter_id)))*100, ".3f")
print(f'Khan: {khan_percent}% ({khan_count})')

correy_count = candidate_votes.count('Correy')
correy_percent = format((float(correy_count)/float(len(voter_id)))*100, ".3f")
print(f'Correy: {correy_percent}% ({correy_count})')

li_count = candidate_votes.count('Li')
li_percent = format((float(li_count)/float(len(voter_id)))*100, ".3f")
print(f'Li: {li_percent}% ({li_count})')

tooley_count = candidate_votes.count("O'Tooley")
tooley_percent = format((float(tooley_count)/float(len(voter_id)))*100, ".3f")
print(f"O'Tooley: {tooley_percent}% ({tooley_count})")

candidate_count = {
    'candidates': ['Khan', 'Correy', 'Li', "O'Tooley"],
    'votes': [khan_count, correy_count, li_count, tooley_count]
    }

print('-'*20)
winner_votes = max(candidate_count['votes'])
for index, winner in enumerate(candidate_count['votes']):
    if candidate_count['votes'][index] == winner_votes:
        print(f"Winner: {candidate_count['candidates'][index]}")
print('-'*20)
