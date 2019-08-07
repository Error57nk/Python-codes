import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="niteshmysql"
    )
print(mydb)
mycr=mydb.cursor()
mycr.execute("SHOW DATABASES") #to show data base
for db in mycr:
    print(db)
