import requests
from bs4 import BeautifulSoup

shopee_link = "https://shopee.co.id/daily_discover?pageNumber=2"

response = requests.get(shopee_link)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

base_url = "https://shopee.co.id"

i = 1

for area in soup.find_all('div', class_="httLi0 col-xs-2"):
    nama = area.find('div', class_="ie3A+n Cve6sh").get_text()
    gambar_elem = area.find('img')
    gambar = gambar_elem['src'] if gambar_elem.has_attr('src') else ''
    harga = area.find('span', class_="juCMSo").get_text()
    link = base_url + area.find('a')['href']
    terjual = area.find('div', class_="r6HknA dQAXj1")
    if terjual != None:
        terjual.get_text()

    print(f"\nData ke-{i}\n")
    print(f"Nama:\n{nama}")
    print(f"Gambar:\n{gambar}")
    print(f"Harga:\nRp {harga}")
    print(f"Link:\n{link}")
    print(f"Terjual:\n{terjual}")
    print()
    print("==="*10)
    print()
    i += 1

print(f"\nJUMLAH DATA : {i}\n")
