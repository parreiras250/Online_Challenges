# Challenge 1
# Solução pessoal

# def capital_indexes(str):
#     capital_letters =[]
#     for i,j in enumerate(str):
#         if j.isupper():
#             capital_letters.append(i)
#     return capital_letters


# Challenge 2
# Solução pessoal
# def mid(str):
#     size = len(str)
#     middle = size // 2
#     if size % 2 == 0:
#         return ''
#     else:
#         return str[middle]
    
# print(mid('abcde'))

# Challenge 3
# solução pessoal 
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# def count_on(dict):
#    mapped_dict =[]
#    for key, value in dict.items():
#       if value == "online":
#          mapped_dict.append(value)
#    count = len(mapped_dict)
#    return count

# #solução do site: 
# # long version
# def online_count(people):
#     count = 0
#     for person, status in people.items():
#         if status == "online":
#             count += 1
#     return count

# # short version
# def online_count(people):
#     return len([p for p in people if people[p] == "online"])

# Challenge 4
# #solução pessoal: 
# import random

# def random_number():
#     return random.randint(1,100)

# print(random_number())

#         Challenge 5
# Solução pessoal 
# def only_ints(x, y):
#     if isinstance(x,bool) or isinstance(y, bool):
#         return False
#     if isinstance(x,int) and isinstance(y, int):
#         return True
#     else: 
#         return False 
# Solução do site: 
# def only_ints(a, b):
#     return type(a) == int and type(b) == int

#         Challenge 6
# Solução pessoal
# def double_letters(str):
#     for index, element in enumerate(str): 
#       if index < len(str) - 1:
#          next_element = str[index + 1]
#          if element == next_element:
#             return True       
#     else: 
#       return False 
    
# Soluções do site 
# naive solution
# def double_letters(string):
#     for i in range(len(string) - 1):
#         letter1 = string[i]
#         letter2 = string[i+1]
#         if letter1 == letter2:
#             return True
#     return False

# shorter solution
# using a list comprehension, zip, and any
# def double_letters(string):
#     return any([a == b for a, b in zip(string, string[1:])])

#           Challenge 7
# Solução pessoal
# def add_dots(str):
#     new_name = ''
#     for i, j  in enumerate(str):
#         if not i == 0:
#           new_name += f'.{j}'
#         else:
#            new_name += j
#     return new_name

# def remove_dots(str):
#     new_name =''
#     for i in  str:
#         if i != '.':
#            new_name += i
#     return new_name
# #Solução site
# # the longer way
# def add_dots(s):
#     out = ""
#     for letter in s:
#         out += letter + "."
#     return out[:-1]

# def remove_dots(s):
#     out = ""
#     for letter in s:
#         if letter != ".":
#             out += letter
#     return out
# # the short way
# def add_dots(s):
#     return ".".join(s)

# # def remove_dots(s):
#     return s.replace(".", "")

#     Challenge 8
# def count(str):
#     counter = 1
#     for i in str:
#       if i == '-' :
#         counter+=1
#     return counter

# print(count('checked'))

# # naive solution
# def count(word):
#     syllables = 1
#     for letter in word:
#         if letter == "-":
#             syllables = syllables + 1
#     return syllables

# # using the count method
# def count(word):
#     return word.count("-") + 1

# # using split
# def count(word):
#     return len(word.split("-"))   
    