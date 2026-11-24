import numpy as np

sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000,  11000, 13000, 12000]
])

print(sales[0,0])
print(sales[1,2])
print(sales[2,3])

#Select a whole column
# day_2_sales = sales[:, 1]
# print(day_2_sales)

# day_1_sales = sales[:, 0]
# print(day_1_sales)

# print(sales[0, :])

#Slice rows and columns together

first_two_branches = sales[:2, 1:3]
print(first_two_branches)

#cpoy

sales = np.array([12000, 15000, 18000, 11000])

first_two = sales[:2]

first_two[0] = 999

print(first_two)
print(sales)

#independt copy
sales = np.array([12000, 15000, 18000, 11000])

first_two = sales[:2].copy()
first_two[0] = 999

print(first_two)
print(sales)

#Boolean indexing: select values that meet a condition
sales = np.array([12000, 15000, 18000, 11000, 20000])

highest_sales = sales[sales > 15000]
print(highest_sales)

sales_between = sales[(sales >= 15000) & (sales <= 18000)]
print(sales_between)

# This selects values below 12000 or above 18000.

# For Boolean indexing, remember:
# - & means element-wise AND.
# - | means element-wise OR.
# - ~ means element-wise NOT.
# - Put each comparison in parentheses.
