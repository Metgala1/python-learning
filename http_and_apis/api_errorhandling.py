import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    
    response.raise_for_status()
    post = response.json()
    print(post["title"])
except requests.exceptions.Timeout:
    print("The server took too long to respond")
except requests.exceptions.HTTPError as error:
    print(f"HTTP error occured: {error}")
except requests.exceptions.ConnectionError:
    print("Could not connect to server")
except requests.RequestException as error:
    print(f"Unexpected request problem: {error}")