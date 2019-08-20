import re

text ="my book is my Book Not your book"
found =re.search(r'Bok',text)
if found:
    print("Yes found->",found.group())
else:
    print("not found->",found)