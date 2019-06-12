# python
Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ
dosya = open("file.txt","r")
liste = dosya.readlines()
satır = input("Satır Sayısını giriniz : ")
satır = int(satır)
try:
    print(liste[satır-1])
    x = len(liste[satır-1])
    print(x-1)
    print(dosya.read())
except:
    print("Bir Hata Oluştu...")
