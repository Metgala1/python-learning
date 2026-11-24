import numpy as np

one_d = np.array([10,20,30,40])
two_d = np.array(
    [
        [10,20,30],
        [40,50,60]
    ]
)

three_d = np.array([
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
])


# print(one_d)
# print(two_d)
# print(three_d)

#ndim tells us how many dimension our array is

# print(one_d.ndim)
# print(two_d.ndim)
# print(three_d.ndim)

#Shape tells us the shape of our array
print(one_d.shape)
print(two_d.shape)

#size tells us the number of element in the array
print(two_d.size)

sales = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

#add the values vertically across the rows
print(np.sum(sales, axis=1))

#add the numbers horizontally across the columns 


#Creates an array filled with zeros.
zeros = np.zeros((2, 3))

print(zeros)

#Creates an array filled with ones.
ones = np.ones((2, 3))

print(ones)

#Creates an array filled with a specific value.
filled = np.full((2, 3), 7)

print(filled)

#Creates a sequence of values using a start, stop, and optional step.

filled = np.full((2, 3), 7)

print(filled)

#Creates a sequence of values using a start, stop, and optional step.
numbers = np.arange(0, 10, 2)

print(numbers)