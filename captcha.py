# python // YUSUF KILIC
import random
list = "ABCDEFGHIJKLMOPRSTUVYZQWXabcdefghijklmnoprstuvyzqwx0123456789"
mix = random.sample(list,6)
id = ','.join(map(str, mix))
captcha =id.replace(',','')
print("Your Security Code : ",captcha)
while True:
 user_captcha = input("Verify : ")
 if captcha == user_captcha:
  print("Succesfuly Entered")
  break
 print("Please try again")
