import re
text="java and python makes pyclass"
res=re.match(r'java',text) #matching one

#res=re.match(r'jqav',text) #not matching one
#It match only the first letter or word of text
#when matched it return object add else None

if res:
    print("The result",res)
else:
    print("Not matched",res)