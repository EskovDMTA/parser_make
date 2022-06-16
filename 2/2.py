import requests
from bs4 import BeautifulSoup
import json

#URL= 'https://health-diet.ru/table_calorie/'
#DOMEN = 'https://health-diet.ru'
headers = {"accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
           }
#
#req = requests.get(URL, headers=headers)
#src = req.text
#
#with open('index.html', 'w') as file:
#    file.write(src)


#with open('index.html') as file:
#    src = file.read()
#
#soup = BeautifulSoup(src, 'lxml')
#all_products_hrefs = soup.find_all('a', class_="mzr-tc-group-item-href")
#
#all_categories_dict = {}
#for item in all_products_hrefs:
#    item_text = item.text
#    item_href = DOMEN + item.get('href')
#    all_categories_dict[item_text] = item_href
#
#with open('all_categories_dict.json', 'w') as file:
#    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dict.json') as file:
    all_categories = json.load(file)
count = 0
for category_name, category_href in all_categories.items():
    if count == 0:
        rep = [',', ' ', '-', "'"]
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, '_')
        req = requests.get(url=category_href, headers=headers)
        src = req.text

        with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)

        with open(f'data/{count}_{category_name}.html') as file:
            src = file.read()
         soup = BeautifulSoup(src, 'lxml')

        count += 1