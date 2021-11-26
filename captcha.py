# python // YUSUF KILIC
import random

listOfCharacters = "ABCDEFGHIJKLMOPRSTUVYZQWXabcdefghijklmnoprstuvyzqwx0123456789"
mixCharacters = random.sample(listOfCharacters,6)

captchaCode = ','.join(map(str, mixCharacters))
captchaCode = id.replace(',','')

print("Your Security Code : ", captchaCode)

while True:
 getCaptcha = input("Verify : ")
 
 if (captchaCode == getCaptcha):
  print("Succesfuly Entered")
  break
  
 print("Please try again")
