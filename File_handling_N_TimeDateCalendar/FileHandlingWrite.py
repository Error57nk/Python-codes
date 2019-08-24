import calendar
class Write:
    nw=None
    def main():
        try:
            Write.nw=open("./Python.txt", 'a')
            Write.nw.write("\n")
            Write.nw.write("Nitesh \n\n")
            obj=calendar.month(2019,8)

            print(obj)
            Write.nw.write(obj)
        except Exception as msg:
            print("Error :"+ msg)
        finally:
            if Write.nw != None:
                Write.nw.close()
        return

Write.main()

