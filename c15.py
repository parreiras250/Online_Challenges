# # Consecutive zeros
# # The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
# Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

# # "1001101000110"
# # The biggest number of consecutive zeros is 3.

# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.

#solução pessoal
def consecutive_zeros(number):
  splits = number.split('1')
  bigger_value = 0
  for value in splits:
    acutal_size = len(value)
    if acutal_size > bigger_value:
      bigger_value = acutal_size    
  return bigger_value

print(consecutive_zeros('1001101000110'))
            

# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])