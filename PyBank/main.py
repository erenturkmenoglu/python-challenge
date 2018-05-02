import os
import csv

filepath = input("Name of the file:")

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

print("Financial Analysis")
print("-----------------------------------------------")
print(f'Total Months: {count_months}')
print(f'Total Revenue: ${sum}')
print(f'Average Revenue Change: ${round(avg_revenue_change, 2)}')
print(f'Greatest Increase in Revenue: {date[GreatestIncreaseIndex]} (${GreatestIncrease})')
print(f'Greatest Decrease in Revenue: {date[GreatestDecreaseIndex]} (${GreatestDecrease})')
        

