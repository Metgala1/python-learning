class ErrorInspector:
    def __enter__(self):
        print("Entering the managed block")
        return self
    
    def __exit__(self, exec_type, exec_value, traceback):
        if exec_type is None:
            print("The block finish successfully")
        else:
            print(f"Exception type: {exec_type.__name__}")
            print(f"Execption message: {exec_value}")
        print("Cleanup is complete")
        
        return True

with ErrorInspector():
   print("No exceptions occured")


with ErrorInspector():
   raise ValueError("The supplied value is invalid")

