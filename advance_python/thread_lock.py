import threading

balance = 100
balance_lock = threading.Lock()

def withdraw(amount):
    global balance
    
    with balance_lock:
       if balance >= amount:
           balance -= amount
           print(f"Withdrawn {amount}. Balance: {balance}")
       else:
           print("Insufficient funds")

threads = [
    threading.Thread(target=withdraw, args=(30,)),
    threading.Thread(target=withdraw, args=(30,))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
print(f"Final balance: {balance}")
    