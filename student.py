# python
import time
import locale
locale.setlocale(locale.LC_ALL, 'turkish')
class student:
    def __init__(self,name,surname,no,s_class,):
        self.name = name
        self.surname = surname
        self.no = no
        self.s_class = s_class
    def view(self):
        dosya = open("student.log", "a")
        print(""" 
        Student Name    : {} 
        Student Surname : {}
        Student No      : {}
        Student Class   : {}
        """.format(self.name,self.surname,self.no,self.s_class))
        dosya.write(""" \n        - - -  Student  - - -
        Student Name    : {} 
        Student Surname : {}
        Student No      : {}
        Student Class   : {}
        Registered Date : {}
        """.format(self.name,self.surname,self.no,self.s_class,time.strftime('%c')))
def run():
    liste = []
    x = input("How Many Students Do You Want To Add : ")
    try:
     for i in range(int(x)):
        s_name = input("Name : ")
        s_surname = input("Surname : ")
        s_no = input("No : ")
        s_class = input("Class : ")
        student1 = student(str(s_name), str(s_surname), s_no, str(s_class))
        liste.append(student1)
        print("-------------")
     i = 1
     for list in liste:
         print("        - - -  Student " + str(i) + " - - -")
         list.view()
         i += 1
    except:
        print("Please Enter Decimal Number.")
run()
