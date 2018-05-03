import os
import csv

prompt = input("Select file: (1) election_data_1.csv or (2) election_data_2.csv : ")
if prompt == "1":
    filepath = "election_data_1.csv"
    output_path = "output_1.txt"
elif prompt == "2":
    filepath = "election_data_2.csv"
    output_path = "output_2.txt"

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

with open(output_path, "w", newline='') as textfile:
    print("Election Results", file=textfile)
    print("-----------------------------------", file=textfile)
    print(f'Total Votes: {count_votes}', file=textfile)
    print("-----------------------------------", file=textfile)
    for i in range(count_candidates):
        print(f'{results[i]}: {round(percentage[i], 2)}% ({votes[i]})', file=textfile)
    print("-----------------------------------", file=textfile)
    winner = results[votes.index(max(votes))]
    print(f'Winner: {winner}', file=textfile)
    print("-----------------------------------", file=textfile)

with open(output_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)