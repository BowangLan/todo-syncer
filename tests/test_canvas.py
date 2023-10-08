from datetime import datetime
from platforms.canvas import CanvasClient

cookies = "_ga_SE47FJL7S6=GS1.2.1689616559.1.0.1689616559.0.0.0; _ga_WVZSJ3RGKJ=GS1.2.1689616560.1.0.1689616560.0.0.0; _ga_B3VH61T4DT=GS1.1.1695405272.6.1.1695405283.0.0.0; _gcl_au=1.1.1902743278.1696111870; _ga=GA1.1.1895634793.1687887922; _hjSessionUser_1219699=eyJpZCI6ImFmNzBmMDNmLTZhNTUtNTBiYS05NmFmLWNkNjIxMmFiNzdlMSIsImNyZWF0ZWQiOjE2OTYxMTE4NzE0MDgsImV4aXN0aW5nIjpmYWxzZX0=; _ga_EP4L2JRFBY=GS1.1.1696132140.2.0.1696132140.60.0.0; _ga_JP2435EY96=GS1.1.1696144793.2.0.1696144793.0.0.0; _ga_BFQJ094C4L=GS1.1.1696479875.5.0.1696479880.0.0.0; log_session_id=f2264d8dfd89dcb6e87c20fc8f03802c; _ga_TNNYEHDN9L=GS1.1.1696663369.12.1.1696663373.0.0.0; _legacy_normandy_session=HXDNkvYgIAX7NYQJaX_MFg+TLLyeSuVOLA7rahMHQks3vmacO54x5L1geASbenqI-8K5hlSQBeyW8pG4KmdERxqlIzs8xFyD_3_D2mW96oWJEpIqaK9GS-I_eyrKV26lgTzMUnRmxuT8vE8_lRZjXLWI3xWIhsK8CZMlQ9w_ijzpUrB-bhI_g0bquYRe6vTLMVgR0AyPZBtDcrM4MwjyvrORRPvf8TfSqRODl59pYye2-J-09EMiZKs4PiUL6Q1S5--6Ihi9Vn96C7SpoOVj13vBXAQORlwunwl6NnC2FagZyyIjbhrV7uKU4fu92KRYL2nr3iazEENKab3Ff_PevVkZhcPUPAJP37WfCuG-L04kxQWJSzX7_IbjHtCoPPIlA3wr7Pin3WaCIn5ZibSiuNVV61481BTiQit45KIQBkVcG7IUig6QZrKvYWVFA8o0lRtifQcs61mWqGrpZnfUS8CijmLwre8Tn_3ct2QRwLpmTxrtFrJZ6OFfW_Eo9qrePCnxbObEZ6-zaxKXedVh_OJNSPGkOXZmrNmjzvy5ZpTwqBpbYOOyxkCphiOAgUL5U6vAhwpYvEeCKWaVHdsr_ZyZ4DjKYn_yrczmhjAswFr8B86nQJDLP6LrI43LdF8f2tmwMV47NHKwNSMm9MW9RnRrgb8hZzAea11Fh2glEP5Jg.bSPewwDQx6iusWOC6piq5-DOf20.ZSIyjA; canvas_session=HXDNkvYgIAX7NYQJaX_MFg+TLLyeSuVOLA7rahMHQks3vmacO54x5L1geASbenqI-8K5hlSQBeyW8pG4KmdERxqlIzs8xFyD_3_D2mW96oWJEpIqaK9GS-I_eyrKV26lgTzMUnRmxuT8vE8_lRZjXLWI3xWIhsK8CZMlQ9w_ijzpUrB-bhI_g0bquYRe6vTLMVgR0AyPZBtDcrM4MwjyvrORRPvf8TfSqRODl59pYye2-J-09EMiZKs4PiUL6Q1S5--6Ihi9Vn96C7SpoOVj13vBXAQORlwunwl6NnC2FagZyyIjbhrV7uKU4fu92KRYL2nr3iazEENKab3Ff_PevVkZhcPUPAJP37WfCuG-L04kxQWJSzX7_IbjHtCoPPIlA3wr7Pin3WaCIn5ZibSiuNVV61481BTiQit45KIQBkVcG7IUig6QZrKvYWVFA8o0lRtifQcs61mWqGrpZnfUS8CijmLwre8Tn_3ct2QRwLpmTxrtFrJZ6OFfW_Eo9qrePCnxbObEZ6-zaxKXedVh_OJNSPGkOXZmrNmjzvy5ZpTwqBpbYOOyxkCphiOAgUL5U6vAhwpYvEeCKWaVHdsr_ZyZ4DjKYn_yrczmhjAswFr8B86nQJDLP6LrI43LdF8f2tmwMV47NHKwNSMm9MW9RnRrgb8hZzAea11Fh2glEP5Jg.bSPewwDQx6iusWOC6piq5-DOf20.ZSIyjA; _hp2_id.3001039959=%7B%22userId%22%3A%224596047079871461%22%2C%22pageviewId%22%3A%222073958901764898%22%2C%22sessionId%22%3A%224595234006339418%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.3001039959=%7B%22r%22%3A%22https%3A%2F%2Fcanvas.uw.edu%2F%22%2C%22ts%22%3A1696739984119%2C%22d%22%3A%22canvas.uw.edu%22%2C%22h%22%3A%22%2Fcourses%2F1662306%22%7D; _csrf_token=%2BCZKRgW6z%2BpC%2BA8sKYDGEFdgN6izlcRn%2Br4gNzVPErK6SiZpYd6kq3eAQU9B7LBCJBFT3PujgRHLiEQOAQVB2g%3D%3D"

client = CanvasClient(cookies)

def test_get_plannable():
    startDate = datetime.now()
    p = client.get_plannables(startDate, '1662308')
    data = p.json()
    assert p.status_code == 200
    assert type(data) == list

    # p_types = set([x['plannable_type'] for x in data])
    # p_types_count = {x: 0 for x in p_types}
    # contexts = set([x['context_name'] for x in data])
    # context_map = {x: [] for x in contexts}
    # for x in data:
    #     p_types_count[x['plannable_type']] += 1
    #     context_map[x['context_name']].append(x['plannable']['title'])
    # print(data)
    # print(p_types_count)
    # print(context_map)
    # print(len(data))


def test_get_courses():
    res = client.get_courses()
    data = res.json()
    data = res.json()
    assert res.status_code == 200
    assert type(data) == list