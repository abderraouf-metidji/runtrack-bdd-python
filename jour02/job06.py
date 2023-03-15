import mysql.connector

bdd = mysql.connector.connect(
    user='root', 
    password='nbkf213A,',
    host='localhost',
    database='LaPlateforme'
    )

cursor = bdd.cursor()

query = ("SELECT SUM(capacite) AS capacite_totale FROM salles")
cursor.execute(query)

result = cursor.fetchone()[0]

print("La capacité totale des salles est de : {}".format(result))

cursor.close()
bdd.close()