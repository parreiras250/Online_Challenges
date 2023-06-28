# Challenge 1
# Solução pessoal
def capital_indexes(str):
    capital_letters =[]
    for i,j in enumerate(str):
        if j.isupper():
            capital_letters.append(i)
    return capital_letters