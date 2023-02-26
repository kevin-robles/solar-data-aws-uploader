import json
import pathlib
from authentication import Authentication
from website_connection import WebsiteConnection
from datetime import datetime, timedelta
from s3_uploader import S3Uploader

class Main:
    def __init__(self):
        base_dir = pathlib.Path(__file__).parent.parent
        final_path = base_dir / 'secrets.json'

        with open(final_path) as f:
            secrets = json.load(f)

        self.username = secrets['PV_USERNAME']
        self.password = secrets['PV_PASSWORD']
        self.serial_number = secrets['PV_SERIAL_NUMBER']
        self.auth = Authentication(self.username, self.password)
        self.s3_bucket_name = secrets['S3_BUCKET_NAME']

    def run(self):
        self.auth.get_access_token()
        access_token = self.auth.access_token
        today = datetime.now().date().isoformat()
        yesterday = (datetime.now() - timedelta(days=1)).date().isoformat()
        file_generator = WebsiteConnection(access_token, self.serial_number, yesterday, today)
        file = file_generator.get_file()
        bucket = S3Uploader(self.s3_bucket_name)
        bucket.upload_file(file, f"{self.serial_number}_{yesterday}_{today}.xlsx")


if __name__ == "__main__":
    main = Main()
    main.run()

