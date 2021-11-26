# python
import requests
from bs4 import BeautifulSoup

urlImdbWebSite = "https://www.imdb.com/chart/top"
tagImdb = requests.get(urlImdbWebSite)
tagImdb = BeautifulSoup(tagImdb.content,"html.parser")

dataImdb = tagImdb.find_all("table",{"class":"chart full-width"})

tableOfMovies = (dataImdb[0].contents) [len(dataImdb[0].contents)-2]
tableOfMovies = tableOfMovies.find_all("tr")

for film in tableOfMovies:
    headersMovies = film.find_all("td",{"class":"titleColumn"})
    nameOfMovie = headersMovies[0].text
    nameOfMovie = nameOfMovie.replace("\n","")
    print(nameOfMovie)
    print("--------------------------------------------------------")
