import numpy as np

sales = np.array([12000, 15000, 18000, 11000])

print(sales + 1000)
print(sales - 2000)
print(sales * 2)
print(sales / 1000)

#Element-wise operations between arrays
# When two arrays have compatible shapes, NumPy can perform arithmetic between corresponding elements.
day_1_sales = np.array([12000, 20000, 9000])
day_2_sales = np.array([15000, 22000, 11000])

difference = day_2_sales - day_1_sales
print(difference)

#Vectorization: let NumPy handle the loop
#Done without a python loop
increased_sales = sales * 1.15
print(increased_sales)

#Common mathematical functions
values = np.array([4, 9, 16, 25])

print(np.sqrt(values))

#Other useful functions:
values = np.array([1.2, 2.7, 3.5])

print(np.round(values))
print(np.floor(values))
print(np.ceil(values))

#Aggregate functions: summarize an array
sales = np.array([12000, 15000, 18000, 11000])

print(np.sum(sales))
print(np.mean(sales))
print(np.min(sales))
print(np.max(sales))

#Aggregates across rows and columns
sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000,  11000, 13000, 12000]
])
#Total sales
print(np.sum(sales))

#total per branch 
print(np.sum(sales, axis=1))

#total per day 
print(np.sum(sales, axis=0))

#Calculating percentages and growth rates
day_1 = np.array([12000, 20000, 9000])
day_2 = np.array([15000, 22000, 11000])

growth_rate = (day_2 - day_1) / day_1 * 100

print(growth_rate)

#A useful conditional tool: np.where()
sales = np.array([12000, 15000, 18000, 11000])
status = np.where(sales >= 15000, "Target met", "Below target")
#np.where(condition, value_if_true, value_if_false)
print(status)