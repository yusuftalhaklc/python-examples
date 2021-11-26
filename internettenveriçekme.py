# python
import requests
from bs4 import BeautifulSoup

urlImdbWebSite = "https://www.imdb.com/chart/top"
tagImdb = requests.get(urlImdbWebSite)
tagImdb = BeautifulSoup(tagImdb.content,"html.parser")

dataImdb = tagImdb.find_all("table",{"class":"chart full-width"})

tableOfFilms = (dataImdb[0].contents) [len(dataImdb[0].contents)-2]
tableOfFilms = tableOfFilms.find_all("tr")

for film in tableOfFilms:
    headersFılms = film.find_all("td",{"class":"titleColumn"})
    nameOfFilm = headersFılms[0].text
    nameOfFilm = nameOfFilm.replace("\n","")
    print(nameOfFilm)
    print("--------------------------------------------------------")
