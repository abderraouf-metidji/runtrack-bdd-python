import mysql.connector

bdd = mysql.connector.connect(
    user='root', 
    password='nbkf213A,',
    host='localhost',
    database='LaPlateforme'
    )

cursor = bdd.cursor()

query = ("SELECT SUM(superficie) AS superficie_totale FROM etage")
cursor.execute(query)

result = cursor.fetchone()[0]

print("La superficie de La Plateforme est de {} m2".format(result))

cursor.close()
bdd.close()