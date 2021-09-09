"""
? Есть сайт (https://psycatgames.com/ru/magazine/conversation-starters/things-to-talk-about/), на котором отображены названия тем для разговоров и возможные вопросы
! На вход подается url ссылка на страницу
* Необходимо запарсить страницу по h3 тегу и собранные данные записать в файл .txt
"""
from bs4 import BeautifulSoup
import requests

def save(str):
    with open('parse_tags.txt', 'a') as file:
        file.write(f'Tag:{str}\n')

def parse():
    URL = 'https://psycatgames.com/ru/magazine/conversation-starters/things-to-talk-about/'
    HEADERS = {
        'User_Agenet': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.468 Yowser/2.5 Safari/537.36'
    }
    
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('h3')
    
    for item in items:
        str = item.get_text()
        save(str)

parse()
