#           Challenge 7
# Solução pessoal
def add_dots(str):
    new_name = ''
    for i, j  in enumerate(str):
        if not i == 0:
          new_name += f'.{j}'
        else:
           new_name += j
    return new_name

def remove_dots(str):
    new_name =''
    for i in  str:
        if i != '.':
           new_name += i
    return new_name

#Solução site
# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out
# the short way
def add_dots(s):
    return ".".join(s)
def remove_dots(s):
    return s.replace(".", "")