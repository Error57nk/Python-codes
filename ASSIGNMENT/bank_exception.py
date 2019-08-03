class Err(Exception):
    def __init__(self,name):
        self.name=name
        return
    def Error():
        err=Err(" Low Balance ")
        raise err
        return

class Account:
    def __init__(self,bal):
        self.__balance=bal
        return
    
    def GetBalance(self):
        return self.__balance

    def Withdraw(self,amt):
        try:
            if(self.__balance < amt):
                Err.Error()
            else:
                Y= self.__balance - amt
                self.__balance=Y
        except Err as e:
            print("Exception ",e)

class Bank:
    def main():
        bal=int(input("Enter Balance : "))
        obj=Account(bal)
        print("Your Balance : ",obj.GetBalance())
        amt=int(input("Enter amount to withddraw : "))
        obj.Withdraw(amt)
        print("Available Balance : ",obj.GetBalance())
        return

Bank.main()
                
            
    
