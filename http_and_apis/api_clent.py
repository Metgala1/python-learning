
import requests


class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json"
        })

        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

    def get(self, path, params=None):
        response = self.session.get(
            f"{self.base_url}/{path.lstrip('/')}",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    def post(self, path, payload):
        response = self.session.post(
            f"{self.base_url}/{path.lstrip('/')}",
            json=payload,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    def close(self):
        self.session.close()
