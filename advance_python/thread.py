import threading
import time 

def download_file(filename):
    print(f"Downloading {filename}...")
    time.sleep(2)
    print(f"Finised downloading {filename}")

thread_one = threading.Thread(
    target=download_file,
    args=("photo.jpg",)
)

thread_two = threading.Thread(
    target=download_file,
    args=("document.pdf",)
)

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

print("All downloads finished!")