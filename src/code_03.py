"""
Given an array of integers, return the sum of all the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
Notes:

If the input_arr does not contain any positive integers, the default sum should be 0.
[execution time limit] 4 seconds (py3)

[input] array.integer input_arr

[output] integer

Expected Output:
---------------
print(csSumOfPositive([1, 2, 3, 4, 5])) -> 15 
print(csSumOfPositive([1, -2, 3, 4, 5])) -> 13  
print(csSumOfPositive([-1, 2, 3, 4, -5])) -> 9  
print(csSumOfPositive([])) -> 0
"""
def csSumOfPositive(input_arr):
    #  Making empty array
    positive = []
    #  Go over each number in array
    for number in input_arr:
        #  if number greater than zero
        if number > 0:
            #  put number in positive way
            positive.append(number)
    #  sum all numbers in positive
    print(positive)
    result = sum(positive)
    return result

print(csSumOfPositive([1, 2, 3, 4, 5]))
print(csSumOfPositive([1, -2, 3, 4, 5]))
print(csSumOfPositive([-1, 2, 3, 4, -5]))
print(csSumOfPositive([]))

