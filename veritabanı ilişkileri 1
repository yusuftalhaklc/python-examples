# python
#Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ
import sqlite3

con = sqlite3.connect("dersler.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT,numara INT,ogrencinotu INT)")
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('MURAT','COŞKUN','123','82')")
    con.commit()
    con.close()
tablo_olustur()
degerekle()
