import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': '*/*'}
HOST = 'https://auto.ria.com/newauto/marka-jeep'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    print(items)
    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text(),
            'link': HOST + item.find('a').get('href'),
            'usd price': item.find('span', class_='green').get_text().strip()
        })
    '''
    items = soup.find_all('h3', class_='proposition_name')
    for item in items:
        cars.append({
            'link': item.find('a').get('href')                     можно сделать так, чтобы забрать ссылку из h3
        })
    print(cars)
    '''
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')


parse()
