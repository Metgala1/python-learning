import threading
import time

def task():
    print("Starting message")
    time.sleep(1)
    print("Finishing message")

threads = [
    threading.Thread(target=task),
    threading.Thread(target=task),
    threading.Thread(target=task)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
print("All tasks completed!")