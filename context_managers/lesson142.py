from contextlib import contextmanager

@contextmanager
def study_session():
    print("Starting session")
    
    try:
        yield "Javascript developer"
    finally:
        print("Ending session")

with study_session() as person:
    print(f"You are a {person}")
    raise ValueError("Something went wrong")