import re
text_= input()
def acronym(tex):
    list_=re.sub(r"([a-zA-Z])[a-z,A-Z]+\s*",r"\1",tex).upper()
    return list_
print(acronym(text_))
