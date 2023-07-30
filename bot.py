from telebot.types import Message
from config_data.config import load_config, Config
from telebot import TeleBot

from keyboards.functions_kb import *

from parser.parser_processing import User_Parsing

from collections import defaultdict

config: Config = load_config()
bot: TeleBot = TeleBot(config.tgbot.token, parse_mode='html')
users = defaultdict(lambda: {'date1': [None, None],
                             'date2': [None, None],
                             'status': None,
                             'type_dec': None,
                             'type_obj_dec': None,
                             'origin': None,
                             'rf_prod': None,
                             'es_prod': None,
                             'es_list': None,
                             'rf_list': None,
                             'tech': None,
                             'type': None})


# ----------------------------------

def enter_date1(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        try:
            dates = message.text.split('-')
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
            dates = message.text.split('-')
            assert len(dates) == 2
        except:
            bot.send_message(chat_id=message.from_user.id, text='Вы ввели некорректные данные\n'
                                                                'Возвращаюсь в главное меню...',
                             reply_markup=menu)
        else:
            print(dates)
            users[message.from_user.id]['date2'] = dates

            bot.send_message(chat_id=message.chat.id,
                             text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                             reply_markup=menu)


def enter_status(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:
        users[message.from_user.id]['status'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_typedec(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['type_dec'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_type_objdec(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['type_obj_dec'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_origin(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['origin'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_rfprod(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['rf_prod'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_esprod(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['es_prod'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_eslist(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['es_list'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_rflist(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['rf_list'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_tech(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['tech'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


def enter_type(message: Message):
    if message.text in ('<< Назад', '/start'):
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)
    else:

        users[message.from_user.id]['type'] = message.text

        bot.send_message(chat_id=message.chat.id,
                         text=f'Вы ввели: {message.text}\n\n...Возвращаюсь в главное меню...',
                         reply_markup=menu)


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
    if message.text == '<< Назад':
        bot.send_message(chat_id=message.chat.id, text='== Главное меню ==', reply_markup=menu)

    if message.text == 'Начать парсинг по фильтрам':
        bot.send_message(chat_id=message.from_user.id, text='Парсинг начался!', reply_markup=none)
        parser = User_Parsing(users[message.from_user.id])
        parser.start_parsing()
        bot.send_message(chat_id=message.from_user.id, text='Парсинг закончился!', reply_markup=none)

    elif message.text == 'Показать введенные фильтры':
        bot.send_message(chat_id=message.from_user.id,
                         text='\n'.join([f'<b>{k}</b>: {v}' for k, v in zip(LEXICON_RU['menu'],
                                                                            users[message.from_user.id].values())]),
                         reply_markup=back_kb)

    for i, msg in enumerate(LEXICON_RU['menu']):
        if message.text == msg:
            bot.send_message(chat_id=message.from_user.id, text=input_fils[i], reply_markup=list_btn[i])
            bot.register_next_step_handler(message, list_func[i])


bot.infinity_polling()
