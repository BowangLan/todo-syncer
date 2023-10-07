import requests
from config import ua

def create_tasks(tasks, cookies: str):
    # Define the API endpoint URL
    url = "https://api.ticktick.com/api/v2/batch/task"

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
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookies,
        "User-Agent": ua,
    }

    res = requests.post(url, json=payload, headers=headers)
    return res