from selenium import webdriver
import requests
from bs4 import BeautifulSoup

'''
Пример парсера с selenium, чтобы парсить сайты на джсе
'''



URL = 'https://catalog.onliner.by/videocard'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    with webdriver.Chrome(r'C:\Users\Fezaru\Downloads\chromedriver.exe') as browser:
        browser.get(url)
        return browser.page_source


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='schema-product')
    print(len(items))  # почему то достает только 2 элемента
    for item in items:
        print(item.find('div', class_='schema-product__title').get_text())


def parse():
    html = get_html(URL)
    get_content(html)


parse()
