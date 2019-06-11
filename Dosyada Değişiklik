# python
Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ
with open("Yazılım.txt","r+") as dosya:
    data = dosya.readlines()
    
    satır = int(input("Eklemek istediğiniz Satır : "))
    satır = satır-1
    
    kelime = input("Eklemek istediğiniz Kelime : ")
    
    data.insert(satır,"{}\n".format(kelime))
    dosya.seek(0)
    dosya.writelines(data)
