import timeit
import numpy as np

#Measure performance instead of guessing
sales = np.arange(1_000_000)

def using_loop():
    result = []
    for sale in sales:
        result.append(sale * 1.1)
    
    return result

def using_numpy():
    return sales * 1.1

loop_time = timeit.timeit(
    using_loop,
    number=3
)

numpy_time = timeit.timeit(
    using_numpy,
    number=3
)

print("Loop time:", loop_time)
print("numpy time:", numpy_time)

