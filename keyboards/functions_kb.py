from telebot import types
from lexicon.lexicon_ru import *


def _none():
    return types.ReplyKeyboardRemove()


def _create_keyboard(btn_lines, back=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for line in btn_lines:
        btn_arr = []
        for name in line:
            btn_arr.append(types.KeyboardButton(text=name))
        keyboard.add(*btn_arr)
    if back:
        keyboard.add(types.KeyboardButton(text='<< Назад'))
    return keyboard


def _create_inline_keyboard(btn_lines):
    keyboard = types.InlineKeyboardMarkup(row_width=7)
    for line in btn_lines:
        btn_arr = []
        for name, data in line:
            btn_arr.append(types.InlineKeyboardButton(text=name, callback_data=data))
        keyboard.add(*btn_arr)
    return keyboard


def _back():
    return _create_keyboard([
        ['<< Назад']
    ])


menu = _create_keyboard([LEXICON_RU['menu'], ['Начать парсинг по фильтрам'], ['Показать введенные фильтры', 'Очистить '
                                                                                                            'фильтры']])

status_kb = _create_keyboard([["Черновик",
                               "Действует",
                               "Прекращен",
                               "Приостановлен",
                               "Возобновлен",
                               "Архивный",
                               "Направлено уведомление о прекращении",
                               "Выдано предписание",
                               "Ожидает проверки оператора реестра",
                               "Недействителен"]], True)
typedec_kb = _create_keyboard([["Декларация о соответствии требованиям технического регламента Евразийского "
                                "экономического союза (технического регламента Таможенного союза)",
                                "Декларация о соответствии, оформленная по единой форме Евразийского экономического "
                                "союза",
                                "Декларация о соответствии требованиям технических регламентов Российской Федерации",
                                "Декларация о соответствии продукции, включенной в Единый перечень продукции "
                                "Российской Федерации",
                                "Декларация о соответствии продукции, включенной в перечень продукции Российской "
                                "Федерации"]], True)
type_objdec_kb = _create_keyboard([["Единичное изделие", "Партия", "Серийный выпуск"]], True)
date1_kb = _back()
date2_kb = _back()
back_kb = _back()
origin_kb = _back()
rfprod_kb = _back()
esprod_kb = _back()
eslist_kb = _back()
rflist_kb = _back()
tech_kb = _create_keyboard([['Решение Совета Евразийской экономической комиссии от 18.04.2018 № 44',
                             *[f"ТР ТС {f'00{i}'[-3:]}/2011" for i in range(1, 25)],
                             *[f"ТР ТС 0{i}/2012" for i in range(25, 32)],
                             *[f"ТР ТС 0{i}/2013" for i in range(32, 35)],
                             "ТР ТС 035/2014",
                             *[f"ТР ЕАЭС 0{i}/2016" for i in range(36, 41)],
                             *[f"ТР ЕАЭС 0{i}/2017" for i in range(40, 46)],
                             *[f"ТР ЕАЭС 0{i}/2018" for i in range(46, 48)],
                             *[f"ТР ЕАЭС 0{i}/2018" for i in range(46, 48)],
                             'Федеральный закон от 22.07.2008 № 123-ФЗ '
                             'Технический регламент о требованиях пожарной безопасности',
                             'ТР РФ 007/2008',
                             'ТР РФ 015/2009',
                             'ТР РФ 016/2010',
                             'ТР РФ 022/2010',
                             'ТР РФ 023/2010',
                             'ТР РФ 024/2010',
                             'ТР ЕАЭС 051/2021',
                             'ТР ЕАЭС 049/2020',
                             'ТР ЕАЭС 048/2019',
                             'Федеральный закон от 07.07.2003 № 126-ФЗ О связи',
                             'ТР ЕАЭС 052/2021',
                             'ТР ЕАЭС 050/2021'
                             ]], True)
type_kb = _create_keyboard([["Уполномоченное изготовителем лицо",
                             "Продавец",
                             "Изготовитель",
                             "Иcполнитель",
                             "Поставщик"]], True)

none = _none()
