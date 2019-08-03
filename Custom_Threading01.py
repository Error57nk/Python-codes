from threading import Thread
import time

class Custom(Thread):
    def run(self):
        for i in range(1,11):
            print("Custom Thread"+str(i),end='\n')
            time.sleep(1)   #one bye one with same delay time
            
        print("Custom Thread Ended")
        return

class Default:
    def main():
        obj=Custom()
        obj.start()
        
        print("Default Thread of Main")
        for i in range(1,11):
            print("*Default Thread"+str(i),end='\n')
            time.sleep(1)   #one bye one with same delay time
        print("Default Thread of Main Ended")
             
        return

Default.main()
