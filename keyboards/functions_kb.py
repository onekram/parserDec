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
        keyboard.add([types.KeyboardButton(text='<< Назад')])
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


menu = _create_keyboard([LEXICON_RU['menu'], ['Начать парсинг по фильтрам'], ['Показать введенные фильтры']])
status_kb = _create_keyboard(["Черновик", "Действует", "Прекращен", "Приостановлен", "Возобновлен", "Архивный", "Направлено уведомление о прекращении", "Выдано предписание", "Ожидает проверки оператора реестра", "Недействителен"], back=True)
typedec_kb = _create_keyboard(["Декларация о соответствии требованиям технического регламента Евразийского "
                               "экономического союза (технического регламента Таможенного союза)",
                               "Декларация о соответствии, оформленная по единой форме Евразийского экономического "
                               "союза",
                               "Декларация о соответствии требованиям технических регламентов Российской Федерации",
                               "Декларация о соответствии продукции, включенной в Единый перечень продукции "
                               "Российской Федерации",
                               "Декларация о соответствии продукции, включенной в перечень продукции Российской "
                               "Федерации"], back=True)
typeobjdec_kb = _create_keyboard(["Единичное изделие", "Партия", "Серийный выпуск"], back=True)

back_kb = _back()
none = _none()
