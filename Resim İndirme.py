# python
# Kütüphaneyi tanımlıyoruz
import urllib.request

url="https://upload.wikimedia.org/wikipedia/commons/9/9b/Python_molurus_bivittatus_%283%29.jpg"

#Dosya'ya isim veriyoruz
urllib.request.urlretrieve(url,'python.jpeg')
