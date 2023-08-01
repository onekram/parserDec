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


# ---------------------------------------------------------


# GET COUNTRIES -------------------------------------------

# Get All-Countries list
def get_nations(session):
    json_data = {
        'sort': 'id',
        'attrs': [],
        'offset': None,
        'limit': 350,
    }
    response = session.post('https://pub.fsa.gov.ru/nsi/api/oksm/get', headers=headers, json=json_data, verify=False)
    return json.loads(response.text)


# ---------------------------------------------------------


# ---- EAS SINGLE PRODUCTS --------------------------------

def get_eas_single_products_PARENTS():
    while True:
        try:
            session = requests.Session()
            json_data = {
                'parentId': None,
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
            response = session.post('https://pub.fsa.gov.ru/nsi/api/tree/singleListEEU/get', headers=headers,
                                    json=json_data, verify=False)
            return [{'name': item['name'], 'id': item['id']} for item in json.loads(response.text)['items']]
        except:
            print(f'[ERROR] get_eas_single_products_PARENTS')
            time.sleep(0.5)
            continue


def get_eas_single_products_CHILD(parent_id):
    while True:
        try:
            session = requests.Session()
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
            response = session.post('https://pub.fsa.gov.ru/nsi/api/tree/singleListEEU/get', headers=headers,
                                    json=json_data, verify=False)
            return [{'name': item['name'], 'id': item['id']} for item in json.loads(response.text)['items']]
        except:
            print(f'[ERROR] get_eas_single_products_CHILD - {parent_id}')
            time.sleep(0.5)
            continue


def get_eas_single_products():
    eas_res = list()
    PARENT_ITEMS = get_eas_single_products_PARENTS()

    for PARENT in PARENT_ITEMS:
        # Если категория в категории
        CHILD_ITEMS = get_eas_single_products_CHILD(PARENT['id'])

        # Если попалась не категория а объект
        if len(CHILD_ITEMS) == 0:
            if not PARENT in eas_res:
                eas_res.append(PARENT)
            continue

        # Категория в категории
        while True:
            NEXT_CHILDS = list()
            while_stop = False

            # Проходимся по 'детям' категории и чекаем является ли 'ребенок' - еще одной категорией
            for CHILD in CHILD_ITEMS:
                CUR_CHILDS = get_eas_single_products_CHILD(CHILD['id'])

                # Если 'ребенок' - не категория, то выходим из цикла
                if not CUR_CHILDS:
                    if not CHILD in eas_res:
                        eas_res.append(CHILD)
                    while_stop = True
                else:
                    # Если 'ребенок' - категория, то добавляем в результат
                    NEXT_CHILDS += CUR_CHILDS
                    for CUR_CHILD in CUR_CHILDS:
                        if CUR_CHILD not in eas_res:
                            eas_res.append(CUR_CHILD)

            CHILD_ITEMS = [item for item in NEXT_CHILDS]
            if while_stop:
                break

    return eas_res


# ---------------------------------------------------------


# ---- EAS SINGLE PRODUCTS --------------------------------

def get_eas_single_products_PARENTS():
    while True:
        try:
            session = requests.Session()
            json_data = {
                'parentId': None,
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
            response = session.post('https://pub.fsa.gov.ru/nsi/api/tree/singleListEEU/get', headers=headers,
                                    json=json_data, verify=False)
            return [{'name': item['name'], 'id': item['id']} for item in json.loads(response.text)['items']]
        except:
            print(f'[ERROR] get_eas_single_products_PARENTS')
            time.sleep(0.5)
            continue


def get_eas_single_products_CHILD(parent_id):
    while True:
        try:
            session = requests.Session()
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
            response = session.post('https://pub.fsa.gov.ru/nsi/api/tree/singleListEEU/get', headers=headers,
                                    json=json_data, verify=False)
            return [{'name': item['name'], 'id': item['id']} for item in json.loads(response.text)['items']]
        except:
            print(f'[ERROR] get_eas_single_products_CHILD - {parent_id}')
            time.sleep(0.5)
            continue


def get_eas_single_products():
    eas_res = list()
    PARENT_ITEMS = get_eas_single_products_PARENTS()

    for PARENT in PARENT_ITEMS:
        # Если категория в категории
        CHILD_ITEMS = get_eas_single_products_CHILD(PARENT['id'])

        # Если попалась не категория а объект
        if len(CHILD_ITEMS) == 0:
            if not PARENT in eas_res:
                eas_res.append(PARENT)
            continue

        # Категория в категории
        while True:
            NEXT_CHILDS = list()
            while_stop = False

            # Проходимся по 'детям' категории и чекаем является ли 'ребенок' - еще одной категорией
            for CHILD in CHILD_ITEMS:
                CUR_CHILDS = get_eas_single_products_CHILD(CHILD['id'])

                # Если 'ребенок' - не категория, то выходим из цикла
                if not CUR_CHILDS:
                    if not CHILD in eas_res:
                        eas_res.append(CHILD)
                    while_stop = True
                else:
                    # Если 'ребенок' - категория, то добавляем в результат
                    NEXT_CHILDS += CUR_CHILDS
                    for CUR_CHILD in CUR_CHILDS:
                        if CUR_CHILD not in eas_res:
                            eas_res.append(CUR_CHILD)

            CHILD_ITEMS = [item for item in NEXT_CHILDS]
            if while_stop:
                break

    return eas_res


# ---------------------------------------------------------


# ---- RF SINGLE PRODUCTS ---------------------------------

def get_rf_single_products_PARENTS():
    while True:
        try:
            session = requests.Session()
            json_data = {
                'parentId': None,
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
            response = session.post('https://pub.fsa.gov.ru/nsi/api/tree/singleListRU/get', headers=headers,
                                    json=json_data, verify=False)
            return [{'name': item['name'], 'id': item['id']} for item in json.loads(response.text)['items']]
        except:
            print('[ERROR] get_rf_single_products_PARENTS')
            time.sleep(0.5)
            continue


def get_rf_single_products_CHILD(parent_id):
    while True:
        try:
            session = requests.Session()
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
            response = session.post('https://pub.fsa.gov.ru/nsi/api/tree/singleListRU/get', headers=headers,
                                    json=json_data, verify=False)
            return [{'name': item['name'], 'id': item['id']} for item in json.loads(response.text)['items']]
        except:
            # return [{'name': None, 'id': None}]
            print(f'[ERROR] get_rf_single_products_CHILD - {parent_id}')
            time.sleep(0.5)
            continue


def rf_get_parent(PARENT, rf_res):
    # Если категория в категории
    CHILD_ITEMS = get_rf_single_products_CHILD(PARENT['id'])

    # Если попалась не категория а объект
    if len(CHILD_ITEMS) == 0:
        if not PARENT in rf_res:
            rf_res.append(PARENT)
        return

    # Категория в категории
    while True:
        NEXT_CHILDS = list()
        while_stop = False

        # Проходимся по 'детям' категории и чекаем является ли 'ребенок' - еще одной категорией
        for CHILD in CHILD_ITEMS:
            CUR_CHILDS = get_rf_single_products_CHILD(CHILD['id'])

            # Если 'ребенок' - не категория, то выходим из цикла
            if not CUR_CHILDS:
                if not CHILD in rf_res:
                    rf_res.append(CHILD)
                while_stop = True
            else:
                # Если 'ребенок' - категория, то добавляем в результат
                NEXT_CHILDS += CUR_CHILDS
                for CUR_CHILD in CUR_CHILDS:
                    if CUR_CHILD not in rf_res:
                        rf_res.append(CUR_CHILD)

        CHILD_ITEMS = [item for item in NEXT_CHILDS]
        if while_stop:
            break


def get_rf_single_products():
    rf_res = list()
    PARENT_ITEMS = get_rf_single_products_PARENTS()

    for PARENT in PARENT_ITEMS:
        rf_get_parent(PARENT, rf_res)

    return rf_res


# ---------------------------------------------------------


# ---- TECH REGL ------------------------------------------

# Get Tech Regl
def get_tech_regl(session):
    json_data = {
        'sort': 'sortIndex',
        'attrs': [
            {
                'name': 'docTypeId',
                'operation': 'in',
                'value': [
                    1,
                    2,
                ],
            },
            {
                'name': 'docStatusId',
                'operation': 'in',
                'value': [
                    1,
                    2,
                    9,
                ],
            },
        ],
        'offset': 0,
        'limit': 50,
    }

    response = session.post('https://pub.fsa.gov.ru/nsi/api/dicNormDoc/get', headers=headers, json=json_data,
                            verify=False)
    return [{'name': item['displayName'], 'id': item['id']} for item in json.loads(response.text)['items']]


# ---------------------------------------------------------

# Get All-Filters list
def get_filters(session):
    result = dict()

    url = 'https://pub.fsa.gov.ru/api/v1/rds/common/identifiers'
    response = session.get(url, headers=headers, verify=False)
    filters = json.loads(response.text)

    # Status
    result['status'] = [{'name': filters['status'][key]['name'], 'id': filters['status'][key]['id']} for key in
                        filters['status']]

    # Decl_type
    result['decl_type'] = [{'name': filters['declType'][key]['name'], 'id': filters['declType'][key]['id']} for key in
                           filters['declType']]

    # Delc_obj_type
    result['decl_obj_type'] = [
        {'name': filters['declObjectTypes'][key]['name'], 'id': filters['declObjectTypes'][key]['id']} for key in
        filters['declObjectTypes']]

    # Origin_product
    origins = get_nations(session)
    result['origin_product'] = [{'name': item['shortName'], 'id': item['id']} for item in origins['items']]

    # RF_product_groups
    result['status'] = [{'name': filters['status'][key]['name'], 'id': filters['status'][key]['id']} for key in
                        filters['status']]

    # EAS_product_groups
    pass

    # EAS_single_product
    result['eas_single_products'] = get_eas_single_products()

    # RF_single_product
    # result['rf_single_products'] = get_rf_single_products()

    # Tech_regl
    result['tech_regl'] = get_tech_regl(session)

    # Application_type
    result['application_type'] = [
        {'id': filters['applicantTypes'][key]['id'], 'name': filters['applicantTypes'][key]['name']} for key in
        filters['applicantTypes']]

    return result


# ---- READ FROM FILTERS ----
# with open('filters.txt', 'r', encoding='utf-8') as file:
#     res = json.loads(file.read())

session = requests.Session()
url = 'https://pub.fsa.gov.ru/rds/declaration'

all_filters = get_filters(session)

# ---- WRITE TO FILTERS ----
# with open('filters.txt', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(all_filters))