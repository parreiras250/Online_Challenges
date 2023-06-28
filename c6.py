#         Challenge 6
# Solução pessoal
def double_letters(str):
    for index, element in enumerate(str): 
      if index < len(str) - 1:
         next_element = str[index + 1]
         if element == next_element:
            return True       
    else: 
      return False 
    
# Soluções do site 
# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])