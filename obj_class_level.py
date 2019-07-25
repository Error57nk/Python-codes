class Account:
    def __init__(self,bln):
        self.balance=bln
        return
    
    def getbln(self):
        x=self.balance
        return x
    
    def withdraw(self,amnt):
        if(self.balance>=amnt):
            r=self.balance
            p=r-amnt
            self.balance=p
        else:
            print("Insufficint balance")
        return
    def avl_bal(self):
        print("Balance available : ",self.balance)
        return
    
class bank :
    def main():
        print("Enter Balance")
        y=int(input())
        obj=Account(y)
        print("get blace",Account.getbln)
        Account.avl_bal(obj)
        wt=int(input("enter withdraw amount"))
        Account.withdraw(obj,wt)
        Account.avl_bal(obj)
        print("get blace",Account.getbln)
        

        return

bank.main()
        
            
