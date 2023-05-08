from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import mysql.connector

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

driver.set_window_size(1300, 800)

# connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="spill_data"
)

mycursor = mydb.cursor()


# akses ecommerce
jumlah_halaman = 40
for i in range(jumlah_halaman):
    if i == 0:
        continue
    shopee_link = f"https://shopee.co.id/daily_discover?pageNumber={i}"

    driver.get(shopee_link)

    # # scroll browser
    # rentang = 500
    # for i in range(1, 5):
    #     akhir = rentang * i
    #     perintah = "window.scroll(0"+str(akhir)+")"
    #     driver.execute_script(perintah)
    #     time.sleep(1)

    time.sleep(2)

    driver.save_screenshot("home-shopee.png")

    content = driver.page_source

    driver.quit()
    
    data = BeautifulSoup(content, 'html.parser')

    base_url = "https://shopee.co.id"

    j = 1
    # print(data.encode("utf-8"))
    for area in data.find_all('div', class_="httLi0 col-xs-2"):
        # print(area)
        nama = area.find('div', class_="ie3A+n Cve6sh").get_text()
        gambar_elem = area.find('img')
        if gambar_elem.has_attr('src'):
            gambar = gambar_elem['src']
        else:
            break
        # gambar = gambar_elem['src'] if gambar_elem.has_attr('src') else ''
        harga = area.find('span', class_="juCMSo").get_text()
        link = base_url + area.find('a')['href']
        terjual = area.find('div', class_="r6HknA dQAXj1").get_text()
        # if terjual != None:
        #     terjual.get_text()

        print(f"\nData ke-{j}\n")
        print(f"Nama:\n{nama}")
        print(f"Gambar:\n{gambar}")
        print(f"Harga STR:\nRp {harga}")
        print(f"Harga INT:\n{int(harga.replace('.', ''))}")
        print(f"Link:\n{link}")
        print(f"Terjual:\n{terjual}")
        print()
        print("==="*10)
        data_shopee = (nama, gambar, int(harga.replace('.', '')), link, terjual)
        sql = "INSERT INTO product_raw (judul, gambar, harga, link, terjual) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, data_shopee)
        mydb.commit()
        print(mycursor.rowcount, "data berhasil ditambahkan")
        print("==="*10)
        print()
        j += 1

        # time.sleep(5)

    # print(f"\nJUMLAH HALAMAN : {i}")
    # print(f"JUMLAH DATA    : {i*j}\n")

    print(f"JUMLAH DATA    : {j-1}\n")

    # time.sleep(20)