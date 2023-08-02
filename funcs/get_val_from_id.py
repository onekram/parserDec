import requests


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJiY2Y1NjI5MS01M2M3LTRhOWYtODFhNS0wMDE2YTFlOGZjNzIiLCJzdWIiOiJhbm9ueW1vdXMiLCJleHAiOjE2OTEwMjczOTh9.aWqhQOYl7rKS1f9K4sqd3WkwTUPHRDYkj5xjQOIYwQid4O2IvzaFR59q2BfJiY4tVw1khCc_FxTsurnel5-ETQ',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '_ym_uid=1690375467469433987; _ym_d=1690375467; BITRIX_SM_GUEST_ID=22685468; BITRIX_SM_LAST_ADV=5_Y; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1690664340%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BITRIX_SM_LAST_VISIT=29.07.2023%2000%3A01%3A41; _ym_isad=2; JSESSIONID=D141E1D72FD535C790CF3E7D90E0CC6A',
    'Origin': 'https://pub.fsa.gov.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://pub.fsa.gov.ru/rds/declaration/view/17951008/product',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'lkId': '',
    'orgId': '',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'items': {
        'validationScheme2': [
            {
                'id': [
                    228,
                ],
                'fields': [
                    'name'
                ]
            },
        ],
        'tnved': [
            {
                'id': [
                    64961,
                ],
                'fields': [
                    'name',
                    'code',
                ],
            }
        ]
    }
}
session = requests.Session()
response = session.post('https://pub.fsa.gov.ru/nsi/api/multi', headers=headers, json=json_data, verify=False).json()
print(response)

