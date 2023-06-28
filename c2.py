# Challenge 2
# Solução pessoal
def mid(str):
    size = len(str)
    middle = size // 2
    if size % 2 == 0:
        return ''
    else:
        return str[middle]
    
print(mid('abcde'))