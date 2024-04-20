import datetime as dt
import logging
import os
import random
import sys

from dotenv import load_dotenv
from telegram import (
    Bot, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
)
from telegram.ext import (
    CallbackQueryHandler, CommandHandler, Filters, MessageHandler, Updater
)
from data import (
    DAY_OF_WEEK, DECK_OF_CARDS, TIMES, VALUE_OF_LETTER, NUMBER_OF_NAME
)
from zodiac import ZODIAC_SINGS


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# Укажите id своего аккаунта в Telegram
CHAT_ID = os.getenv('CHAT_ID')


def oracle_of_letitia(update, context, cards=12):
    """ Гадание *Оракул Летиции*. Из колоды (32 карты) в случайном порядке 
    извлекаются 12 карт и составляются в пары (1,12; 2,11; 3,10; 4,9; 5,8; 6,7)
    учитывая зависимость между основной и дополнительной картами, выходит 6 
    итоговых значений повременам (5 времён и чем сердце успокоится). """
    chat = update.effective_chat
    name = update.message.chat.first_name
    # в случайном порядке выбираем из колоды 12 карт
    collection = []
    for i in range(cards):
        card = random.choice(DECK_OF_CARDS)
        collection.append(card)
        DECK_OF_CARDS.remove(card)
    # собираем в пары (первая, последняя)
    pairs = list(zip(collection, collection[::-1]))
    # создается 12 пар, после 6-ой пары идет повторение, удаляем последние 6 пар
    unique_pairs = pairs[: len(pairs) - len(pairs) // 2]
    unique_pairs_in_time = list(zip(TIMES, unique_pairs))
    mean_main_and_add_cards = []
    for time, cards in unique_pairs_in_time:
        main_card_title, add_card_title = cards[0]['title'], cards[1]['title']
        main_card_meaning = cards[0]['meaning']
        add_card_meaning = cards[1]['meaning']
        divination_of_pair = (
            cards[0][cards[1]['name']] 
                if cards[1]['name'] in cards[0].keys() 
                    else cards[0][cards[1]['suit']]
        )
        mean_main_and_add_cards.append((
            time, main_card_title, add_card_title, main_card_meaning,
            add_card_meaning, divination_of_pair
    ))
    fortune_telling = '\n'.join([
        f'* {time}: \n'
        f' Основная карта: {main_card_title},'
        f' её значение: {main_card_meaning} \n'
        f' Дополнительная карта: {add_card_title},'
        f' её значение: {add_card_meaning}\n'
        f' Итоговое значение: {divination_of_pair}\n'
        for time, main_card_title, add_card_title, main_card_meaning,
            add_card_meaning, divination_of_pair in mean_main_and_add_cards
    ])
    update.message.reply_text(
        'Гадание "Оракул Лeтиции"\n\n'
        'Не забывайте, карты капризны. Если они решили не говорить\n'
        'Не настаивайте. Лучше попробуйте в другой раз.\n\n'
        f' {name}, взгляните, что Вам выпало: \n\n'
        f'{fortune_telling}\n\n'
        'Карты пророчат и предупреждают, но в нашей власти изменить всё \n'
        'в благоприятную сторону. Хотеть - значит мочь!\n'
    )


def divination_weekday(update, context):
    """ Предлагает ввести дату рождения. Связана с функцией value_birthday()."""
    update.message.reply_text('Введи дату рождения, например: 03.08.1991')

def value_birthday(update, context):
    """ Высчитывает в какой день недели родились. 
    Получает дату от функции divination_weekday()."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    date_example = update.message.text
    print(date_example)
    try:
        post_date = dt.datetime.strptime(date_example, '%d.%m.%Y')
    except:
        raise ValueError('Дата указана неверно! Попробуйте так: 03.08.1991')
    day_of_week = DAY_OF_WEEK[post_date.weekday()]
    # weekday() - Дни недели от 0 до 6, где понедельник - это 0, а воскресенье - 6.
    context.bot.send_message(
        chat_id=chat.id,
        text='{}, Вы родились в день недели {}'.format(name, day_of_week),
        # Добавим кнопку в содержимое отправляемого сообщения
        #reply_markup=button  
    )


# Отправка сообщения при старте бота (функция на доработке)
#def send_message(message):
#    bot.send_message(CHAT_ID, message)

#send_message(message)


#def say_hi(update, context): (функция на доработке)
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
#    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
#    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def name_number(update, context):
    """Подсчет значений букв в имени. Их суммирование до 1 цифры и значение."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    value_of_name = sum([VALUE_OF_LETTER[letter] for letter in name.lower()])
    while value_of_name > 9:
        value_of_name = value_of_name // 10 + value_of_name % 10
    context.bot.send_message(
        chat_id=chat.id,
        text='{}, число Вашего имени {}! {}'.format(
            name, value_of_name, NUMBER_OF_NAME[value_of_name]),
        # Добавим кнопку в содержимое отправляемого сообщения
        #reply_markup=button  
    )


def horos(update, context):
    """ Получение гороскопа с выбором кнопки. """
    keyboard = [
        [InlineKeyboardButton('Овен', callback_data='aries'),
         InlineKeyboardButton('Телец', callback_data='taurus')],
        [InlineKeyboardButton('Близнецы', callback_data='gemini'),
         InlineKeyboardButton('Рак', callback_data='canser')],
        [InlineKeyboardButton('Лев', callback_data='leo'),
         InlineKeyboardButton('Дева', callback_data='virgo')],
        [InlineKeyboardButton('Весы', callback_data='libra'),
         InlineKeyboardButton('Скорпион', callback_data='scorpio')],
        [InlineKeyboardButton('Стрелец', callback_data='sagittarius'),
         InlineKeyboardButton('Козерог', callback_data='capricorn')],
        [InlineKeyboardButton('Водолей', callback_data='aquarius'),
         InlineKeyboardButton('Рыбы', callback_data='pisces')],
        #[InlineKeyboardButton('Узнать знак', callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите интересующий знак зодиака:',
        reply_markup=reply_markup
    )

def button(update, _):
    """ Вспомогательная функция для функции horos(). """
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если 
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы. 
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # для версии 20.x необходимо использовать оператор await
    # await query.answer()

    # редактируем сообщение, тем самым кнопки 
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=ZODIAC_SINGS[variant][0].text)


def wake_up(update, context):
    """ Приветствующая функция с выбором кнопок. """
    chat = update.effective_chat
    name = update.message.chat.first_name
    # Вот она, наша кнопка.
    # Обратите внимание: в класс передаётся список, вложенный в список, 
    # даже если кнопка всего одна.
    # За счёт параметра resize_keyboard=True сделаем кнопки поменьше
    button = ReplyKeyboardMarkup(
        [['/birthday'], ['/oracle'], ['/number'], ['/horos']],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Добро пожаловать, {}!\n'
        'Здесь Вам откроются знания о Вашем предназначении!'.format(name),
        # Добавим кнопку в содержимое отправляемого сообщения
        reply_markup=button  
    )


def main():
    """ Логика работы бота. """
    bot = Bot(token=TELEGRAM_TOKEN)
    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('number', name_number))
    updater.dispatcher.add_handler(CommandHandler('horos', horos))
    updater.dispatcher.add_handler(CommandHandler('birthday', divination_weekday))
    updater.dispatcher.add_handler(CommandHandler('oracle', oracle_of_letitia))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.regex('\d+\.\d+\.\d+'), value_birthday)
    )
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    ##_______ Раздел на доработке
    # Регистрируется обработчик MessageHandler;
    # из всех полученных сообщений он будет выбирать только текстовые сообщения
    # и передавать их в функцию say_hi()

    #updater.dispatcher.add_handler(MessageHandler(Filters.text, divination_weekday))
    ##_______

    # Метод start_polling() запускает процесс polling, 
    # приложение начнёт отправлять регулярные запросы для получения обновлений.
    # Периодичность опроса можно изменить, передав методу именованный параметр 
    # poll_interval и указав нужный интервал запросов (в секундах, float):
    updater.start_polling() #poll_interval=20.0
    # Бот будет работать до тех пор, пока не нажмете Ctrl-C
    updater.idle()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(__file__ + '.log'),
            logging.StreamHandler(stream=sys.stdout)
        ],
        format=('%(asctime)s [%(levelname)s] '
                '[%(funcName)s:%(lineno)d] %(message)s')
    )
    main()
