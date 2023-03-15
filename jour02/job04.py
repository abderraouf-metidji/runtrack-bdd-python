import mysql.connector

bdd = mysql.connector.connect(
    user='root', 
    password='nbkf213A,',
    host='localhost',
    database='LaPlateforme'
    )

cursor = bdd.cursor()

query = ("SELECT nom, capacite FROM salles")

cursor.execute(query)

for (nom, capacite) in cursor:
    print("{} - Capacité : {}".format(nom, capacite))

cursor.close()
bdd.close()