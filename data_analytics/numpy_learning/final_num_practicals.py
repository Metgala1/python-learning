import numpy as np


sales = np.array([
    [12000, 15000, 18000, 21000],  # Branch A
    [10000, 13000, 17000, 16000],  # Branch B
    [15000, 14000, 19000, 22000],  # Branch C
])

print(sales)
print(sales.shape)

#calculate each branch total
branch_total = np.sum(sales, axis=1)
print(branch_total)

print()
#Calculate each day total
daily_total = np.sum(sales, axis=0)
print(daily_total)

#find the highest selling branch
best_branch_index = np.argmax(branch_total)
print(sales[best_branch_index])

#find days with sales of atleast 18000
high_sales = sales >= 18000
print(high_sales)

#Count how many individual sales meet the condition
print(np.sum(high_sales))

#Calculate the average for each branch
average_per_branch = np.mean(sales, axis=1)
print(average_per_branch)

print()
print()

import numpy as np

sales = np.array([
    [12000, 15000, 18000, 21000],
    [10000, 13000, 17000, 16000],
    [15000, 14000, 19000, 22000],
])

branch_totals = np.sum(sales, axis=1)
branch_averages = np.mean(sales, axis=1)
day_totals = np.sum(sales, axis=0)

best_branch_index = np.argmax(branch_totals)
best_branch_total = branch_totals[best_branch_index]

print("Branch totals:", branch_totals)
print("Branch averages:", branch_averages)
print("Day totals:", day_totals)
print("Best branch index:", best_branch_index)
print("Best branch total:", best_branch_total)
print("Sales >= 18000:", sales[sales >= 18000])