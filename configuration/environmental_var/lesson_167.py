import os

from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
debug = os.getenv("DEBUG")

print(type(app_name))
print(type(debug))
