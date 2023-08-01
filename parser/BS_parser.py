import requests
import json
import time


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
    def get_dt(self):
        page = 'common'
        try:
            time.sleep(0.1)
            session = requests.Session()
            response = session.get(url=f'https://pub.fsa.gov.ru/api/v1/rds/{page}/declarations/{self.id_p}',
                                   verify=False,
                                   headers=self.get_headers()).json()


        except Exception as e:
            time.sleep(10)
            return False
        else:
            return response




if __name__ == '__main__':
    fil = BSparser(17945659)
    with open(f'datacommon.json', 'w', encoding='utf-8') as out:
        json.dump(fil.get_dt(), out, ensure_ascii=False, indent=4)

