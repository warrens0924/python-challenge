import os
import csv

#path
voter_csv = os.path.join('election_data.csv')

#empty dictionary
vote_count = {}

vote_per = {}

#variable
vote_total = 0

with open(voter_csv, newline="") as csvfile:
    voterreader = csv.reader(csvfile, delimiter=",")

    #skip header 
    next(voterreader)

    #loop
    for row in voterreader:

        #count total votes
        vote_total += 1

        #count votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1

         #not in dictionary, add them and set value as 1
        else:
            vote_count[row[2]] = 1

#variable
winner_count = 0

#loop to find winner
for candidate in vote_count:
    
    #store vote percentage
    vote_per[candidate] = (vote_count[candidate] / vote_total) * 100

    #winner
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate

#write to a text file
results_path = os.path.join('election_results.txt')

with open(results_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {vote_total}
-------------------------\n''')

    print(f'''\nElection Results
-------------------------
Total Votes: {vote_total}
-------------------------''')

    for candidate, votes in vote_count.items():
        txtfile.write(f'{candidate}: {vote_per[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {vote_per[candidate]:.3f}% ({votes})''')
    
    txtfile.write(f'''-------------------------
Winner: {winner}
-------------------------''')

    print(f'''-------------------------
Winner: {winner}
-------------------------''')
