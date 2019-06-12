import sqlite3

conn = sqlite3.connect("Database1.db")
cursor = conn.cursor()

def tablo():
    print("Database'e Bağlanılıyor...\n-------------------")

    if conn:
        print("Database'e Bağlandı.\n-------------------\n")
        print("Tablo Oluşturuluyor...\n")
        try:
            print("Tablo Oluşturuldu.\n-------------------\n")
            cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (ad TEXT,soyad TEXT,numara INT,nott INT )")
            conn.commit()
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
        except:
            print("Tablo Oluşturulamadı\nÇıkış Yapılıyor...")
    else:
        print("Database'e Bağlanamadı.\nÇıkış Yapılıyor...")


def ekle():
    ad = input("İsim = ")
    soyad = input("Soyisim = ")
    numara = int(input("Numara = "))
    nott = int(input("Not = "))
    try:
     cursor.execute("INSERT INTO bilgiler (ad,soyad,numara,nott) VALUES (?,?,?,?)",(ad,soyad,numara,nott))
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
    except:
        print("Database'e Eklenemedi.\nÇıkış Yapılıyor...")

def goster():
    print("")

print("Database Bağlan - 1\nVeri Ekle - 2\nVerileri Göster - 3\nDatabase'den Çık - 0 ")
secim = int(input("Seçiminiz : "))

if secim == 1:
 tablo()
elif secim == 2:
 ekle()
elif secim == 3:
 goster()
