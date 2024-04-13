import csv
import json
from telebot.types import Message
from config_data.config import load_config, Config
from telebot import TeleBot

from keyboards.functions_kb import *

from parser.requests_parser import FilterParser

from collections import defaultdict

config: Config = load_config()
bot: TeleBot = TeleBot(config.tgbot.token, parse_mode='html')
users = defaultdict(lambda: {'date1': [None, None],
                             'date2': [None, None],
                             'status': [],
                             'type_dec': [],
                             'type_obj_dec': [],
                             'origin': [],
                             'rf_prod': [],
                             'es_prod': [],
                             'es_list': [],
                             'rf_list': [],
                             'tech': [],
                             'type': []})

with open('lexicon/buttons.json', 'r') as file:
    var = json.load(file)
# ----------------------------------

def enter_date1(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        try:
            dates = message.text.split(',')
            assert len(dates) == 2
        except:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            users[message.from_user.id]['date1'] = dates

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_date2(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        try:
            dates = message.text.split(',')
            assert len(dates) == 2
        except:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            users[message.from_user.id]['date2'] = dates

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_status(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['status']:
            users[message.from_user.id]['status'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_typedec(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['decl_type']:
            users[message.from_user.id]['type_dec'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)



def enter_type_objdec(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['decl_obj_type']:
            users[message.from_user.id]['type_obj_dec'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_origin(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['origin_product']:
            users[message.from_user.id]['origin'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_rfprod(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['rf_group']:
            users[message.from_user.id]['rf_prod'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_esprod(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['es_group']:
            users[message.from_user.id]['es_prod'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_eslist(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['eas_single_products']:
            users[message.from_user.id]['es_list'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)

def enter_rflist(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        # users[message.from_user.id]['rf_list'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_tech(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        if message.text in var['tech_regl']:
            users[message.from_user.id]['tech'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)

def enter_type(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        if message.text in var['application_type']:
            users[message.from_user.id]['type'].append(message.text)

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)



on_parsing = False


def enter_amount(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        num = message.text
        if not num.isdigit():
            bot.send_message(chat_id=message.chat.id, text='Вы ввели некорректные данные', reply_markup=menu)
        else:
            try:
                global on_parsing
                on_parsing = True
                num = int(num)
                msg = bot.send_message(chat_id=message.chat.id, text='Парсинг начался...')

                obj = users[message.from_user.id]
                filter = {
                             'date1': obj['date1'],
                             'date2': obj['date2'],
                             'status': [var['status'][i] for i in obj['status']],
                             'type_dec': [var['decl_type'][i] for i in obj['type_dec']],
                             'type_obj_dec': [var['decl_obj_type'][i] for i in obj['type_obj_dec']],
                             'origin': [var['origin_product'][i] for i in obj['origin']],
                             'rf_prod': [var['rf_group'][i] for i in obj['rf_prod']],
                             'es_prod': [var['es_group'][i] for i in obj['es_prod']],
                             'es_list': [var['eas_single_products'][i] for i in obj['es_list']],
                             'rf_list': [var['rf_single_prod'][i] for i in obj['rf_list']],
                             'tech': [var['tech_regl'][i] for i in obj['tech']],
                             'type': [var['application_type'][i] for i in obj['type']]}
                parser = FilterParser(bot=bot, fiter=filter, amount=num)

                data = parser.download_data(chid=message.chat.id, mid=msg.message_id)
                with open('data.csv', 'w', encoding='utf-8-sig', newline='') as file_out:
                    writer = csv.DictWriter(file_out, fieldnames=parser.fields, delimiter=';')
                    writer.writeheader()
                    writer.writerows(data)
            except Exception as ex:
                bot.send_message(chat_id=message.from_user.id, text=f'В ходе работы парсера произошла ошибка: {ex}',
                                 reply_markup=menu)
            else:
                with open('data.csv', 'r', encoding='utf-8-sig', newline='') as file:
                    bot.send_document(chat_id=message.chat.id, document=file, reply_markup=menu)


            finally:
                on_parsing = False


# ----------------------------------


list_func = (enter_date1,
             enter_date2,
             enter_status,
             enter_typedec,
             enter_type_objdec,
             enter_origin,
             enter_rfprod,
             enter_esprod,
             enter_eslist,
             enter_rflist,
             enter_tech,
             enter_type)

list_btn = (date1_kb,
            date2_kb,
            status_kb,
            typedec_kb,
            type_objdec_kb,
            origin_kb,
            rfprod_kb,
            esprod_kb,
            eslist_kb,
            rflist_kb,
            tech_kb,
            type_kb)


@bot.message_handler(commands=['start'])
def start_processing(message: Message):
    bot.send_message(chat_id=message.from_user.id, text=LEXICON_RU['/start'], reply_markup=menu)


@bot.message_handler(content_types=['text'])
def menu_processing(message: Message):
    if on_parsing:
        bot.send_message(chat_id=message.chat.id, text='Подождите идет парсинг.....', reply_markup=none)
    if message.text == '<< Назад':
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)

    if message.text == 'Начать парсинг по фильтрам':
        bot.send_message(chat_id=message.from_user.id, text='Введите количество:', reply_markup=none)
        bot.register_next_step_handler(message, enter_amount)
    elif message.text == 'Показать введенные фильтры':
        bot.send_message(chat_id=message.from_user.id,
                         text='\n'.join([f'<b>{k}</b>: {v}' for k, v in zip(LEXICON_RU['menu'],
                                                                            users[message.from_user.id].values())]),
                         reply_markup=back_kb)
    elif message.text == 'Очистить фильтры':
        users[message.from_user.id] = {'date1': [None, None],
                                       'date2': [None, None],
                                       'status': [],
                                       'type_dec': [],
                                       'type_obj_dec': [],
                                       'origin': [],
                                       'rf_prod': [],
                                       'es_prod': [],
                                       'es_list': [],
                                       'rf_list': [],
                                       'tech': [],
                                       'type': []}
        bot.send_message(chat_id=message.chat.id, text='Готово', reply_markup=menu)
    for i, msg in enumerate(LEXICON_RU['menu']):
        if message.text == msg:
            bot.send_message(chat_id=message.from_user.id, text=input_fils[i], reply_markup=list_btn[i])
            bot.register_next_step_handler(message, list_func[i])


bot.infinity_polling()
