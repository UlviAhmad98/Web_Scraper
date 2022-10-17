import os
import requests
import string
from bs4 import BeautifulSoup

page = int(input())
article_type = input()

main_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"

if page == 0:
    pass
else:
    for n in range(1, page + 1):
        response = requests.get(main_url + "&page=" + str(n))
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.findAll("li", {"class": "app-article-list-row__item"})
        os.mkdir(f"Page_{n}")
        for article in articles:
            category = article.find('span', {'class': 'c-meta__type'}).text
            if category == article_type:
                title = article.find('a').text
                for character in string.punctuation:
                    title = title.replace(character, "")
                title = title.replace(" ", "_").replace("’", "") + '.txt'

                link = 'https://nature.com' + article.find('a').get('href')
                page = requests.get(link)
                soup2 = BeautifulSoup(page.content, 'html.parser')
                body = soup2.find('div', {'class': 'c-article-body'}).text.strip()
                current_directory = f"{os.getcwd()}\\Page_{n}"
                page_directory = os.path.join(current_directory, title)

                with open(page_directory, 'w', encoding="utf-8") as f:
                    f.write(body)

