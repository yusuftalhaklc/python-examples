# python
Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ
try:
    dosya = open("yusuf.txt","r")
except IOError:
    print("Dosya Bulunamadı")
finally:
    dosya.close()
