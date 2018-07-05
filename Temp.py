print('HEllOW HUMANS \n')
print('WELCOME TO CONVERTOR\n')

b = float(input("Enter the Temprature in Celsius"))



def temp(c):
    f=(c*9/5)+32
    k=c+273.15
    print("Temprature in:- \n Celsius(C)= ",c )
    print("\n Fahrenheit(F)= ",f)
    print("\n Kelvin (K)= ",k)
    return c

ab = temp(b)