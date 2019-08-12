import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.sinarharian.com.my/article/41684/BERITA/Politik/PM-adakan-pertemuan-dengan-pemimpin-Bersatu")
bs = BeautifulSoup(r.content, features="html.parser")
print(r.content)

comments = bs.find_all("div", {"class": "_3-8y _5nz1 clearfix"})
for comment in comments:
    print(comment.find("span", {"class": "_5mdd"}))
