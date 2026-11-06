import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    
    response.raise_for_status()
    
    post = response.json()
    print(post.get("title", "Not found"))
except requests.exceptions.Timeout:
    print("The server took too ling to respond")
except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")
except requests.ConnectionError:
    print("Could not connect to the server.")
except requests.exceptions.RequestException as error:
    print(f"Something went wrong: {error}")
    