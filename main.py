import requests
from bs4 import BeautifulSoup

link = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find(class_="gallery").find_all(class_='title')
titles = [title.get_text() for title in titles][::-1]

with open('movies.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(title + '\n')
