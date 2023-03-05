import requests
from io import BytesIO
from typing import Union

FILE_URL = "https://pv.inteless.com/api/v1/workdata/dynamic/download"
LANGUAGE = "en"
TYPE = "1"


class WebsiteConnection:
    """
    This class is used to retrieve the file from the website.

    Args:
        access_token: access token from website's oauth2
        serial_number: the serial number of the inverter that streams the data
        begin_date: The date from which to start retrieving data
        end_date: The date from which to finish retrieving data

    """
    def __init__(self, access_token, serial_number, begin_date, end_date) -> None:
        self.access_token = access_token
        self.serial_number = serial_number
        self.begin_date = begin_date
        self.end_date = end_date

    def get_file(self) -> Union[bytes, None]:
        """
        Retrieves file from the website.

        :return: An object wrapped in BytesIO to maintain the object as a file.
        """
        payload = {
            "sn": self.serial_number,
            "dateRange": f"{self.begin_date},{self.end_date}",
            "type": TYPE,
            "lan": LANGUAGE
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(FILE_URL, params=payload, headers=headers)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise Exception("Failed to retrieve file")

