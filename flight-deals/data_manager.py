import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, get_sheety_endpoint, put_sheety_endpoint):
        self.get_sheety_endpoint = get_sheety_endpoint
        self.username = os.environ.get("ENV_SHEETY_USER")
        self.pwd = os.environ.get("ENV_SHEETY_PWD")
        self.put_sheety_endpoint = put_sheety_endpoint

    def get_data(self):
        try:
            response = requests.get(
                url=self.get_sheety_endpoint, auth=(self.username, self.pwd)
            )
            response.raise_for_status()
            data = response.json()
            return data["prices"]
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")

    def update_data(self, row_id, updated_data):
        try:
            put_url = f"{self.put_sheety_endpoint}/{row_id}"
            response = requests.put(
                url=put_url, json=updated_data, auth=(self.username, self.pwd)
            )
            response.raise_for_status()
            print(f"Row {row_id} updated successfully.")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
