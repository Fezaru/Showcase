from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.onliner.by/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    with webdriver.Chrome(r'C:\Users\Fezaru\Downloads\chromedriver.exe') as browser:
        browser.get(url)
        return browser.page_source


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    rate = soup.find('span', class_='_u')
    print(rate)


def parse():
    html = get_html(URL)
    get_content(html)


parse()
