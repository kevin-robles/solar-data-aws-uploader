import requests
from typing import Union

FILE_URL = "https://pv.inteless.com/api/v1/workdata/dynamic/download"
LANGUAGE = "en"
TYPE = "1"


class WebsiteConnection:
    def __init__(self, access_token, serial_number, begin_date, end_date) -> None:
        self.access_token = access_token
        self.serial_number = serial_number
        self.begin_date = begin_date
        self.end_date = end_date

    def generate_retrieval_url(self) -> str:
        return FILE_URL  # plus logic

    def get_file(self) -> Union[bytes, None]:
        payload = {
            "sn": self.serial_number,
            "date_range": f"{self.begin_date},{self.end_date}",
            "type": TYPE,
            "lan": LANGUAGE
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(FILE_URL, params=payload, headers=headers)
        if response.status_code == 200:
            filename = f"{self.serial_number}_{self.begin_date}_{self.end_date}.csv"
            with open(filename, "wb") as f:
                f.write(response.content)
            return filename
        else:
            raise Exception("Failed to retrieve file")

