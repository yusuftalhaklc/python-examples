# python
import requests
import smtplib
from bs4 import BeautifulSoup

mesaj = input("Mesaj gir : ")
str(mesaj)
for i in range(1):
    content1 = str(mesaj)

    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()

    mail.login("yusuftalhaklc@gmail.com","email_şifre")

    mail_url = "https://temp-mail.org/tr/"
    r = requests.get(mail_url)
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all("input", {"class": "emailbox-input opentip"})
    words = []
    x = str(data)
    y = x.split()
    for i in y:
        words.append(i)
    id = ','.join(map(str, words))
    x = id[175:200]
    new = []
    id = ','.join(map(str, new))
    for i in x:
        i.split('/')
        i.replace('/', '')
        i.replace('>', '')
        i.replace(']', '')
        i.replace('"', '')
        new.append(i)

    for a in new:
        i = ','.join(map(str, new))
        i.replace('/', '')
        i.replace('>', '')
        i.replace(']', '')
        i.replace('"', '')
    newnew = []
    a = []
    b = []
    c = []
    d = []

    id = ','.join(map(str, new))
    token = id.replace('/', '')
    newnew.append(token)

    id = ','.join(map(str, newnew))
    token = id.replace('"', '')
    a.append(token)

    id = ','.join(map(str, a))
    token = id.replace(']', '')
    b.append(token)

    id = ','.join(map(str, b))
    token = id.replace('>', '')
    c.append(token)

    id = ','.join(map(str, c))
    token = id.replace(',', '')
    d.append(token)
    x = str(token)
    print(x)
    mail.sendmail("yusuftalhaklc@gmail.com",x,content1)
