import requests

payload = {
    "title": "Learning Python",
    "body": "I am learning how to communicate with APIs.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

print(response.status_code)
print(response.json())