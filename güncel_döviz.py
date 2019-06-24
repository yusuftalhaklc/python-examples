# python
import requests
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
def dolartotl():
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
    try:
       dolar = float(input("Dolar to TL : "))
       x = tl * dolar
       print(dolar,"Dolar",round(x),"TL")
    except:
        print("Please Enter Decimal Number")
def eurototl():
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
    try:
        euro = float(input("Euro to TL : "))
        x = tl * euro
        print(euro, "Euro", round(x), "TL")
    except:
        print("Please Enter Decimal Number")
print("1 - Dolar : ",dolar(),"TL")
print("2 - Euro  : ",euro()," TL")
while True:
    choice = input("Choice : ")
    if choice == "1":
        dolartotl()
    elif choice == "2":
        eurototl()
