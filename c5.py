#         Challenge 5
# Solução pessoal 
def only_ints(x, y):
    if isinstance(x,bool) or isinstance(y, bool):
        return False
    if isinstance(x,int) and isinstance(y, int):
        return True
    else: 
        return False 
    
# Solução do site: 
def only_ints(a, b):
    return type(a) == int and type(b) == int