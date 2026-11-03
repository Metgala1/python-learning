import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "My Application")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

MAX_LOGIN_ATTEMPTS = int(
    os.getenv("MAX_LOGIN_ATTEMPTS", "5")
)