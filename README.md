## Автор [Урсул Вера](https://github.com/VeraUrsul)

## Телеграм бот [Узнай свою судьбу](https://web.telegram.org/a/#6344722417)

## Как запустить проект:

# Cоздать и активировать виртуальное окружение:
python -m venv venv
source venv/Scripts/activate 
# venv/Scripts/activate.bat проверить

# Обновить пакет pip
python -m pip install --upgrade pip

# Создаем файл зависимостей
pip freeze > requirements.txt

# Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

# Установить Beautiful Soup
pip install beautifulsoup4
# Установить python-dotenv 
pip install python-dotenv
pip install requests
# модуль для парсинга
pip install lxml


# Настройка интерпретатора, чтобы библиотека заработала
.\yatube_parsing\venv\Scripts\python.exe

# команда выводит список установленных библиотек через двойное равно, пример: beautifulsoup4==4.12.2 
pip freeze

# команда выводит в терминал и те библиотеки, которые программист устанавливал самостоятельно, и зависимые от них пакеты, пример: beautifulsoup4     4.12.2
pip list

# ОТПРАВИТЬ ПРОЕКТ НА Github
git add .
git commit -m 'Вывод в файл'
git config --global user.name Vera
git push

# Устанавливаем библиотеку
(venv) ... pip install python-telegram-bot==13.7 

# [Интересная статья](https://github.com/DjangoIPython/TelegramBot/blob/master/bot.py)
