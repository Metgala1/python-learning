import numpy as np

sales = np.array([
    12000, 15000, 18000, 11000,
    20000, 22000, 19000, 25000,
    9000, 11000, 13000, 12000
])

print(sales.shape)

sales_by_branch = sales.reshape(3, 4)

print(sales_by_branch)

#Sometimes you know the number of rows but don't want to calculate the number of columns yourself.
#NumPy allows one dimension to be -1, meaning: “calculate this dimension automatically.”
sales_by_branch = sales.reshape(3, -1)
print(sales_by_branch)

#NumPy can reshape data into 3D arrays too.
print()

sales = np.array([
    100, 200, 150, 250, 300, 350,
    400, 500, 450, 550, 600, 650
])

sales_3d = sales.reshape(2,3,2)
print(sales_3d)
print(sales_3d.shape)

#Transposing: swapping rows and columns
sales = np.array([
    [12000, 15000, 18000],
    [20000, 22000, 19000]
])

print(sales.shape)

transposed_sales = sales.T
print(transposed_sales)

#Combining arrays with np.concatenate()
branch_0 = np.array([12000, 15000, 18000])
branch_1 = np.array([20000, 22000, 19000])
branch_2 = np.array([9000, 11000, 13000])

all_sales = np.concatenate([
    branch_0,
    branch_1,
    branch_2
])

print(all_sales)

#Combining 2D arrays by rows
branch_0 = np.array([[12000, 15000, 18000]])
branch_1 = np.array([[20000, 22000, 19000]])

combined = np.concatenate([branch_0, branch_1], axis=0)



#A simpler way to stack arrays
# NumPy also provides np.vstack() and np.hstack().

branch_0 = np.array([12000, 15000, 18000])
branch_1 = np.array([20000, 22000, 19000])

combined = np.vstack([branch_0, branch_1])


#np.hstack()
first_half = np.array([12000, 15000])
second_half = np.array([18000, 11000])

combined = np.hstack([first_half, second_half])

print(combined)