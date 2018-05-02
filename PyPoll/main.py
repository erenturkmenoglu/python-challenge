import os
import csv

prompt = input("Select file: (1) election_data_1.csv or (2) election_data_2.csv : ")
if prompt == "1":
    filepath = "election_data_1.csv"
elif prompt == "2":
    filepath = "election_data_2.csv"

candidate = []
results = []
votes = []
percentage = []
count_votes = 0
count_candidates = 0

with open(filepath, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        candidate.append(row[2])
        count_votes += 1

for x in set(candidate):
    results.append(x)
    votes.append(candidate.count(x))
    percentage.append((candidate.count(x)/count_votes)*100)
    count_candidates += 1

print("Election Results")
print("-----------------------------------")
print(f'Total Votes: {count_votes}')
print("-----------------------------------")
for i in range(count_candidates):
    print(f'{results[i]}: {round(percentage[i], 2)}% ({votes[i]})')
print("-----------------------------------")
winner = results[votes.index(max(votes))]
print(f'Winner: {winner}')
print("-----------------------------------")

        

