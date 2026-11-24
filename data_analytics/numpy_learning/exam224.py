import numpy as np


sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000, 11000, 13000, 12000]
], dtype=np.int64)

print("Sales:")
print(sales)

print("Dimensions:", sales.ndim)
print("Shape:", sales.shape)
print("Total elements:", sales.size)

print("Total sales:", np.sum(sales))
print("Sales per branch:", np.sum(sales, axis=1))
print("Sales per day:", np.sum(sales, axis=0))

print("Data type:", sales.dtype)
print("Bytes per value:", sales.itemsize)
print("Total element memory:", sales.nbytes)