import numpy as np

daily_sales = np.array([
    12000,
    15000,
    18000,
    11000,
    20000,
    25000,
    22000
])

total_sales = np.sum(daily_sales)
highest_sales = np.max(daily_sales)
average_sales = np.mean(daily_sales)
lowest_sales = np.min(daily_sales)

print("Total:", total_sales)
print("Average:", average_sales)
print("Highest:", highest_sales)
print("Lowest:", lowest_sales)