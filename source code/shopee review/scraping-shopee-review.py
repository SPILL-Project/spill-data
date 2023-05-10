import re
import json
import requests
import shopee_product_data

url = 'https://shopee.co.id/TWS-Handsfree-Headset-Earphone-Bluetooth-Wireless-Inpods-i.315471606.8209972668?sp_atk=c8b7824a-cb0d-4813-9f80-ad4bd7e15781&xptdk=c8b7824a-cb0d-4813-9f80-ad4bd7e15781'

r = re.search(r'i\.(\d+)\.(\d+)', url)
shop_id, item_id = r[1], r[2]
ratings_url = 'https://shopee.co.id/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0'

offset = 0
while True:

    data = requests.get(ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)).json()

    # uncomment this to print all data:
    # print(json.dumps(data, indent=4))

    i = 1
    for i, rating in enumerate(data['data']['ratings'], 1):
        print(rating['author_username'])
        print(rating['comment'])
        print('-' * 80)

    if i % 20:
        break

    offset += 20