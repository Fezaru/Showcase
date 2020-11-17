import requests
from bs4 import BeautifulSoup

URL = 'https://kurs.onliner.by/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url=url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('p', class_='value')
    print(items[2].get_text())


def parse():
    html = get_html(URL)
    print(html.status_code)
    get_content(html.text)


parse()
