import json
import csv
import requests
from copy import copy
from telebot import TeleBot

from lexicon.alphabet import var, status

import time
import urllib3
from parser.BS_parser import BSparser

urllib3.disable_warnings()


class FilterParser:

    def __init__(self, bot: TeleBot, fiter: dict = None, amount: int = 10):
        self.bot = bot
        self.data = []
        self.json_data = {
            'size': min(1000, amount),
            'page': 0,
            'filter': {
                'status': fiter['status'],
                'idDeclType': fiter['type_dec'],
                'idCertObjectType': fiter['type_obj_dec'],
                'idProductType': [],
                'idGroupRU': fiter['rf_prod'],
                'idGroupEEU': fiter['es_prod'],
                'idTechReg': fiter['tech'],
                'idApplicantType': fiter['type'],
                'regDate': {
                    'minDate': fiter['date1'][0],
                    'maxDate': fiter['date1'][1],
                },
                'endDate': {
                    'minDate': fiter['date2'][0],
                    'maxDate': fiter['date2'][1],
                },
                'columnsSearch': [
                    {
                        'name': 'number',
                        'search': '',
                        'type': 9,
                    },
                ],
                'idProductOrigin': fiter['origin'],
                'idProductEEU': fiter['es_list'],
                'idProductRU': fiter['rf_list'],
                'idDeclScheme': [],
                'awaitForApprove': None,
                'awaitOperatorCheck': None,
                'editApp': None,
                'violationSendDate': None,
                'isProtocolInvalid': None,
                'checkerAIResult': None,
                'checkerAIProtocolsResults': None,
                'checkerAIProtocolsMistakes': None,
            },
            'columnsSort': [
                {
                    'column': 'declDate',
                    'sort': 'DESC',
                },
            ],
        }
        self.row = {'ID': '',
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
                    'Полное наименование юридического лица': '',
                    'ИНН(заявитель)': '',
                    'ОГРН(-ИП)(заявитель)': '',
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
                    'Испытания продукции': '',
                    'Наименование испытательной лаборатории': ''
                    }
        self.fields = self.row.copy().keys()

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

    def download_data(self, chid, mid):
        session = requests.Session()
        response = session.post(
            'https://pub.fsa.gov.ru/api/v1/rds/common/declarations/get',
            headers=self.get_headers(),
            json=self.json_data,
            verify=False
        )
        for i, item in enumerate(response.json()['items'], 1):
            self.bot.edit_message_text(chat_id=chid, text=f'Процесс парсинга: {i} операций выполнено!', message_id=mid)
            self.row['ID'] = f"https://pub.fsa.gov.ru/rds/declaration/view/{item.get('id', '')}"
            self.row['Тип декларации'] = item.get('declType', '')
            self.row['Технические регламенты'] = item.get('technicalReglaments', '')
            self.row['Группа продукции ЕАЭС'] = item.get('group', '')
            self.row['Тип объекта декларирования'] = item.get('declObjectType', '')
            self.row['Статус декларации'] = status[item.get('idStatus', '')]
            self.row['Регистрационный номер декларации о соответствии'] = item.get('number', '')
            self.row['Дата регистрации декларации'] = item.get('declDate', '')
            self.row['Дата окончания действия декларации о соответствии'] = item.get('declEndDate', '')
            self.row['Размер партии'] = item.get('productBatchSize', '')
            self.row['Полное наименование'] = item.get('manufacterName', '')
            self.row['Испытания продукции'] = item.get('statusTestingLabs', '')
            self.row['Общее наименование продукции'] = item.get('productFullName', '')
            self.row['Происхождение продукции'] = item.get('productOrig', '')
            self.row['Наименование (обозначение) продукции'] = item.get('productIdentificationName', '')

            sess = BSparser(item.get('id', ''))
            item_info, addids = sess.get_dt()
            scheme, tnved = addids

            try:
                self.row['ИНН(заявитель)'] = item_info['applicant']['inn']
            except:
                pass
            try:
                self.row['ОГРН(-ИП)(заявитель)'] = item_info['applicant']['ogrn']
            except:
                pass
            try:
                self.row['Код ТН ВЭД ЕАЭС'] = tnved
            except:
                pass

            try:
                self.row['Заявитель'] = item_info['applicant']['shortName'] or item_info['applicant']['fullName']
            except:
                pass
            try:
                self.row['Полное наименование юридического лица'] = item_info['applicant']['fullName']
            except:
                pass

            try:
                self.row['Схема декларирования'] = scheme
            except:
                pass
            try:
                self.row['Адрес места нахождения(заявитель)'] = item_info['applicant']['addresses'][0][
                    'fullAddress']
                self.row['Адрес места осуществления деятельности'] = item_info['applicant']['addresses'][1][
                    'fullAddress']
            except:
                pass
            try:
                self.row['Номер телефона(заявитель)'] = item_info['applicant']['contacts'][1]['value']
            except:
                pass
            try:
                self.row['Адрес электронной почты(заявитель)'] = item_info['applicant']['contacts'][0]['value']
            except:
                pass
            self.row['ИНН(иготовитель)'] = item_info['manufacturer']['inn']
            try:
                self.row['Адрес места нахождения(иготовитель)'] = item_info['manufacturer']['addresses'][0][
                    'fullAddress']
            except:
                pass
            try:
                self.row['Адрес производства продукции'] = item_info['manufacturerFilials'][0]['addresses'][0][
                    'fullAddress']
            except:
                pass

            try:
                self.row['Адрес электронной почты(иготовитель)'] = [i['value'] for i in
                                                                    item_info['manufacturer']['contacts'] if
                                                                    i['value'].count('@') == 1][0]
                self.row['Номер телефона(иготовитель)'] = [i['value'] for i in item_info['manufacturer']['contacts'] if
                                                           i['value'].count('@') == 0][0]
            except:
                pass
            try:
                self.row[
                    'Продукция, ввезена для проведения исследований и испытаний в качестве проб (образцов) для целей подтверждения соответствия?'] = \
                    ('нет', 'да')[bool(item_info['testingLabs'][0]['importedForResearchTesting'])]
            except:
                pass
            try:
                self.row['Регистрационный номер таможенной декларации'] = \
                    item_info['testingLabs'][0]['docConfirmCustom'][0]['customInfo'][0]['customDeclNumber']
            except:
                pass
            try:
                self.row['Наименование документа'] = item_info['product']['identifications'][0]['documents'][0]['name']
            except:
                pass

            try:
                self.row['Общие условия хранения продукции'] = item_info['product']['storageCondition']
            except:
                pass
            try:
                self.row['Наименование испытательной лаборатории'] = item_info['testingLabs'][0]['fullName']
            except:
                pass
            for k, val in self.row.items():
                if isinstance(val, str):
                    string = val.replace('\n', '').replace('\r\n', '').replace(';', '').replace('\xa0', '')
                    self.row[k] = ('%r' % string)[1:-1]
            self.data.append(self.row.copy())
            self.row.clear()

        return self.data


