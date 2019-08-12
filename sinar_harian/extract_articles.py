import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.sinarharian.com.my/search/azmin/1/0/0")
bs = BeautifulSoup(r.content, features="html.parser")

articles = bs.find_all("div", {"class": "row spacewithborder"})
for a in articles:
    print(a.find("a", {"class":"title-2"}).text)
    print(a.find("a", {"class":"description-2"}).text)
