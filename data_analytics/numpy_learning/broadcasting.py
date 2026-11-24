#Broadcasting is NumPy's way of performing operations between arrays of different shapes when those shapes are compatible.
import numpy as np

sales = np.array([100, 200, 300])

result = sales + 10

print(result)

#Broadcasting with two-dimensional arrays
sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, 22000, 19000, 25000],
    [9000, 11000, 13000, 12000]
])

print(sales.shape)

adjusted_sales = sales + 1000


#Broadcasting arrays with different shapes
# Now let's make it more interesting.

# Suppose the company offers different promotional bonuses depending on the day:

# Sales:
# Branch 1: [12000, 15000, 18000, 11000]
# Branch 2: [20000, 22000, 19000, 25000]
# Branch 3: [ 9000, 11000, 13000, 12000]

# Daily bonus:
#           [    0,  1000,   500,  2000]

daily_bonus = np.array([0, 1000, 500, 2000])
adjusted_sales = sales + daily_bonus

print(adjusted_sales)

# Broadcasting is NumPy's way of combining arrays of different shapes without a loop and without making you copy data by hand. It does this by virtually "stretching" the smaller array so the two shapes match.

# The procedure
# Right-align the two shapes and compare them dimension by dimension, starting from the last one.
# If one shape is shorter, pad it on the left with 1s until both have the same number of dimensions.
# For each pair of dimensions, they're compatible if they're equal or one of them is 1.
# If every pair is compatible, the result's dimension in each position is the larger of the two. A dimension of 1 gets stretched to match the other. If any pair fails, NumPy raises an error.

# Here's a sample array to use in the examples (3 days × 4 stores):

# python
# sales = np.array([[100, 200, 300, 400],
#                   [500, 600, 700, 800],
#                   [900, 1000, 1100, 1200]])   # shape (3, 4)
# Example A: (3, 4) and (4,)
# python
# bonus = np.array([1, 2, 3, 4])   # shape (4,)
# print(sales + bonus)

# Right-aligned:

# sales:  (3, 4)
# bonus:  (   4)   → padded to (1, 4)
# 4 and 4 are equal.
# 3 and 1: one is 1, so it's compatible.

# The result shape is (3, 4). The single row [1, 2, 3, 4] is stretched down across all 3 rows:

# [[ 101,  202,  303,  404],
#  [ 501,  602,  703,  804],
#  [ 901, 1002, 1103, 1204]]

# This is the typical case where you add a per-store value to every day.

# Example B: (3, 4) and (3, 1)
# python
# day_bonus = np.array([[10], [20], [30]])   # shape (3, 1)
# print(sales + day_bonus)
# sales:      (3, 4)
# day_bonus:  (3, 1)
# 4 and 1: compatible, because one is 1.
# 3 and 3: equal.

# Here the column is stretched sideways across all 4 columns, so each row gets its own value added:

# [[ 110,  210,  310,  410],
#  [ 520,  620,  720,  820],
#  [ 930, 1030, 1130, 1230]]

# That's a per-day value applied to every store.

# Example C: (3, 4) and (3,) is not compatible
# python
# bad = np.array([10, 20, 30])   # shape (3,)
# sales + bad   # ValueError
# sales:  (3, 4)
# bad:    (   3)   → padded to (1, 3)

# The last dimensions are compared first: 4 vs 3. They're unequal and neither is 1, so NumPy raises: operands could not be broadcast together with shapes (3,4) (3,).

# The trap is that the 3 looks like it should line up with the 3 rows, but padding always happens on the left, so the 3 ends up facing the 4 columns. If you meant a per-day value, turn it into a column:

# python
# sales + bad.reshape(3, 1)     # or bad[:, np.newaxis]

# That makes it shape (3, 1), which is Example B.

# Example D: (3, 4) and (2, 4) is not compatible
# sales:  (3, 4)
# other:  (2, 4)
# 4 and 4: fine.
# 3 and 2: unequal, and neither is 1. This fails.

# Only dimensions of 1 can be stretched. A dimension of 2 can't be stretched to 3, because NumPy has no sensible way to repeat 2 items across 3 slots.

# Why right to left?

# NumPy treats the last axis as the "innermost" one, where neighbouring values sit together. In (3, 4), the 4 is the columns inside each row. Matching from the right makes a plain 1-D array like [1, 2, 3, 4] line up with the columns, which is the case you want most of the time. If NumPy matched from the left, the 4-item array would be compared against the 3 rows and fail.

# A quick checklist
# Write the two shapes one under the other, right-aligned.
# Fill empty spots on the left with 1.
# Check every column: equal, or one is 1.
# If all pass, the result takes the larger number in each column.
# Shapes	Result
# (3, 4) and (4,)	(3, 4)
# (3, 4) and (3, 1)	(3, 4)
# (3, 1) and (1, 4)	(3, 4)
# (3, 4) and (3,)	error
# (3, 4) and (2, 4)	error

# The third row is worth noticing: both arrays get stretched, and the result is a full grid. That's how you build things like multiplication tables with no loop.

# Stretching is virtual. NumPy doesn't actually copy the small array into a bigger one in memory, so broadcasting is fast and cheap on memory, as well as convenient.