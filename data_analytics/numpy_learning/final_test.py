import numpy as np

sales = np.array([
    [12000, 15000, 18000, 21000, 16000],
    [10000, 13000, 17000, 16000, 14000],
    [15000, 14000, 19000, 22000, 25000],
    [11000, 12000, np.nan, 17000, 19000],
], dtype=np.float64)

branches = np.array(["Branch A", "Branch B", "Branch C", "Branch D"])

# Task 1: Dataset information
shape = sales.shape
elements = sales.size
memory = sales.nbytes

# Task 2: Branch performance (axis=1 -> across days, one result per branch)
branch_totals = np.nansum(sales, axis=1)
branch_averages = np.nanmean(sales, axis=1)
best_branch_index = np.argmax(branch_totals)

# Task 3: Daily performance (axis=0 -> down branches, one result per day)
daily_totals = np.nansum(sales, axis=0)
best_day_index = np.argmax(daily_totals)

# Task 4: Filtering (comparisons with NaN return False, so NaN is ignored)
high_sales = sales[sales >= 18000]
count_high = high_sales.size
count_low = np.count_nonzero(sales < 15000)

# Task 5: Validation
missing_count = np.count_nonzero(np.isnan(sales))
any_negative = np.any(sales < 0)
available = sales[~np.isnan(sales)]
all_non_negative = np.all(available >= 0)

# Task 6: Business adjustment (NaN * 1.05 stays NaN; original is untouched)
adjusted_sales = sales * 1.05
adjusted_averages = np.nanmean(adjusted_sales, axis=1)

# Output
print("DATASET INFORMATION")
print("Shape:", shape)
print("Elements:", elements)
print("Memory:", memory, "bytes")

print("\nBRANCH PERFORMANCE")
print("Branch totals:", branch_totals)
print("Branch averages:", branch_averages)
print(f"Best branch: {branches[best_branch_index]} ({branch_totals[best_branch_index]:,.0f})")

print("\nDAILY PERFORMANCE")
print("Daily totals:", daily_totals)
print(f"Best day: Day {best_day_index + 1} ({daily_totals[best_day_index]:,.0f})")

print("\nSALES FILTERING")
print("Sales >= 18000:", high_sales)
print("Count >= 18000:", count_high)
print("Count below 15000:", count_low)

print("\nDATA VALIDATION")
print("Missing values:", missing_count)
print("Any negative sales:", any_negative)
print("All available sales non-negative:", all_non_negative)

print("\nADJUSTED SALES")
print("Adjusted array:\n", adjusted_sales)
print("Adjusted branch averages:", adjusted_averages)