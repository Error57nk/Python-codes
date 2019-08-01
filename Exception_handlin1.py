class Err(Exception):
    def __init__(self,name):
        self.name=name
        return
    
class raisee:
    def main():
        print("Program start !!")
        err=Err("Coustom Error")
        try:
            raise err
        except Err as e:
            print("Exception : ",e)
            
        print("end of try")
        
raisee.main()
