import asyncio


# async def download_file(filename):
#     print(f"Downloading {filename}...")
#     await asyncio.sleep(2)
#     print(f"{filename} downloaded!")


# async def main():
#     task_one = asyncio.create_task(
#         download_file("photo.jpg")
#     )

#     task_two = asyncio.create_task(
#         download_file("document.pdf")
#     )

#     task_three = asyncio.create_task(
#         download_file("video.mp4")
#     )

#     await task_one
#     await task_two
#     await task_three

#     print("All downloads completed!")


# asyncio.run(main())


#Instead of manually creating and awaiting each task, we can write:

# async def download_file(filename):
#     print(f"Downloading {filename}")
#     await asyncio.sleep(2)
#     print("f{filename} downloaded!")

# async def main():
#     async with asyncio.TaskGroup() as group:
#         group.create_task(
#             download_file("photo.jpg")
#         )
        
#         group.create_task(
#             download_file("document.pdf")
#         )
        
#         group.create_task(
#             download_file("video.mp4")
#         )
#     print("All downloads completed")
    
# asyncio.run(main())

#Using async lock

# balance = 100
# balance_lock = asyncio.Lock()

# async def withdraw(amount):
#     global balance
    
#     async with balance_lock:
#         print("Processing withdrawal...")
        
#         current = balance
        
#         await asyncio.sleep(5)
        
#         new_balance = current - amount
#         balance = new_balance
        
#         print(f"New balance: {balance}")

# async def main():
#     await asyncio.gather(
#         withdraw(30),
#         withdraw(30)
#     )
    
#     print(f"Final balance: {balance}")

# asyncio.run(main())

#If you want multiple downloads at a time use semaphores

# semephore = asyncio.Semaphore(2)
# #This determine the size of the coroutine that should run at once

# async def download_file(filename):
#     async with  semephore:
#         print(f"Downloading {filename}...")
        
#         await asyncio.sleep(2)
        
#         print(f"{filename} downloaded!")
        

# async def main():
#     files = [
#         "photo.jpg",
#         "document.pdf",
#         "video.mp4",
#         "music.mp3",
#         "report.pdf"
#     ]
    
#     await asyncio.gather(
#         *(download_file(filename) for filename in files)
#     )

# asyncio.run(main())

#Enforce timeout

# async def fetch_data():
#     print("Fetching data...")
    
#     await asyncio.sleep(10)
    
#     return "Data received"

# async def main():
#     try:
#         async with asyncio.timeout(3):
#             result = await fetch_data()
#             print(result)
#     except TimeoutError:
#         print("The operation took too long")
        
# asyncio.run(main())

#cancel ansycrhonous operation 

async def background_task():
    try:
        while True:
            print("Background task running")
            await asyncio.sleep(1)
            
    except asyncio.CancelledError:
        print("Background task was cancelled!")
        raise

async def main():
    task = asyncio.create_task(background_task())
    
    await  asyncio.sleep(5)
    print("Requesting cancellation")
    
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Cancellation handled by main!")

asyncio.run(main())    