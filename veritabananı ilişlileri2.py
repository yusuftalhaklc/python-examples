# python
# Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ

import sqlite3


conn = sqlite3.connect("Database1.db")
cursor = conn.cursor()

def tablo():


    print("Database'e Bağlanılıyor...\n-------------------")

    if conn:
     print("Database'e Bağlandı.\n-------------------\n")
     print("Tablo Oluşturuluyor...")
    else:
     print("Database'e Bağlanamadı.\nÇıkış Yapılıyor...")
    try:
     print("Tablo Oluşturuldu.\n-------------------\n")
     cursor.execute("CREATE TABLE IF NOT EXISTS bilgi (ad TEXT,soyad TEXT,numara INT,nott INT )")
     print("Database Bağlan - 1\nVeri Ekle - 2\nVerileri Göster - 3\nDatabase'den Çık - 0 ")
     secim = input("Seçiminiz : ")
     secim = int(secim)
     while True:
         if secim == 1:
             tablo()
         elif secim == 2:
             ekle()
         elif secim == 3:
             goster()

     print("Çıkıldı.")
    except:
        print("Tablo Oluşturulamadı\nÇıkış Yapılıyor...")
def ekle():
    ad = input("İsim = ")
    soyad = input("Soyisim = ")
    numara = int(input("Numara = "))
    nott = int(input("Not = "))
    try:
     cursor.execute("INSERT INTO bilgi (ad,soyad,numara,nott) VALUES (?,?,?,?)",(ad,soyad,numara,nott))
     conn.commit()
     print("Database'e Eklendi.\n")
     print("Database Bağlan - 1\nVeri Ekle - 2\nVerileri Göster - 3\nDatabase'den Çık - 0 ")
     secim = input("Seçiminiz : ")
     while True:
         if secim == 1:
             tablo()
         elif secim == 2:
             ekle()
         elif secim == 3:
             goster()


     print("Çıkıldı.")
    except:
        print("Database'e Eklenemedi.\nÇıkış Yapılıyor...")

def goster():
    print("hi")
def isle():
    print("Database Bağlan - 1\nVeri Ekle - 2\nVerileri Göster - 3\nDatabase'den Çık - 0 ")
    secim = input("Seçiminiz : ")
    while True:
     if secim == 1:
            tablo()
     elif secim == 2:
            ekle()
     elif secim == 3:
            goster()
isle()
