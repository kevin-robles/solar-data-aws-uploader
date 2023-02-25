import os
import json
import pathlib as pl
from authentication import Authentication
from website_connection import WebsiteConnection
from datetime import datetime, timedelta

class Main:
    def __init__(self):
        base_dir = pl.Path(__file__).parent.parent
        final_path = os.path.join(base_dir, 'secrets.json')
        with open(final_path) as f:
            secrets = json.load(f)
        self.username = secrets['PV_USERNAME']
        self.password = secrets['PV_PASSWORD']
        self.serial_number = secrets['PV_SERIAL_NUMBER']
        self.auth = Authentication(self.username, self.password)

    def run(self):
        self.auth.get_access_token()
        access_token = self.auth.access_token
        today = datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        file_generator = WebsiteConnection(access_token, self.username, self.password, today, yesterday)
        file = file_generator.get_file()


if __name__ == "__main__":
    main = Main()
    main.run()

