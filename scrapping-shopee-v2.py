from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

shopee_link = "https://shopee.co.id/daily_discover?pageNumber=1"

driver.set_window_size(1300, 800)

# fungsi untuk mengambil data dari satu halaman
def scrape_data(driver):
    content = driver.page_source
    data = BeautifulSoup(content, 'html.parser')
    base_url = "https://shopee.co.id"
    i = 1
    for area in data.find_all('div', class_="httLi0 col-xs-2"):
        print(f"\nData ke-{i}\n")
        nama = area.find('div', class_="ie3A+n Cve6sh").get_text()
        link = base_url + area.find('a')['href']
        terjual = area.find('div', class_="r6HknA dQAXj1").get_text()
        gambar_elem = area.find('img')
        gambar = gambar_elem['src'] if gambar_elem.has_attr('src') else ''
        harga_elem = area.find('span', class_="juCMSo")
        harga = harga_elem.get_text() if harga_elem else ''
        print(f"Nama\t: {nama}")
        print(f"Gambar\t: {gambar}")
        print(f"Harga\t: Rp {harga}")
        print(f"Link\t: {link}")
        print(f"Terjual\t: {terjual}")
        print()
        print("==="*10)
        print()
        i += 1
    return i

driver.get(shopee_link)
time.sleep(5)

# scrap data di halaman 1
total_data = scrape_data(driver)

# scrap data di halaman berikutnya (jika ada)
while True:
    try:
        # cari tombol next page
        next_button = driver.find_element_by_xpath("shopee-icon-button shopee-icon-button--right")
        # klik tombol next page
        next_button.click()
        time.sleep(5)
        # scrap data di halaman berikutnya
        total_data += scrape_data(driver)
    except:
        # jika tombol next page tidak ditemukan, keluar dari loop
        break

driver.quit()

print(f"Total Data : {total_data}")