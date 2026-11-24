import numpy as np
#Sorting an array

sales = np.array([18000, 12000, 25000, 15000, 22000])

sorted_sales = np.sort(sales)

print(sorted_sales)

#Decending order
#The [::-1] slice reverses the array.
decending_sales = np.sort(sales)[::-1]

print(decending_sales)

#Sorting a two-dimensional array

sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000, 11000, 13000, 12000]
])

print(np.sort(sales, axis=1))
