# python
Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ

veri1 = input("Karekökünü hesaplamak istediğiniz sayı: ")
try:
 karekök = int(veri1) ** 0.5
 print(veri1, "sayısının karekökü: ", karekök)
except ValueError:
    print("Lütfen 10'luk değer girniz.")

#--------------------------------------------------------

veri2 = input("Karesini hesaplamak istediğiniz sayı: ")
try:
  kare = int(veri2) ** 2
  print(veri2, "sayısının karesi: ", kare)
except ValueError:
    print("Lütfen 10'luk değer giriniz.")
