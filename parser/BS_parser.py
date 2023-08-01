import requests
import json


class BSparser:

    def __init__(self, id_p: str | int):
        self.id_p = id_p
        self.row = {'id': id_p,
                    'Тип декларации': '',  # common
                    'Технические регламенты': '',
                    'Группа продукции ЕАЭС': '',
                    'Схема декларирования': '',
                    'Тип объекта декларирования': '',
                    'Статус декларации': '',  # declaration
                    'Регистрационный номер декларации о соответствии': '',
                    'Дата регистрации декларации': '',
                    'Дата окончания действия декларации о соответствии': '',
                    'Заявитель': '',  # applicant
                    'ИНН(заявитель)': '',
                    'ОГРНИП(заявитель)': '',
                    'Адрес места осуществления деятельности': '',
                    'Адрес места нахождения(заявитель)': '',
                    'Номер телефона(заявитель)': '',
                    'Адрес электронной почты(заявитель)': '',
                    'Полное наименование': '',  # manufacturer
                    'ИНН(иготовитель)': '',
                    'Адрес места нахождения(иготовитель)': '',
                    'Адрес производства продукции': '',
                    'Номер телефона(иготовитель)': '',
                    'Адрес электронной почты(иготовитель)': '',
                    'Продукция, ввезена для проведения исследований и испытаний в качестве проб (образцов) для целей подтверждения соответствия?': '',
                    # custom info
                    'Регистрационный номер таможенной декларации': '',
                    'Общее наименование продукции': '',  # product
                    'Общие условия хранения продукции': '',
                    'Происхождение продукции': '',
                    'Размер партии': '',
                    'Код ТН ВЭД ЕАЭС': '',
                    'Наименование (обозначение) продукции': '',
                    'Наименование документа': '',
                    'Испытания продукции': ''
                    }

        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
            'Authorization': self.get_token(),
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': '_ym_uid=169048467811544140; _ym_d=1690484678; _ym_isad=2; JSESSIONID=C951472604EEA9680F4EC6B0FAF9651C',
            'Pragma': 'no-cache',
            'Referer': 'https://pub.fsa.gov.ru/rds/declaration/view/17941350/common',
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
    def get_dt(self, headers):
        page = 'common'
        try:
            session = requests.Session()
            response = session.get(url=f'https://pub.fsa.gov.ru/api/v1/rds/{page}/declarations/{self.id_p}',
                                   verify=False,
                                   headers=headers)


        except Exception as e:
            print(123, e)
        else:
            return response.json()




if __name__ == '__main__':
    fil = BSparser(17933740)
    with open(f'datacommon.json', 'w', encoding='utf-8') as out:
        json.dump(fil.get_dt(fil.headers), out, ensure_ascii=False, indent=4)

