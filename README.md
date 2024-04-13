## Телеграм бот парсер
- Бот написан на Python
- Использована библиотека telebot
- Библиотека использует Telegram Bot API

### Функционал
- Весь интерфейс вынесен в _inline_ кнопки, поддерживаемые телеграмом
- Кнопки позволяют задать необходимую конфигурацию для парсинга
- На выходе - csv файл с данными

### Реaлизация
- Бот анализирует отправленные ему сообщения
- Составляет конфигурацию фильтров
- На основе этой конфигурации строиться цепочка запросов
- Получаем ответ в JSON формате
- Информация структурируется в csv файл и отправляется пользователю
