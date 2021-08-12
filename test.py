import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.reachforthestarss.com/post/the-departments-of-reach-for-the-stars')

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())