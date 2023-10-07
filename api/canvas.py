import requests
from datetime import datetime
from config import ua

HOST = "https://canvas.uw.edu"

common_headers = {
        'accept': 'application/json+canvas-string-ids, application/json+canvas-string-ids, application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://canvas.uw.edu/',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': ua,
        'x-requested-with': 'XMLHttpRequest',
}

def get_plannables(
        cookies: str, 
        startDate: datetime, 
        course_id: str = None
):
    startDate = startDate.strftime('%Y-%m-%d')
    headers = {
        **common_headers,
        'cookie': cookies,
        # 'x-csrf-token': token,
    }

    url = f'{HOST}/api/v1/planner/items?start_date={startDate}T07:00:00.000Z&order=asc&per_page=20'
    if course_id:
        url += f'&context_codes[]=course_{course_id}'
    return requests.get(url, headers=headers)


def get_courses(cookies: str):
    url = f"{HOST}/api/v1/users/self/favorites/courses?include[]=term&exclude[]=enrollments&sort=nickname"
    return requests.get(url, headers={
        **common_headers,
        'cookie': cookies,
    })
