# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(word1, word2):
    count1 = {}
    count2 = {}

    for letter in word1:
        if letter in count1:
            count1[letter] += 1
        else:
            count1[letter] = 1

    for letter in word2:
        if letter in count2:
            count2[letter] += 1
        else:
            count2[letter] = 1

    if count1 == count2:
        return True
    else:
        return False
        
is_anagram('galeria', 'alergia')
# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
            
