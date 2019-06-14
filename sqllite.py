# Python Created by YUSUF KILIC
# %% <<<
import sqlite3
import random
def CreateSQL():
    print(" - - - CREATE SQL - - - ")
    SQL_name = input("SQL Name = ")
    global conn
    conn = sqlite3.connect(SQL_name+".db")
    global cursor
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS group_skills(id TEXT ,p_name TEXT,p_surname TEXT,p_age INT,p_skills TEXT)")
def Add_data():
    print(" - - - ADD DATA - - -")
    sql_name = input("Registered Database = ")
    conn = sqlite3.connect(sql_name + ".db")
    cursor = conn.cursor()
    p_name = input("Name = ")
    p_surname = input("Surname = ")
    p_age = input("Age = ")
    p_skills = input("Skills = ")
    list = "abcdefghijklmnoprstuvyzqwx0123456789"
    mix = random.sample(list, 6)
    sort = ','.join(map(str, mix))
    id = sort.replace(',', '')

    try:
     cursor.execute("INSERT INTO group_skills(id,p_name,p_surname,p_age,p_skills) VALUES (?,?,?,?,?)",(id,p_name,p_surname,p_age,p_skills))
     conn.commit()
     print("Your data has been added.")
    except:
        print("Could not add your data.")
        print("Logging out...")
        conn.close()
def View_data():
    sql_name = input("Registered Database = ")
    conn = sqlite3.connect(sql_name + ".db")
    cursor = conn.cursor()
    print("   ID', '  NAME', ' SURNAME ', AGE , 'SKILLS'")
    cursor.execute("SELECT * FROM group_skills")
    data = cursor.fetchall()
    for i in data:
        print(i)
def Query_data():
    while True:
     print(" - - - Select - - -\nCreate Database - 1\nAdd data - 2\nView data - 3\nExit - 0")
     choice = int(input("Choice = "))
     if   choice == 1:
         CreateSQL()
     elif choice == 2:
         Add_data()
     elif choice == 3:
         View_data()
Query_data()
