import requests
import bs4
from Headers import *


response = requests.get('https://habr.com/ru/all/', headers=HEADERS)  # Запрос
response.raise_for_status()  # Проверка статус код (200, 400, 500)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')  # Найти все статьи


for article in articles:
    title = article.find('h2')  # Заголовок
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')  # Получить заголовок "a"
    article_hubs = set([hub.find('span').text for hub in hubs])

    title_times = article.find('div') #Заголовок
    hubs_times = article.find_all('span', class_='tm-article-snippet__datetime-published')  # Получить заголовок "span"
    article_times = [time.find('time').text for time in hubs_times]  # Найти time

    if set(MY_HUBS) & article_hubs:  # Пересичение хабов по имени
        tag_href = title.find('a')
        href = tag_href.attrs['href']
        url = 'https://habr.com' + href
        time = title_times.find('time')['title']  # Дата + время
        t = time.split(',')
        data = t[0]  # Дата
        print(f'{data}: \n{title.text}, {url}')
        #print(article_hubs)
        print('------------')


