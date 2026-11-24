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
print(np.min(sales))
print(np.max(sales))

#Calculate the min and max along and axis
print(np.min(sales, axis=1))
print(np.max(sales, axis=0))

print()

print(np.min(sales, axis=0))

#Finding the position of the maximum or the minimum
daily_sales = np.array([12000, 15000, 18000, 11000])

highest_position = np.argmax(daily_sales)
lowest_position = np.argmin(daily_sales)

highest_value = daily_sales[highest_position]
lowest_value = daily_sales[lowest_position]

print(highest_position)
print(lowest_position)
print(highest_value)
print(lowest_value)

#Finding the highest-sales day for each branch
sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000, 11000, 13000, 12000]
])

highest_day_positions = np.argmax(sales, axis=1)

print(highest_day_positions)

#.Finding a specific value

sales = np.array([18000, 12000, 25000, 15000, 22000])
position = np.where(sales == 25000)[0]
print(position)

#Getting the top three sales values
sales = np.array([18000, 12000, 25000, 15000, 22000])

top_three = np.sort(sales)[::-1][:3]

print(top_three)
