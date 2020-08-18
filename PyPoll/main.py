import os
import csv

# Paths
file_path = os.path.join('Resources','election_data.csv')
txt_file_path = os.path.join('Analysis', 'Pypoll_Analysis.txt')

# Lists
voter_id = []
candidate_votes = []

with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        voter_id.append(row)
        candidate_votes.append(row[2])

# Open txt file
txt_file = open(txt_file_path, 'w')

# Headers
print('Election Results')
print('-'*20)
txt_file.write('Election Results' + '\n')
txt_file.write('-'*20 + '\n')

# Print the total voter count
print(f'Total Votes: {len(voter_id)}')
txt_file.write(f'Total Votes: {len(voter_id)}' + '\n')

# Counts the percentages and total count per candidate
khan_count = candidate_votes.count('Khan')
khan_percent = format((float(khan_count)/float(len(voter_id)))*100, ".3f")
print(f'Khan: {khan_percent}% ({khan_count})')
txt_file.write(f'Khan: {khan_percent}% ({khan_count})' + '\n')

correy_count = candidate_votes.count('Correy')
correy_percent = format((float(correy_count)/float(len(voter_id)))*100, ".3f")
print(f'Correy: {correy_percent}% ({correy_count})')
txt_file.write(f'Correy: {correy_percent}% ({correy_count})' + '\n')

li_count = candidate_votes.count('Li')
li_percent = format((float(li_count)/float(len(voter_id)))*100, ".3f")
print(f'Li: {li_percent}% ({li_count})')
txt_file.write(f'Li: {li_percent}% ({li_count})' + '\n')

tooley_count = candidate_votes.count("O'Tooley")
tooley_percent = format((float(tooley_count)/float(len(voter_id)))*100, ".3f")
print(f"O'Tooley: {tooley_percent}% ({tooley_count})")
txt_file.write(f"O'Tooley: {tooley_percent}% ({tooley_count})" + "\n")

# Candidate dictionary with name and voter count
candidate_count = {
    'candidates': ['Khan', 'Correy', 'Li', "O'Tooley"],
    'votes': [khan_count, correy_count, li_count, tooley_count]
    }

# Enumerate function that checks for the max of votes list in dictionary and returns the winner
print('-'*20)
txt_file.write('-'*20 + '\n')
winner_votes = max(candidate_count['votes'])
for index, winner in enumerate(candidate_count['votes']):
    if candidate_count['votes'][index] == winner_votes:
        print(f"Winner: {candidate_count['candidates'][index]}")
        txt_file.write(f"Winner: {candidate_count['candidates'][index]}" + "\n")
print('-'*20)
txt_file.write('-'*20 + '\n')