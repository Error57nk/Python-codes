import mysql.connector as cn

class DB:
    con=None
    def fetch(entry):
        try:
            
            DB.con = cn.connect(host="localhost",
                                             user="root",passwd="niteshmysql",
                                             database="student")
            print("Connected")
            cur=DB.con.cursor()
            q="select * from account where no=%d ;" %entry
            #print(q)
            cur.execute(q)
            record=cur.fetchall()
            #print(record)
            return record
           
           
               
        except Exception as msg:
            print("Exception :",msg)
           
        finally:
            if DB.con != None:
                DB.con.close()
                print("Sucessfully Dis-Connected")
        

           
