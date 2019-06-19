# python
#Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ
import random
import sqlite3

print("- - -RASTGELE İNSAN YARAT - - -")
conn = sqlite3.connect("Randomhuman.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS random (İSİM TEXT,SOYİSİM TEXT,TCNO TEXT,TELEFON TEXT)")

sayı = int(input("Kaç kişi oluşturmak istersiniz : "))

for i in range(sayı):
  tc = "12345670389"
  _name ="YUSUF YUNUS ALİ MERT AKIN ATAHAN ATALAY AYBERK ALİŞAN ALPER ALPARSLAN AYKUT HAKAN FURKAN YAKUP TALHA EMİRHAN AYTAÇ ESMA OYA PINAR SU ARZU ASENA" \
        " AYÇA ALEV ANIL SEDA SUDE AFRA ALİSA AHU HATİCE NİLÜFER ALYA NUR ASUMAN ASLI AYLİN AYBEN AZRA BEGÜM BELİZ "
  _surname = "ŞEN KANDEMİR YILMAZ AY VURAL YAVUZ ÇAY IŞIK BAL KILIÇ DOĞAN SEZER GÜMÜŞAY YİĞİT TÜRK TÜRKDOĞAN YALÇIN ERARSLAN KOÇ" \
            "TEKİN PİRDOĞAN SAĞLAM EYÜP KOPAN GENÇ KARAARSLAN KAHRAMAN BEKİR YÜCE KÖSE KARAMAHMUTOĞLU YILDIZ KILINÇ MUTLU ERSOY ER GÜÇLÜ ÇİÇEK"
  tel = "535 505 545 531 530 533 534 536 537 538 539 561 540 541 542 543 54 546 547 548 549 506 507 551 552 553 554 555 556 557 558"

  # isim
  mixisim = random.sample(_name.split(),1)
  _isim = ','.join(map(str, mixisim))
  isim =_isim.replace(',','')


  # soyisim
  mixsoyisim = random.sample(_surname.split(),1)
  _soyisim = ','.join(map(str, mixsoyisim))
  soyisim =_soyisim.replace(',','')

  # tc
  mix = random.sample(tc, 10)
  id = ','.join(map(str, mix))
  tcno = id.replace(',', '')
  tcno = "1"+ tcno

  #tel no
  mixtel = random.sample(tc,7)
  _tel = ','.join(map(str, mixtel))
  telno = _tel.replace(',', '')

  # tel kod
  mixtelkod = random.sample(tel.split(),1)
  _telkod = ','.join(map(str, mixtelkod))
  telkod = _telkod.replace(',', '')

  telefon = "0"+telkod+telno
  print(i+1,")",isim,"            ",soyisim,"            ",tcno,"            ",telefon)
  cursor.execute("INSERT INTO random(İSİM,SOYİSİM,TCNO,TELEFON) VALUES (?,?,?,?)",(isim,soyisim,tcno,telefon))
  conn.commit()
print("Veritabanına Kaydedildi.")

