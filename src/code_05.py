"""
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12

Notes:

The output can contain the digit 5.
The start number will always be less than the end number (both numbers can also be negative).
[execution time limit] 4 seconds (py3)

[input] integer start

[input] integer end

[output] integer

Expected Output:
---------------
print(csAnythingButFive(1, 9)) # -> 8
print(csAnythingButFive(4, 17)) # -> 12
print(csAnythingButFive(1, 90)) # -> 72
print(csAnythingButFive(-4, 17)) # -> 20

"""

def csAnythingButFive(start, end):
    #  Making list from range of start to end 
    array1 = list(range(start, end + 1))
    #  Create empty array to hold stuff
    array2 = []
    #  Loop through each item in array1
    for item in array1:
        #  Convert all item in array1 to strings (not intergers anymore) & putting them into array2
        array2.append(str(item))   
    i = 0
    # if i less than 5
    while i < 5:
        # continue to add 1
        i += 1 
        for item in array2:
            #  if item contains element of 5 greater than 0 times 
            if item.count("5") > 0:
            # i want the index of said item that match 5 in array 3
                array3 = array2.index(item)
                #  remove those indexs from array2
                array2.pop(array3)
    # check the len of array2
    end = len(array2)
    return end

print(csAnythingButFive(1, 9)) # -> 8
print(csAnythingButFive(4, 17)) # -> 12
print(csAnythingButFive(1, 90)) # -> 72
print(csAnythingButFive(-4, 17)) # -> 20