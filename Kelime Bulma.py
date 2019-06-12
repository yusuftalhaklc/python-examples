# python
""" Yazılım.txt ' in içi
Java
Python
C#
Ruby
JavaScript
JavaScript
"""
fileway = input("Dosya yolunu giriniz: ")

try:
 with open(fileway,"r") as dosya:
    word = input("Kelimenizi giriniz: ")
    ks = len(word)
    toplam = dosya.read()
    toplam = len(toplam)
    print("Toplam karakter sayısı:",toplam)
    s = 0
    for i in range(0,toplam):
        dosya.seek(i)
        dosya.read(ks)
        if(dosya.read(ks) == word):
            s+=1
    print(s,"adet","'",word,"'","bulundu")
except FileNotFoundError:
    print("Dosya Bulunamadı.")
# çıktı -------------
"""
Dosya yolunu giriniz: Yazılım.txt  veya  C:\Users\your_pc_name\Desktop\Yazılım.txt
Kelimenizi giriniz: JavaScript
Toplam karakter sayısı: 41
2 adet ' JavaScript ' bulundu
""
