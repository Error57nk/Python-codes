import re
class Read:
    file=None
    def main():
        try:
            Read.file = open("./Python.txt", 'r')
            print("File Opened...")
            data = Read.file.read()
            res=re.findall(r'\d{2}',data)
            print("There is %d two digit  number" %len(res))
            print("They are",res)
            print("In Python.txt")
            print(data)
        except Exception as msg:
            print("Error: ",msg)
        finally:
            if Read.file != None:
                Read.file.close()
                print("file closed")
Read.main()