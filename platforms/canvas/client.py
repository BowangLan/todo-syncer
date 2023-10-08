from datetime import datetime
import requests
from config import ua


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


class CanvasClient():

    DOMAIN = "https://canvas.uw.edu"

    def __init__(self, cookies: str = ""):
        self.cookies = cookies or ""
        pass

    @property
    def headers_with_auth(self):
        return {
            **common_headers,
            'cookie': self.cookies,
        }

    def get_plannables(
        self,
        startDate: datetime, 
        course_id: str = None
    ):
        startDate = startDate.strftime('%Y-%m-%d')

        url = f'{self.DOMAIN}/api/v1/planner/items?start_date={startDate}T07:00:00.000Z&order=asc&per_page=20'
        if course_id:
            url += f'&context_codes[]=course_{course_id}'
        return requests.get(url, headers=self.headers_with_auth)


    def get_courses(self):
        url = f"{self.DOMAIN}/api/v1/users/self/favorites/courses?include[]=term&exclude[]=enrollments&sort=nickname"
        return requests.get(url, headers=self.headers_with_auth)
