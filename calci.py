
# coding: utf-8

# In[9]:


a=0
while(a==0):
    print('Welcome to Coustom Calculator\n for  Add  Sub  Multi  Div ')
    val_a=float(input(' Enter the first value or 0 for exit '))
    if(val_a==0):
        break
    val_b=float(input(' Enter the first value '))
    opt=input('Enter the Opration to perform or \n 1.Add \n 2.Sub \n 3.Multi \n 4.Div \n 0.EXIT \n')
    if opt=='+' or opt=='1':
        print('Adding')
        result=val_a + val_b
        print('The ressult is',result)
    
    elif opt=='-' or opt=='2':
        print('Subtracting')
        result=val_a - val_b
        print('The ressult is',result)
    
    elif opt=='*' or opt=='3':
        print('multiplying')
        result=val_a * val_b
        print('The ressult is',result)
    
    elif opt=='/' or opt=='4':
        print('Dividing')
        result=val_a / val_b
        print('The ressult is',result)
    elif opt=='0' or opt=='o':
        print('Closing')
        a=12
        break
    else:
        print('Error 404xfoo32 \n Try Again !! ')
    

