class Atprop:
    def __init__(self,val):
        self._val=val
        return

    def getval(self):
        print("GetVal Function")
        return self._val

    def setval(self,val):
        print("SetVal Function",val)
        self._val=val
        return

    def dltval(self):
        print("Val deleted Function")
        del self._val
        return
    value=property(getval, setval, dltval, )

obj=Atprop("Python") #Setting
print(obj.value)    #Getiing

obj.value="Nitesh" #Setting

print(obj.value) #Getting

del obj.value    #Deleting

obj.value="Nit" #Setting

print(obj.value) #Getting