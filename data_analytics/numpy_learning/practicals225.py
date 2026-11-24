import numpy as np

branch_0 = np.array([12000, 15000, 18000, 11000])
branch_1 = np.array([20000, 22000, 19000, 25000])
branch_2 = np.array([9000, 11000, 13000, 12000])

sales = np.vstack([
    branch_0,
    branch_1,
    branch_2
])

print(sales)
print("Shape", sales.shape)
print("Total sales:", np.sum(sales))

branch_total = np.sum(sales, axis=1)
print(branch_total)

#daily total 
daily_total = np.sum(sales, axis=0)
print(daily_total)

#Transpose 
sales_by_day = sales.T
print(sales_by_day)