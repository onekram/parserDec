import requests
import json
import time


class BSparser:

    def __init__(self, id_p: str | int):
        self.id_p = id_p

    def get_headers(self):
        return {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
            'Authorization': self.get_token(),
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            # 'Cookie': '_ym_uid=169048467811544140; _ym_d=1690484678; _ym_isad=2; JSESSIONID=6CF5F590463C74D99260BA5719DC1E9D',
            'Origin': 'https://pub.fsa.gov.ru',
            'Pragma': 'no-cache',
            'Referer': 'https://pub.fsa.gov.ru/rds/declaration',
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

    def get_token(self):
        url = 'https://pub.fsa.gov.ru/login'
        my_headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://pub.fsa.gov.ru',
        }
        data = {
            'username': 'anonymous',
            'password': 'hrgesf7HDR67Bd'
        }
        response = requests.post(url, headers=my_headers, json=data, verify=False)
        return response.headers['Authorization']

    def get_val(self, scheme_id, tnved_id):
        json_data = {
            'items': {
                'validationScheme2': [
                    {
                        'id': [
                            scheme_id,
                        ],
                        'fields': [
                            'name'
                        ]
                    },
                ],
                'tnved': [
                    {
                        'id': [
                            tnved_id,
                        ],
                        'fields': [
                            'name',
                            'code',
                        ],
                    }
                ]
            }
        }
        try:
            session = requests.Session()
            response = session.post('https://pub.fsa.gov.ru/nsi/api/multi', headers=self.get_headers(),
                                    json=json_data,
                                    verify=False).json()
        except:
            time.sleep(10)
            return self.get_val(scheme_id, tnved_id)
        else:
            return response['validationScheme2'][0]['name'], response['tnved'][0]['code'] + ' '  + response['tnved'][0]['name'].replace('\xa0', '')

    def get_dt(self):
        page = 'common'
        try:
            session = requests.Session()
            response = session.get(url=f'https://pub.fsa.gov.ru/api/v1/rds/{page}/declarations/{self.id_p}',
                                   verify=False,
                                   headers=self.get_headers()).json()


        except Exception as e:
            time.sleep(20)
            return self.get_dt()
        else:
            scheme = response['idDeclScheme']
            tnved = response['product']['identifications'][0]['idTnveds'][0]
            return response, self.get_val(scheme, tnved)


if __name__ == '__main__':
    fil = BSparser(17942106)
    print(fil.get_dt())
    with open(f'datacommon.json', 'w', encoding='utf-8') as out:
        json.dump(fil.get_dt(), out, ensure_ascii=False, indent=4)
