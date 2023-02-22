import os
import json
from authentication import Authentication

class Main:
    def __init__(self):
        with open('secrets.json') as f:
            secrets = json.load(f)
        self.username = secrets['PV_USERNAME']
        self.password = secrets['PV_PASSWORD']
        self.auth = Authentication(self.username, self.password)

    def run(self):
        self.auth.get_access_token()
        print(self.auth.access_token)


if __name__ == "__main__":
    main = Main()
    main.run()

