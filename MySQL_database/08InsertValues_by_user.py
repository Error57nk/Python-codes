import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="niteshmysql",
    database="testdb"
    )
print(mydb)
mycr=mydb.cursor()

while True:
    
    try:
        nam=input("Enter Name: ")
        age=int(input("Enter age: "))
        mycr.execute('''insert into student values("%s", %d)''' %(nam, age))
        mydb.commit()
        print("Record Stored in DataBase Succesfully !")
    except Exception as m:
        print("ERROR: ",m)
        break

    
    print("Press [Y/N] for more record")
    ch=input()
    if(ch == 'N' or ch == 'n'):
        break
    else:
        pass
            
print("ALL RECORD HAVE BEEN SAVED !!")






        
    









