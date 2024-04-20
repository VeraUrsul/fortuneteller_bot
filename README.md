## Описание проекта

Телеграм-бот "Узнай свою судьбу" расскажет о Вашем предназначении и особенностях!
Воспользуетесь следущими кнопками:
- :confetti_ball: /birthday: расскажет в какой день недели Вы родились и какая планета Вам покровительствует;
- :crystal_ball: /oracle: моментальный расклад "Оракул Летиции" расскажет что было, что будет и чем сердце успокоется;
- :earth_asia: /number: подсчитает число Вашего имени и даст советы в какую сторону развиваться и ким видом деятельности заняться, также подскажет как проработать Ваш картический урок;
- :leo: /horos: гороскоп

## Как запустить проект:

### 1. Клонирование кода приложения с GitHub
```

git clone git@github.com:VeraUrsul/fortuneteller_bot.git

```
### 2. Cоздать и активировать виртуальное окружение:
```
# Переходим в директорию fortuneteller_bot
cd fortuneteller_bot/
# Создаём виртуальное окружение
python -m venv venv
# Активируем виртуальное окружение.
# для Linux
source venv/bin/activate
# для Windows
source venv/Scripts/activate

```

### 3. Установить зависимости из файла requirements.txt:
```

# Обновить пакет pip
python -m pip install --upgrade pip
# Устанавливаем зависимости
pip install -r requirements.txt

```

## 4. Создание и заполнение файла .env

```

touch .env
nano .env
TELEGRAM_TOKEN = '<GDUIYDYRYT641659565gcygvkchfxhvihcg>'
CHAT_ID = '<5543675147>'

```

## 5. Запускаем приложение

```

 python main.py 

 ```


## 6. Переходим по ссылке на телеграм бот [Узнай свою судьбу](https://web.telegram.org/a/#6344722417)

## Автор [Урсул Вера](https://github.com/VeraUrsul)
