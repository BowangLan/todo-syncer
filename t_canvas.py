from api.canvas import get_plannables, get_courses
from datetime import datetime
from rich import print


if __name__ == "__main__":

    startDate = datetime.now()
    p = get_plannables(token, cookies, startDate, '1662308')
    data = p.json()
    p_types = set([x['plannable_type'] for x in data])
    p_types_count = {x: 0 for x in p_types}
    contexts = set([x['context_name'] for x in data])
    context_map = {x: [] for x in contexts}
    for x in data:
        p_types_count[x['plannable_type']] += 1
        context_map[x['context_name']].append(x['plannable']['title'])
    print(data)
    print(p_types_count)
    print(context_map)
    print(len(data))

    # get courses
    # res = get_courses(token, cookies)
    # courses = res.json()
    # print(courses)