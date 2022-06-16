import requests
from bs4 import BeautifulSoup

#URL = input()
URL = 'https://auto.ru/voronezh/cars/skoda/rapid/21738448/all/transmission-automatic/?year_from=2019&year_to=2022&price_to=1500000'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

def get_html(url, params=None):
    res = requests.get(URL, headers)
    return res

def get_pages_count(html):
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find('span', class_='Button__content').find_next('span').text
    if pagination:
        return int(pagination)
    else:
        return 1
    print(pagination)

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='ListingItem__description')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='ListingItemTitle ListingItem__title').get_text(strip=True),
            'link': item.find('a', class_='Link ListingItemTitle__link').get('href'),
            'price': item.find('div', class_='ListingItemPrice__content').find_next('span').text
        })
    return cars



def parse():
    html = get_html(URL)
    print(html)
    if html.status_code == 200:
        get_pages_count(html.text)
        #get_content(html.text)
    else:
        print('error')

parse()

