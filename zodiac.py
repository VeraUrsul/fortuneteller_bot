from bs4 import BeautifulSoup
import requests


response = requests.get('https://horo.mail.ru/horoscope/zodiac/')
soup = BeautifulSoup(response.text, features='lxml')
ZODIAC_SINGS = dict(
    aries = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3)'),
    taurus = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(3)'),
    gemini = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(4) > div > div:nth-child(2) > div:nth-child(3)'),
    canser = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(5) > div > div:nth-child(2) > div:nth-child(3)'),
    leo = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(3)'),
    virgo = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(7) > div > div:nth-child(2) > div:nth-child(3)'),
    libra = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(8) > div > div:nth-child(2) > div:nth-child(3)'),
    scorpio = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(9) > div > div:nth-child(2) > div:nth-child(3)'),
    sagittarius = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(10) > div > div:nth-child(2) > div:nth-child(3)'),
    capricorn = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(11) > div > div:nth-child(2) > div:nth-child(3)'),
    aquarius = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(12) > div > div:nth-child(2) > div:nth-child(3)'),
    pisces = soup.select('body > div.layout > div:nth-child(3) > div:nth-child(5) > div > div > div > div > div > div:nth-child(13) > div > div:nth-child(2) > div:nth-child(3)'),
)
d = ZODIAC_SINGS['capricorn'][0].text
#print(type(d))
#print(d)
#print(capricorn[0].text)
#price = result['value']