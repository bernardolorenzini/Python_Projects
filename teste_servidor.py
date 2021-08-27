import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin506606",
    database="condominio_turin"
)

mycursor = db.cursor()
#CRIANDO DATABASE TESTE  ----
# mycursor.execute("CREATE DATABASE condominio_turin DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci )

# CRIANDO TABELA PESSOAS ----- mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# DESCREVENDO TABELA CRIADA ---- mycursor.execute("DESCRIBE Person")

#  mycursor.execute("INSERT INTO Person(name, age) VALUES (%s,%s)",("Bernardo", 29))

mycursor.execute("INSERT INTO Predio (apID) VALUES (601)")
mycursor.execute("INSERT INTO Predio (apID) VALUES (602)")
mycursor.execute("INSERT INTO Predio (apID) VALUES (603)")
mycursor.execute("INSERT INTO Predio (apID) VALUES (604)")
db.commit()

#mycursor.execute("INSERT INTO Person(name, age) VALUES (%s,%s)",("Maria", 26))
#db.commit()
#mycursor.execute("SELECT * FROM Person")

