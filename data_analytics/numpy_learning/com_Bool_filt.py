import numpy as np

sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000, 11000, 13000, 12000]
])

result = sales > 15000

high_sales =  sales[sales > 15000]
# sales > 15000 creates a Boolean mask.
# NumPy checks the mask against the original array.
# It selects the values at positions where the mask is True.
# The selected values are returned in a new one-dimensional array.

print(high_sales)

#Filtering 
selected_sales = sales[(sales > 12000) & (sales < 20000)]
print(selected_sales)

#OR: either condition can be true

selected_sales = sales[(sales < 10000) | (sales > 20000)]
print(selected_sales)