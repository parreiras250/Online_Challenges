# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.

# Name your function flatten. It should take a single parameter and return a list.

# For example, calling:

# flatten([[1, 2], [3, 4]])
# Should return the list:

# [1, 2, 3, 4]
# Solução pessoal

def flatten(list1):
    new_list = []
    for sublists in list1:
        for itens in sublists:
            new_list.append(itens)       
    return new_list

#outra forma - mais pythonica 
def flatten(list1):
    new_list =[]
    for sublists in list1:
        new_list.extend(sublists)
    return new_list
      

#solução do site
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]