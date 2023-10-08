import requests
from config import ua


class TickTickClient():

    API_DOMAIN = "https://api.ticktick.com"

    def __init__(self, cookies: str = ""):
        self.cookies = cookies or ""

    @property
    def headers_with_auth(self):
        return {
            "Content-Type": "application/json",
            "Cookie": self.cookies,
            "User-Agent": ua,
        }

    def create_tasks(self, tasks):
        # Define the API endpoint URL
        url = f"{self.API_DOMAIN}/api/v2/batch/task"

        # Define the payload using the provided format
        payload = {
            "add": tasks,
            "update": [],
            "delete": [],
            "addAttachments": [],
            "updateAttachments": [],
            "deleteAttachments": []
        }

        # Make the POST request to the API

        return requests.post(url, json=payload, headers=self.headers_with_auth)
