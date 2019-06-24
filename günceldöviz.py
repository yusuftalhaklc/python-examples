# python
import requests
import time
from bs4 import BeautifulSoup
def dolar():
    url = "http://bigpara.hurriyet.com.tr/doviz/dolar/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all("span", {"class": "value up"})
    add =[]
    for i in str(data).split():
        add.append(i)
    data2 = ','.join(map(str, add))
    data3 = data2[24:30]

    dlr = data3.replace(',','.')
    tl = float(dlr)
    return tl
def euro():
    url = "http://bigpara.hurriyet.com.tr/doviz/euro/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all("span", {"class": "value up"})
    add = []
    for i in str(data).split():
        add.append(i)
    data2 = ','.join(map(str, add))
    data3 = data2[24:30]

    dlr = data3.replace(',', '.')
    tl = float(dlr)
    return tl
liste = [dolar(),euro()]
for i in range(1000):
    print("Güncel Dolar : ",dolar(),"              Güncel Euro : ",euro())
    time.sleep(1)
    if liste[0] != dolar():
        print("Dolar Güncellendi.")

    elif liste[1] != euro():
        print("Euro Güncellendi.")
    liste[0] = dolar()
    liste[1] = euro()
