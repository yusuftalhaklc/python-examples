# python
import requests
from bs4 import BeautifulSoup
imdb_url = "https://www.imdb.com/chart/top"
r = requests.get(imdb_url)
soup = BeautifulSoup(r.content,"html.parser")
gelen_veri = soup.find_all("table",{"class":"chart full-width"})
filmtablo = (gelen_veri[0].contents) [len(gelen_veri[0].contents)-2]
filmtablo = filmtablo.find_all("tr")
for film in filmtablo:
    filmbasliklari = film.find_all("td",{"class":"titleColumn"})
    filmismi = filmbasliklari[0].text
    filmismi = filmismi.replace("\n","")
    print(filmismi)
    print("--------------------------------------------------------")
