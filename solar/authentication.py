import requests
from datetime import datetime, timedelta

URL = "https://pv.inteless.com/oauth/token"

class Authentication:
    """
    An authentication class that should be used to retrieve
    the authentication credentials needed to access the content
    in the pv.inteless website.

    Args:
        username: username for the account to be used
        password: password for the account to be used

    """
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.token_expiration = None

    def login(self) -> None:
        """
        Executes a login to the website and stores credentials.

        """
        payload = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password",
            "client_id": "csp-web"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(URL, json=payload, headers=headers)
        data = response.json()["data"]
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        expires_in = data["expires_in"]
        self.token_expiration = datetime.now() + timedelta(seconds=expires_in)

    def get_access_token(self) -> str:
        """
        Returns the current access token.

        Returns:
             The access token granted saved from the previous login() method call.
        """
        if self.access_token is None:
            self.login()
        return self.access_token

    def get_refresh_token(self) -> str:
        """
        Returns the current refresh token.

        Returns:
             The refresh token granted saved from the previous login() method call.
        """
        if self.refresh_token is None:
            self.login()
        return self.refresh_token

    def refresh_token_if_expired(self) -> None:
        """
        Refreshes the token if its expired.

        """
        if self.access_token and self.token_expiration and self.token_expiration < datetime.now():
            self.login(self)
            # need to flesh this out
            # don't see needing to actually use the refresh token
            # API with refresh token is also unknown
            # so just trigger a new login to get a new token
