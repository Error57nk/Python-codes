import pickle
from emp import Employee

class Serialization:
    file=None
    def main():
        e1=Employee(101,'Annie')
        print("object is ready")
        try:
            Serialization.file=open("abc.txt",mode='wb')
            pickle.dump(e1,Serialization.file)
            print("Serialized")
        except Exception as msg:
            print("Error:",msg)
        finally:
            if Serialization.file != None:
                Serialization.file.close()
        return
Serialization.main()


