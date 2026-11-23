import time

def load_data():
    time.sleep(1)

def process_data():
    time.sleep(2)

def save_data():
    time.sleep(1)

def main():
    load_data()
    process_data()
    save_data()
    
    print("Test completed")

main()


#use python3 -m cProfile -s cumulative -module_name to profile a module