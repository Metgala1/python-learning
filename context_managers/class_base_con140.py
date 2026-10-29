class StudySession:
    def __init__(self, student):
        self.student =  student
    def __enter__(self):
        print("Preparing the study sesion")
        return self.student
    
    def __exit__(self, exec_type, exec_value, traceback):
        print("Cleaning up the study session")

with StudySession("Javascript student") as student:
    print(f"Welcome, {student}")
    raise ValueError("The study session crashed")