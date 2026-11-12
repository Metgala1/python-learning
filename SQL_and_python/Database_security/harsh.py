import bcrypt

password = "secret123"

password_bytes = password.encode("utf-8")

hashed_password = bcrypt.hashpw(
    password_bytes,
    bcrypt.gensalt()
)

print(hashed_password)