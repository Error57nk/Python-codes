import time
import calendar as c

sec=time.time()
print(sec)

info=time.localtime(sec)
#print(info)

#Printing Year only
print("Year : %d" %info.tm_year)

#Printing Month only
print("Month : %d" %info.tm_mon)

#Printing Day only
print("Day : %d" %info.tm_mday)

#Printing Date in DD-MM-YY format
print("Date : %d-%d-%d" %(info.tm_mday, info.tm_mon, info.tm_year))

#Printing Time in HH-MM-SS format
print("Time : %d:%d:%d" %(info.tm_hour, info.tm_min, info.tm_sec))

print()
#printing 2019 month 8
cl=c.month(2019,8)
print(cl)
