s1='07:05:45PM'
s2='12:05:45AM'

s=s1  #change date 

s=s.split(':')
cp=s[2]
s[2]=cp[:2]
cp=s[2]
a=cp[2:]
print(a)

if a=='PM':
    a=int(s[0])+12
    if(a==24):
        s[0]='00'
    else:
        s[0]=str(a)
    
    #print(s[0])
    s=':'.join(s)
    print(s)
else:
    print(s2[:8])

#S1-> 19:05:45
#s2-> 00:05:45

