from api_clent import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

try:
    users = client.get("/users")
    
    print(users[0]["name"])
    
    new_post = client.post("/posts", {
        "title": "Learning Python",
        "Body": "Building a resuable API client",
        "userId": 1
    })
    
    print(new_post)
finally:
    client.close()
