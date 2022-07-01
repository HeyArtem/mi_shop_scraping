import requests
import os
from bs4 import BeautifulSoup
import time
import random
import json
import csv


"""
Скрапинг сайта 
https://mi-shop.com/ru/catalog/smartphones/
"""

cookies = {
        'g4c_x': '1',
        '_ym_uid': '164323380648062422',
        '_ym_d': '1643233806',
        'PHPSESSID': 'p6fh96qj8a09nurddh0n71sefa',
        'GEO_S_CITY': '3764',
        'GEO_CITY': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
        'GEO_S_CITY_FIAS': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
        'MI_SHOP_SALE_UID': '74018498',
        'JS_AFTER_MINDBOX_INIT': 'Y',
        '_gcl_au': '1.1.152429702.1656197066',
        'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A45%2C%22EXPIRE%22%3A1656277140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
        '__gtm_referrer': 'https%3A%2F%2Fwww.google.com%2F',
        '_userGUID': '0:l4ugyz4m:CihPkCxjvgFEQHxKqk2yylnm~CFncOuM',
        'dSesn': '382c1363-375a-75f5-9330-84983defb1ad',
        '_dvs': '0:l4ugyz4m:p8SjLpgxs5iwpSWR1~ZU_VavkYZJuRXn',
        '_gid': 'GA1.2.442981277.1656197067',
        '_ym_isad': '1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'rrpvid': '5',
        'advcake_trackid': '7b447efc-c180-fdc4-ce37-497f1407872f',
        'advcake_session_id': '026cac2c-a498-966b-ae31-5626a1fa64a9',
        'rcuid': '60e85f85f754950001098bc4',
        'blueID': '02b291dd-6712-4fa1-94e4-103c2ced0a41',
        '_ga_3BHES1ZWN3': 'GS1.1.1656197066.1.1.1656197157.59',
        '_ga_CTM34HX9F5': 'GS1.1.1656197066.1.1.1656197157.0',
        '_ga': 'GA1.2.813165930.1656197067',
        'mindboxDeviceUUID': '3d60faa7-7b1c-4bd8-8b45-1946fd5c5753',
        'directCrm-session': '%7B%22deviceGuid%22%3A%223d60faa7-7b1c-4bd8-8b45-1946fd5c5753%22%7D',
    }

headers = {
    'authority': 'mi-shop.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'g4c_x=1; _ym_uid=164323380648062422; _ym_d=1643233806; PHPSESSID=p6fh96qj8a09nurddh0n71sefa; GEO_S_CITY=3764; GEO_CITY=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; GEO_S_CITY_FIAS=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; MI_SHOP_SALE_UID=74018498; JS_AFTER_MINDBOX_INIT=Y; _gcl_au=1.1.152429702.1656197066; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A45%2C%22EXPIRE%22%3A1656277140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; __gtm_referrer=https%3A%2F%2Fwww.google.com%2F; _userGUID=0:l4ugyz4m:CihPkCxjvgFEQHxKqk2yylnm~CFncOuM; dSesn=382c1363-375a-75f5-9330-84983defb1ad; _dvs=0:l4ugyz4m:p8SjLpgxs5iwpSWR1~ZU_VavkYZJuRXn; _gid=GA1.2.442981277.1656197067; _ym_isad=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; rrpvid=5; advcake_trackid=7b447efc-c180-fdc4-ce37-497f1407872f; advcake_session_id=026cac2c-a498-966b-ae31-5626a1fa64a9; rcuid=60e85f85f754950001098bc4; blueID=02b291dd-6712-4fa1-94e4-103c2ced0a41; _ga_3BHES1ZWN3=GS1.1.1656197066.1.1.1656197157.59; _ga_CTM34HX9F5=GS1.1.1656197066.1.1.1656197157.0; _ga=GA1.2.813165930.1656197067; mindboxDeviceUUID=3d60faa7-7b1c-4bd8-8b45-1946fd5c5753; directCrm-session=%7B%22deviceGuid%22%3A%223d60faa7-7b1c-4bd8-8b45-1946fd5c5753%22%7D',
    'dnt': '1',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


def get_data():
    # запросы буду делать в одной ссесии
    sess = requests.Session()
    
    
    response = sess.get('https://mi-shop.com/ru/catalog/smartphones/', cookies=cookies, headers=headers)
    
    # создаю директорию для сохранения файлов
    if not os.path.exists("data"):
        os.mkdir("data")
        
    # сохраняю страницу
    with open("data/index.html", "w") as file:
        file.write(response.text)
    
    # читаю сохраненную страницу
    with open("data/index.html") as file:
        src = file.read()  
    
    # создаю объект BeautifulSoup
    soup = BeautifulSoup(src, "lxml")
    
    # пагинация
    # last_page = int(soup.find("nav", class_="w-100")["data-pages"]) # если несколько атрибутов, то обращаюсь как к словарю!!
    # last_page = int(soup.find("nav", class_="w-100").get("data-pages")) # если несколько атрибутов, то обращаюсь как к словарю!!
    last_page = int(soup.find("nav", class_="w-100").attrs["data-pages"]) # если несколько атрибутов, то обращаюсь как к словарю!!
    
    # print(last_page)
    
    # инфоблок
    print(f"[info] found {last_page} pages\n")
    
    # переменная для записи json
    all_json_data = []
    
    # переменная для записи в csv
    data = []
        
    
    # генератор ссылок на каждую страницу
    for pagination_page_count in range(1, last_page + 1):
    # for pagination_page_count in range(1, 2):
        pagination_page_url = f"https://mi-shop.com/ru/catalog/smartphones/page/{pagination_page_count}/"
        
        # делаю запрос к каждой странице
        response = sess.get(url=pagination_page_url, cookies=cookies, headers=headers)        
        
        soup = BeautifulSoup(response.text, "lxml")
        
        # общий блок с сылками
        main_block_cards = soup.find("div", class_="card-horizontal-mutable").find_all("div", class_="bg-white")        
        
        for card in main_block_cards:
            
            # модель телефона
            try:
                card_name = card.find("div", class_="product-card__title").text.replace("\n", "").strip()
            except Exception as ex:
                card_name = "No name"
            
            # стоимость телефона
            try:
                card_price = card.find("div", class_="price").find("span", class_="price__new").text.replace(" ", "").replace("\n", "")
            except Exception as ex:
                card_price = "No price"
            
            # сумма скидки на телефон
            try:
                card_discount = card.find("div", class_="price").find("div", class_="sale__badge").text
            except Exception as ex:
                card_discount = "No data discount"
            
            # ссылка на телефон
            try:
                # link_on_card = card.find("div", class_="product-card__body").get("href")
                link_on_card = f'https://mi-shop.com{card.find("div", class_="product-card__body").find("a").get("href")}'
            except Exception as ex:
                link_on_card = "No data link"
            
            # print(f"Card title: {card_name}\n card_price: {card_price}\n Discount: {card_discount}\n Link: {link_on_card}\n ")
            
            # упаковываю данные для дальнейшей записи в json
            all_json_data.append(
                {
                    "card_name": card_name,
                    "card_price": card_price,
                    "card_discount": card_discount,
                    "link_on_card": link_on_card
                }
            )
            
            # упаковываю данные для записи в csv
            data.append(
                [
                    card_name,
                    card_price,
                    card_discount,
                    link_on_card
                ]
            )
            
        # инфоблок
        print(f"[info] complited page {pagination_page_url[-2]} of {last_page}\n")
        
        # пауза между запросами 
        time.sleep(random.randrange(1, 3))
        
            
    # записываю в csv заголовки  значения
    with open("data/data_smartphones.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Model",
                "Price",
                "Discount",
                "Link"
            )
        )
        writer.writerows(data) #записываю значения
        
    # записываю json
    with open("data/all_json_data.json", "w") as file:
        json.dump(all_json_data, file, indent=4, ensure_ascii=False)
        
    # инфоблок
    print(f"[info] data collection completed!")
            

def main():
    get_data()
    

if __name__ == "__main__":
    main()
