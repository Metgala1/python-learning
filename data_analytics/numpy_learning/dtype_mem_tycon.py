quantity = 12        # integer
price = 19.99        # floating-point number
product_name = "Tea" # string
is_available = True  # boolean

print(type(quantity))      # <class 'int'>
print(type(price))         # <class 'float'>
print(type(product_name))  # <class 'str'>
print(type(is_available))  # <class 'bool'>

import numpy as np

quantities = np.array([10, 20, 30])
prices = np.array([19.99, 24.50, 12.75])

#maxing int and float will convert the int into a float 
values = np.array([10, 20.5, 30])

print(values)
print(values.dtype)

#Mixing a numbers and strings, numpy will convert the numbers into string
values = np.array([10, 20, "30"])

print(values)
print(values.dtype)

#Signed and unsigned integers
#A signed integer can represent negative and positive whole numbers.
#An unsigned integer can represent only zero and positive whole numbers.

signed_values = np.array([-10, 0, 10], dtype=np.int8)
unsigned_values = np.array([0, 10, 200], dtype=np.uint8)

# print(np.iinfo(np.int8).min)
# print(np.iinfo(np.int8).max)

# print(np.iinfo(np.uint8).min)
# print(np.iinfo(np.uint8).max)

sales_32 = np.zeros(1_000_000, dtype=np.float32)
sales_64 = np.zeros(1_000_000, dtype=np.float64)

print(sales_32.nbytes)
print(sales_64.nbytes)

#Converting an array with astype()
quantities = np.array([10.5, 20.8, 30.2])

whole_quantity = quantities.astype(np.int64)

print(whole_quantity)

#convertion a numeric into text

prices_as_text = np.array(["19.99", "24.50", "12.75"])

prices = prices_as_text.astype(np.float64)

print(prices)
print(prices.dtype)