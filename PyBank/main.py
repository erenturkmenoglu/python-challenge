import os
import csv

prompt = input("Select the file to open: (1) budget_data_1.csv or (2) budget_data_2.csv : ")
if prompt == "1":
    filepath = "budget_data_1.csv"
    output_path = "output_1.txt"
elif prompt == "2":
    filepath = "budget_data_2.csv"
    output_path = "output_2.txt"
    pass

date = []
revenue = []
change = []
count_months = 0
sum = 0
total_change = 0
avg_revenue_change = 0
increase = 0
decrease = 0

with open(filepath, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
        count_months += 1
        sum += int(row[1])
        

i = 0
j = 1
delta = 0    
for i in range(count_months-1):
    delta = int(revenue[j]) - int(revenue[i])
    change.append(delta)
    total_change += delta
    i +=1
    j +=1

GreatestIncrease = 0          

for changes in change:
    if GreatestIncrease < changes:
        GreatestIncrease = changes
        GreatestIncreaseIndex = change.index(changes) + 1

GreatestDecrease = 0
for changes in change:
    if GreatestDecrease > changes:
        GreatestDecrease = changes
        GreatestDecreaseIndex = change.index(changes) + 1

avg_revenue_change = total_change / (count_months - 1)

with open(output_path, "w", newline='') as textfile:
    print("Financial Analysis", file=textfile)
    print("-----------------------------------------------", file=textfile)
    print(f'Total Months: {count_months}', file=textfile)
    print(f'Total Revenue: ${sum}', file=textfile)
    print(f'Average Revenue Change: ${round(avg_revenue_change, 2)}', file=textfile)
    print(f'Greatest Increase in Revenue: {date[GreatestIncreaseIndex]} (${GreatestIncrease})', file=textfile)
    print(f'Greatest Decrease in Revenue: {date[GreatestDecreaseIndex]} (${GreatestDecrease})', file=textfile)
    print("-----------------------------------------------", file=textfile)
      
with open(output_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)
      
