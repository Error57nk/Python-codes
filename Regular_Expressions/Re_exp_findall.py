import re

text="Your name is not = my name"

res=re.findall(r'sn',text)

print(res)
try:
    print("Found",len(res),res[0])
except IndexError as msg:
    print("there is no val present: ",msg)