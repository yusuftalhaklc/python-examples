# python
#Kendi Kodlarımı Paylaşıyorum...    /  YUSUF KILIÇ
import random
import time

class Enemy:
    health_remaining = 100
    def attack(self):
        print("Charge!")
        self.health_remaining -= random.randint(5,50)
    def check(self):
        if (self.health_remaining <= 0):
            print("YOU DIED")
        else:
            print(str(self.health_remaining) + " Health remaining")


Enemy1 = Enemy()

Enemy1.attack()
time.sleep(1)
Enemy1.attack()
time.sleep(1)
Enemy1.attack()
time.sleep(1)
Enemy1.check()
