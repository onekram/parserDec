import requests, json, time

import warnings

warnings.filterwarnings("ignore")


# ---- GLOBAL VARIABLES -----------------------------------


def get_token():
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


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': get_token(),
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Referer': 'https://pub.fsa.gov.ru/rds/declaration',
    # 'Cookie': 'JSESSIONID=0437EFFDA2A8C98A787339A81519EC79',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

def get_list(url):

    childs = dict()
    import time

    def rec(parent_id, parent_value):
        json_data = {
        'parentId': parent_id,
        'attrs': [
            {
                'name': 'id',
                'operation': 'not in',
                'value': [
                    59,
                ],
            },
        ],
        }
        session = requests.Session()
        try:
            response = session.post(url, headers=headers, json=json_data, verify=False).json()
        except:
            time.sleep(10)
            response = session.post(url, headers=headers, json=json_data, verify=False).json()
        if not [i['id'] for i in response['items']]:
            nonlocal childs
            childs[parent_value] = parent_id
            print(parent_value, parent_id)
        else:
            for item in response['items']:
                rec(item['id'], item['name'])
    rec(None, None)
    return childs




if __name__ == '__main__':
    url = 'https://pub.fsa.gov.ru/nsi/api/tree/singleListRU/get'
    print(get_list(url))

    # json_data = {
    #     'parentId': 2,
    #     'attrs': [
    #         {
    #             'name': 'id',
    #             'operation': 'not in',
    #             'value': [
    #                 59,
    #             ],
    #         },
    #     ],
    # }
    # url = 'https://pub.fsa.gov.ru/nsi/api/tree/techregProductListRU/get'
    # session = requests.Session()
    # response = session.post(url, headers=headers, json=json_data, verify=False).json()
    # print([i['id'] for i in response['items']])


