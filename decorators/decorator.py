def announce(message):
    def decorator(original_function):
        def wrapper():
            print(f"{message}: Starting")
            original_function()
            print(f"{message}: Finished")
            
        return wrapper
    
    return decorator

@announce("Backup")
def backup_file():
    print("Backing up files...")

@announce("payment")
def  process_payment():
    print("Processing payment")

backup_file()
print()
process_payment()