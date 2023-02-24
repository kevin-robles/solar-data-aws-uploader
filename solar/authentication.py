import requests
from datetime import datetime, timedelta

class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.token_expiration = None

    def login(self):
        url = "https://pv.inteless.com/oauth/token"
        payload = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password",
            "client_id": "csp-web"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()["data"]
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        expires_in = data["expires_in"]
        self.token_expiration = datetime.now() + timedelta(seconds=expires_in)

    def get_access_token(self):
        if self.access_token is None:
            self.login()
        return self.access_token

    def get_refresh_token(self):
        if self.refresh_token is None:
            self.login()
        return self.refresh_token

    def refresh_token_if_expired(self):
        if self.access_token and self.token_expiration and self.token_expiration < datetime.now():
            self.get_access_token()
            # need to flesh this out
