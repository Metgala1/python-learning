import multiprocessing

def calculate_square(number):
    return number * number


if __name__ == "__main__":
    numbers = [2,4,6,8,10]
    
    with multiprocessing.Pool(processes=3) as pool:
        result = pool.map(calculate_square, numbers)
    
    print(result)