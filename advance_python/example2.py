import multiprocessing

def calculate_squares(number):
    return number * number

if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25, 30]
    
    with multiprocessing.Pool(processes=3) as pool:
        process = pool.map(calculate_squares, numbers)
        
    print(process)