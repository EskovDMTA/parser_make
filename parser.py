import requests
from bs4 import BeautifulSoup

#URL = input()
URL = 'https://auto.ru/voronezh/cars/skoda/rapid/21738448/all/transmission-automatic/?year_from=2019&year_to=2022&price_to=1500000'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

def get_html(url, params=None):
    res = requests.get(URL, headers)
    return res


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ListingItem__description')
    print(items)


def parse():
    html = get_html(URL)
    print(html)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')

parse()

