import timeit

numbers = range(1000)

def using_loop():
    result = []
    
    for number in numbers:
        result.append(number * number)
    
    return result

def using_comprehension():
    return [number * number for number in numbers]

#timeit tell us how fast a piece of code takes to run
loop_time = timeit.timeit(
    using_loop,
    number=1000
)

comprehension_time = timeit.timeit(
    using_comprehension,
    number=1000
)
print("Loop: ", loop_time )
print("Comprehension:", comprehension_time)
