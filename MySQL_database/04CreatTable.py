import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="niteshmysql",
    database="testdb"
    )
print(mydb)
mycr=mydb.cursor()

mycr.execute("CREATE TABLE student(name VARCHAR(255), age INTEGER(10))")
#to creat table name student


