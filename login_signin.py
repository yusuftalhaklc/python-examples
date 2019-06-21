import random
import sqlite3

conn = sqlite3.connect("verify.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS verify(username TEXT,password TEXT,token TEXT,u_name TEXT)")

def token():
    list = "ABCDEFGHIJKLMOPRSTUVYZQWXabcdefghijklmnoprstuvyzqwx0123456789"
    mix = random.sample(list, 50)
    id = ','.join(map(str, mix))
    token = id.replace(',', '')
    return token
def login():
    login = input("Username or Token : ")
    cursor.execute("SELECT * FROM verify WHERE username = '%s'"%login)
    data =cursor.fetchone()
    if data:
        password = input("Password : ")
        cursor.execute("SELECT * FROM verify WHERE username = '%s' and password ='%s'"%(login,password))
        data1 = cursor.fetchone()
        if data1:
            cursor.execute("SELECT * FROM verify WHERE username = '%s'"%login)
            x = cursor.fetchone()
            print("Welcome ",x[3])
        else:
            print("Wrong Password.")
    else:
        pass
    cursor.execute("SELECT * FROM verify WHERE token = '%s'"%login)
    data2 = cursor.fetchone()
    if data2:
        cursor.execute("SELECT * FROM verify WHERE token = '%s'" % login)
        x = cursor.fetchone()
        print("Welcome ", x[3])
    else:
        print("Wrong Username Or Token")
def sign_in():
    print("Registration with Token - 1")
    print("Registration with Username and Password - 2")
    choice = input("Choice : ")
    if choice == "1":
       while True:
        _name = input("Name : ")
        x = token()
        print("Your Token : ",x)
        _username = "NULL"
        _password = "NULL"
        cursor.execute("INSERT INTO verify(username,password,token,u_name) VALUES (?,?,?,?)",
                       (_username, _password, x, _name))
        conn.commit()
        print("Registered.")
        print("Welcome " + _name)
        save = _name+" Token  = "+x
        dosya = open("Token.log", "a")
        dosya.write(save+"\n")
    elif choice == "2":
        while True:
         name = input("Name : ")
         username = input("Username : ")
         if len(username) <6:
            print("Enter more than six characters")
         else:
             break
        while True:
         password = input("Password : ")
         verifypass = input("Verify Password : ")
         _token = "NULL"
         if password == verifypass:
            cursor.execute("INSERT INTO verify(username,password,token,u_name) VALUES (?,?,?,?)",(username,password,_token,name))
            conn.commit()
            dosya = open("Username_and_password.log","a")
            write = "Username = "+username+" Password = "+password+" Name = "+name
            dosya.write(write+"\n")
            print("Registered.")
            print("Welcome "+name)
            break
         else:
            print("Wrong Password")
    else:
            print("Wrong choice!")
print("Login   - 1")
print("Sign in - 2")
while True:
  choice = input("Choice : ")
  if choice == "1":
       login()
       break
  elif choice == "2":
       sign_in()
       break
  else:
      print("Wrong choice!")
