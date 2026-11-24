import numpy as np

sales = np.array([12000, 15000, np.nan, 11000])
print(sales)
#This is a useful reminder: adding NaN to a numeric array can change its dtype.
# print(sales.dtype)

#. Detecting missing values with np.isnan()
sales = np.array([12000, 15000, np.nan, 11000])

missing_mask = np.isnan(sales)
# print(missing_mask)

# np.isnan() checks each element and returns a Boolean array.
# - True means the value is NaN.
# - False means the value is not NaN.

#We can use that mask to select missing values
missing_values = sales[np.isnan(sales)]
# print(missing_values)

#Or select the values that are not missing:
valid_sales = sales[~np.isnan(sales)]

# print(valid_sales)

#Why NaN can affect calculations
#lets calculate average
sales = np.array([12000, 15000, np.nan, 11000])

print(np.mean(sales))

#Using NaN-aware functions
sales = np.array([12000, 15000, np.nan, 11000])
print(np.nanmean(sales))
print(np.nansum(sales))
print(np.nanmax(sales))

# Similarly:
# Regular function	NaN-aware version
# np.sum()	np.nansum()
# np.mean()	np.nanmean()
# np.min()	np.nanmin()
# np.max()	np.nanmax()
# np.std()	np.nanstd()
# np.var()	np.nanvar()

#Replacing missing values
sales = np.array([12000, 15000, np.nan, 11000])
clean_sales = np.nan_to_num(sales, nan=0)

# print(clean_sales)

#Handling missing values in two-dimensional arrays
sales = np.array([
    [12000, 15000, 18000, 11000],
    [20000, np.nan, 19000, 25000],
    [9000, 11000, 13000, 12000]
])

branch_averages = np.nanmean(sales, axis=1)

print(branch_averages)

#Average for each day
daily_averages = np.nanmean(sales, axis=0)

print(daily_averages)

#Counting missing values
missing_values = np.sum(np.isnan(sales))
print(missing_values)

#Count missing values per branch
missing_per_branch = np.sum(np.isnan(sales), axis=1)
print(missing_per_branch)

#Missing per day 
missing_per_day = np.sum(np.isnan(sales), axis=0)
print(missing_per_day)


#Data validation: checking whether values make sense
sales = np.array([
    [12000, 15000, -500, 11000],
    [20000, 22000, 19000, 25000],
    [9000, 11000, np.nan, 12000]
])

negative_mask = sales < 0
print(negative_mask)

invalid_values = sales[negative_mask]
print(invalid_values)

#We can also check whether every value is nonnegative:
all_nonnegative = np.all(sales >= 0)
print(all_nonnegative)

#To check whether at least one value is negative:
has_negative = np.any(sales < 0)
print(has_negative)

# A validation example
# Suppose sales must be nonnegative and no greater than 100,000 FCFA.

valid_mask = (sales >= 0) & (sales <= 100000)

print(valid_mask)

# This produces a Boolean mask indicating which values satisfy both conditions.

# We can check whether all values are valid:

print(np.all(valid_mask))