import os
import json
import pathlib as pl
from authentication import Authentication


class Main:
    def __init__(self):
        base_dir = pl.Path(__file__).parent.parent
        final_path = os.path.join(base_dir, 'secrets.json')
        with open(final_path) as f:
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

