# python
#Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ

# Fonksiyonlarda Recursion

def faktoriyel(n):
# Eğer kullanıcı 1 girmiş ise 1 olarak geri döndürüyor
    if n==1 :
        return 1
    else:
        return n*faktoriyel(n-1)
a = int(input('faktoriyel:'))
print(faktoriyel(a))
