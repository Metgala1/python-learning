import tracemalloc


tracemalloc.start()
#first is a list and it stores all value resulting to more memory
numbers = [number * 2 for number in range(1_000_000)]

#this is a generator that yields values and results to less memory usage
numbers = (number * 2 for number in range(1_000_000))

#But generators aren’t always the best choice. If you need to access the same values repeatedly by index, a list may be more appropriate.

current, peak = tracemalloc.get_traced_memory()

print("Current memory:", current)
print("Peak memory:", peak)

tracemalloc.stop()

# The optimization workflow
# When a program is slow, use this sequence:
# 1. Define the problem. Is it slow, memory-heavy, or both?
# 2. Measure it. Use a benchmark or profiler.
# 3. Find the bottleneck. Identify the operation responsible for most of the cost.
# 4. Make one change. Avoid changing five things at once.
# 5. Measure again. Confirm whether the change actually helped.
# 6. Check correctness. Faster code is useless if it produces the wrong result.
# A good optimization improves something measurable without making the code unnecessarily complicated.