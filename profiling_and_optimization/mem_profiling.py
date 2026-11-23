import tracemalloc


tracemalloc.start()
#first is a list and it stores all value resulting to more memory
numbers = [number * 2 for number in range(1_000_000)]

#this is a generator that yields values and results to less memory usage
numbers = (number * 2 for number in range(1_000_000))

current, peak = tracemalloc.get_traced_memory()

print("Current memory:", current)
print("Peak memory:", peak)

tracemalloc.stop()