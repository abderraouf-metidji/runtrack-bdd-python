import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'nbkf213A,',
    database = 'LaPlateforme'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT  * FROM  etudiants")

etudiants = mycursor.fetchall()

for etudiant in etudiants:
    print(etudiant)

mycursor.close()
mydb.close()