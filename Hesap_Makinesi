# python

def toplama():

    s1 = int(input("Sayı gir : "))
    s2 = int(input(("Sayı gir : ")))
    top = s1+s2
    print("{0} + {1} = {2}".format(s1,s2,top))

def cikarma():
    s1 = int(input("Sayı gir : "))
    s2 = int(input(("Sayı gir : ")))
    if s1<s2:
        print("1.değer 2.değerden küçük olamaz.")
    else:
        top = s1 - s2
        print("{0} - {1} = {2}".format(s1, s2, top))
def carpma():
    s1 = int(input("Sayı gir : "))
    s2 = int(input(("Sayı gir : ")))
    top = s1 * s2
    print("{0} * {1} = {2}".format(s1, s2, top))
def bolme():
    s1 = input("Sayı gir : ")
    s2 = input("Sayı gir : ")
    try:
        top = float(s1) / float(s2)
        print("{0} / {1} = {2}".format(s1, s2, top))
    except (ValueError,ZeroDivisionError):
        print("Bir Hata Oluştu")


print("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme")
secim = str(input("Seçim : "))

if secim == "1":
       toplama()
elif secim == "2":
       cikarma()
elif secim == "3":
       carpma()
elif secim == "4":
       bolme()
else:
    print("Hacker çocuk")
