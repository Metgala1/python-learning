import multiprocessing


def calculate_square(number):
    result = number * number
    print(f"{number} squared is {result}")


if __name__ == "__main__":
    process = multiprocessing.Process(
        target=calculate_square,
        args=(8,)
    )

    process.start()
    process.join()