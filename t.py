from api.ticktick import create_tasks
from faker import Faker
from datetime import datetime
import string
import random
from rich import print

faker = Faker()

cookies = "_ga=GA1.1.748585615.1696601587; t=154BB8FE914467834118B88A6F100E0E0C164C8536E1EAAD302699F47E881311CAB7C3908271B877884C263CF90C3851AD4825610B61613B25C6510A15F7E35A26FCA3A1EC32393C09FE58AE218AF4689A6E6F80995D5639C38FA02741DFDB9882BEE463B1431075BC4DD36207DCA5A89A6E6F80995D56390A69DEADEFC09B52828697D73C2D6DAAF156F7EEC1B0D9023B169CB6794620517C1F86D7076913F60D1E88CA749147E9; _ga_TM2QKQ5S5Q=GS1.1.1696606231.3.1.1696606372.44.0.0; AWSALB=VHEycvWA1YNY6Sj5XaTnsB/iw5D+uxqWWe02vUGG+iPOFcgTKHTbxvzUbP1wPQGUL/E9Co8rIsYQFLDRLdHV8Qxm8y3jCwwVEWnPDciB3y6jRgMhp1Itupd9SVUg; AWSALBCORS=VHEycvWA1YNY6Sj5XaTnsB/iw5D+uxqWWe02vUGG+iPOFcgTKHTbxvzUbP1wPQGUL/E9Co8rIsYQFLDRLdHV8Qxm8y3jCwwVEWnPDciB3y6jRgMhp1Itupd9SVUg"

def getCurrentDatetime():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y-%m-%dT%H:%M:%S") + ".000+0000"

def generateID():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(24))

if __name__ == "__main__":

    curDatetime = getCurrentDatetime()

    tasks = [
        {
            "items": [],
            "reminders": [],
            "exDate": [],
            "dueDate": None,
            "priority": 0,
            "progress": 0,
            "assignee": None,
            "sortOrder": -10445360463872,
            "startDate": None,
            "isFloating": False,
            "columnId": "65201578df81511a39c637be",
            "status": 0,
            "projectId": "inbox121614081",
            "kind": None,
            "createdTime": curDatetime,
            "modifiedTime": curDatetime,
            "title": faker.sentence(),
            "tags": [],
            "timeZone": "America/Los_Angeles",
            "content": "",
            "id": generateID(),
        },
        {
            "items": [],
            "reminders": [],
            "exDate": [],
            "dueDate": None,
            "priority": 0,
            "progress": 0,
            "assignee": None,
            "sortOrder": -10445360463872,
            "startDate": None,
            "isFloating": False,
            "columnId": "65201578df81511a39c637be",
            "status": 0,
            "projectId": "inbox121614081",
            "kind": None,
            "createdTime": curDatetime,
            "modifiedTime": curDatetime,
            "title": faker.sentence(),
            "tags": [],
            "timeZone": "America/Los_Angeles",
            "content": "",
            "id": generateID(),
        }
    ]
    
    print(tasks)
    res = create_tasks(tasks, cookies)
    print(res)
    print(res.text)

