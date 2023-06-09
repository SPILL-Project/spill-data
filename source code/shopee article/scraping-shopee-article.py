import requests
from bs4 import BeautifulSoup

url = 'https://www.pricebook.co.id/article'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/113.0.0.0 Safari/537.36'}

r = requests.get(url, headers=headers)
# print(r.status_code)
soup = BeautifulSoup(r.content, features='lxml')

articles = soup.find_all('div', class_='panel-article inside')

# print(articles)

articles_dataset = list()
for item in articles:
    try:
        title = item.find('h2', class_='media-heading title-article mt-1').text
        article_type = item.find('label', class_='label label-success').text
        date = item.find('time', class_='small text-muted').text
        image = item.find('img')['src']
        link = item.find('a')['href']
        # print('-'*100)
        # print(f'{title}\n{article_type}\n{date}\n{image}\n{link}')
        # print('-'*100)
        article = {
            'title': title,
            'article_type': article_type,
            'date': date,
            'image': image,
            'link': link
        }
        articles_dataset.append(article)
    except:
        pass

for data in articles_dataset:
    print(data)
