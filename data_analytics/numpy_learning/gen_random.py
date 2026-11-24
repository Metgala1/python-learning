import numpy as np

#How to generate random numbers
print(np.random.rand())


print()
#Generate random array
random_numbers = np.random.rand(10)
# print(random_numbers)

#Generate 2d array
random_matrix = np.random.rand(3, 4)
# print(random_matrix)

#Generate random int
random_sales = np.random.randint(1000, 10000, size=10)
#This generates ten random integers between 1,000 and 9,999
# print(random_sales)

#Generating a 2d int
random_sales = np.random.randint(5000, 30000, size=(3,4))

#Understanding random seeds
# A random seed is an initial value used to initialize a random-number generator.
# When you use the same seed with the same generator, you get the same sequence of random numbers.

np.random.seed(42)

sales = np.random.randint(5000, 30000, size=(3,4))


#The modern NumPy random generator
#Instead of relying on the older global random state:
np.random.seed(42)
np.random.randint(1, 100, size=5)

#Create a dedicated random generator:
rng = np.random.default_rng(42)
sales = rng.integers(5000, 30000, size=(3,4))

print(sales)

# For example:
rng_sales = np.random.default_rng(42)
rng_customers = np.random.default_rng(100)

sales = rng_sales.integers(5000, 30000, size=5)
customers = rng_customers.integers(10, 100, size=5)

# Each generator has its own state.

# For the rest of this course, we'll primarily use np.random.default_rng()

#Generate random floating-point values in a specific range
rng = np.random.default_rng(42)
sales = rng.uniform(5000, 30000, size=5)


#Generate normally distributed data
#A normal distribution is a probability distribution that forms a bell-shaped curve. Values near the average are more common, while values far from the average are less common.

#Example
rng = np.random.default_rng(42)
customer_spending = rng.normal(
    loc=15000,
    scale=3000,
    size=10
)

print(customer_spending)

#Build our simulated Business Sales Analytics dataset

rng = np.random.default_rng(42)

sales = rng.integers(
    5000,
    30000,
    size=(3, 7)
)

print("Sales data:")
print(sales)

print("\nBranch totals:")
print(np.sum(sales, axis=1))

print("\nDaily totals:")
print(np.sum(sales, axis=0))

print("\nHighest sale:")
print(np.max(sales))

#Notice how we're combining multiple NumPy skills:
# - Random data generation.
# - Two-dimensional arrays.
# - Array shapes.
# - Aggregation.
# - Axis calculations.
# - Finding maximum values.