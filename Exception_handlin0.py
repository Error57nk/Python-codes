class Err(Exception):
    def __init__(self,name):
        self.name=name
        return
    
class raisee:
    def main():
        print("Program start !!")
        err=Err("Coustom Error")
        raise err
        print("end of try")
        
raisee.main()
