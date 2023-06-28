#     Challenge 8
#Solução pessoal
def count(str):
    counter = 1
    for i in str:
      if i == '-' :
        counter+=1
    return counter

print(count('checked'))

# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))   