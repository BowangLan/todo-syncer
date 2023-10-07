from datetime import datetime
from api.canvas import get_plannables, get_courses

cookies = "_ga_SE47FJL7S6=GS1.2.1689616559.1.0.1689616559.0.0.0; _ga_WVZSJ3RGKJ=GS1.2.1689616560.1.0.1689616560.0.0.0; _ga_B3VH61T4DT=GS1.1.1695405272.6.1.1695405283.0.0.0; _gcl_au=1.1.1902743278.1696111870; _ga=GA1.1.1895634793.1687887922; _hjSessionUser_1219699=eyJpZCI6ImFmNzBmMDNmLTZhNTUtNTBiYS05NmFmLWNkNjIxMmFiNzdlMSIsImNyZWF0ZWQiOjE2OTYxMTE4NzE0MDgsImV4aXN0aW5nIjpmYWxzZX0=; _ga_EP4L2JRFBY=GS1.1.1696132140.2.0.1696132140.60.0.0; _ga_JP2435EY96=GS1.1.1696144793.2.0.1696144793.0.0.0; _ga_BFQJ094C4L=GS1.1.1696479875.5.0.1696479880.0.0.0; _ga_TNNYEHDN9L=GS1.1.1696490344.11.1.1696490557.0.0.0; log_session_id=f2264d8dfd89dcb6e87c20fc8f03802c; _legacy_normandy_session=5rNEbXVOSC6J8qXtAJ1SXw+iu7D3I7sv2v_n2258_VENVzlDXwd5xFZpNB7DVXDan-RX8D6dzk_9T1yp6ZS1UWuDX6vhUDbOUSiNfBHXxqPyT69saVDpkql70prlOA9Egr1U55B-rG70MCCQ7Llf5HnlksYBGJyVV6H25ZasLwNWho1QLRZ5yTr4vX2lp8jrPFAJaUy02VIHzyNu7fChpqQbIL3d45-jTbsmtT4t9Hu09v3JOglyH9l6ghvVvOYNEg0XEVRvRR3QQZ1BCpBVLHwc05uvfBqppLmZzEBBDFWMSDVMJQacZRY_O0MTqpS2cr9HFNYimJkOC4hB6z57ca7IuE5QfRmnopOPVE-sKVszmiaQFcPNJMygwRCjti1JLbDjUtyDU6UHdfA5f7ZRhZZwg3mLvTIWCNYRLAMp-r_kBTWD0tYJVSO1BWeRxzg7JQ5sniq8onknU_3PRvB82j5HFG0jx4lBRLqlmGQ1YBL84qamWSTXA2wdZnCQRneMkp_5YWeoFNcX9ZR9X3cwKbjSh6swlTxhob7dC_K0ddyYr6c3KhY_QALLOi_m71oqFv0M084I16kq7LLiPifV2agpJIcRthAGEgb3fhhdbweN_6l7ZaBNTAuHFN59SIaeUruADnMJ_kKq4hj6gLVFyP8i50Eo-bKZL7BE_C4mb6RfQ.qrwIHB7KMjBCXoHUsCxGEWq12Lk.ZSA_Ug; canvas_session=5rNEbXVOSC6J8qXtAJ1SXw+iu7D3I7sv2v_n2258_VENVzlDXwd5xFZpNB7DVXDan-RX8D6dzk_9T1yp6ZS1UWuDX6vhUDbOUSiNfBHXxqPyT69saVDpkql70prlOA9Egr1U55B-rG70MCCQ7Llf5HnlksYBGJyVV6H25ZasLwNWho1QLRZ5yTr4vX2lp8jrPFAJaUy02VIHzyNu7fChpqQbIL3d45-jTbsmtT4t9Hu09v3JOglyH9l6ghvVvOYNEg0XEVRvRR3QQZ1BCpBVLHwc05uvfBqppLmZzEBBDFWMSDVMJQacZRY_O0MTqpS2cr9HFNYimJkOC4hB6z57ca7IuE5QfRmnopOPVE-sKVszmiaQFcPNJMygwRCjti1JLbDjUtyDU6UHdfA5f7ZRhZZwg3mLvTIWCNYRLAMp-r_kBTWD0tYJVSO1BWeRxzg7JQ5sniq8onknU_3PRvB82j5HFG0jx4lBRLqlmGQ1YBL84qamWSTXA2wdZnCQRneMkp_5YWeoFNcX9ZR9X3cwKbjSh6swlTxhob7dC_K0ddyYr6c3KhY_QALLOi_m71oqFv0M084I16kq7LLiPifV2agpJIcRthAGEgb3fhhdbweN_6l7ZaBNTAuHFN59SIaeUruADnMJ_kKq4hj6gLVFyP8i50Eo-bKZL7BE_C4mb6RfQ.qrwIHB7KMjBCXoHUsCxGEWq12Lk.ZSA_Ug; _hp2_id.3001039959=%7B%22userId%22%3A%224596047079871461%22%2C%22pageviewId%22%3A%227592637574004229%22%2C%22sessionId%22%3A%221975306891350359%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.3001039959=%7B%22r%22%3A%22https%3A%2F%2Fidp.u.washington.edu%2F%22%2C%22ts%22%3A1696612350419%2C%22d%22%3A%22canvas.uw.edu%22%2C%22h%22%3A%22%2Fcourses%2F1663627%22%7D; _csrf_token=E1ozoA1M82rzIuEOhT27ORs%2B6WSwtL0bMlY0MwfgqvBRNl%2BPaSiYK8Zar23tUc1raE%2BNEPiC%2BG0DYFAKM6r5mA%3D%3D"
token = "E1ozoA1M82rzIuEOhT27ORs+6WSwtL0bMlY0MwfgqvBRNl+PaSiYK8Zar23tUc1raE+NEPiC+G0DYFAKM6r5mA=="

def test_get_plannable():
    startDate = datetime.now()
    p = get_plannables(cookies, startDate, '1662308')
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
    res = get_courses(cookies)
    data = res.json()
    data = res.json()
    assert res.status_code == 200
    assert type(data) == list