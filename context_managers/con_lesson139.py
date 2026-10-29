from contextlib import contextmanager

@contextmanager
def study_session():
    print("Entering study session")
    
    try:
        yield "Python student"
    finally:
        print("Leaving study session")

with study_session() as student:
    print(f"Welcome, {student}!")
    raise ValueError("Something went wrong")