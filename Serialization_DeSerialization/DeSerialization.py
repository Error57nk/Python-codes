import pickle
from emp import Employee

class DeSerialization:
    file=None
    def main():
        try:
            # DeSerialization.file=open("abc.txt",mode="rb")
            DeSerialization.file=open("abc.bin",mode="rb")
            e2=pickle.load(DeSerialization.file)
            print("DeSerialization complete")
            print("Eno: ",e2.no)
            print("Name: ",e2.name)
        except Exception as msg:
            print("Error:",msg)
        finally:
            if DeSerialization.file != None:
                DeSerialization.file.close()
        return

DeSerialization.main()
