'''
Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.

Expected Output:
----------------
print(csShortestWord("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live")) -> 1
print(csShortestWord("not great programmer; just good programmer with great habits.")) -> 3
print(csShortestWord("Truth can only be found in one place: the code")) -> 2
print(csShortestWord("Give man program frustrate him for day Teach man program frustrate him for lifetime")) -> 3

'''

def csShortestWord(input_str):

    # split individual words into the array
    split_list = input_str.split()
    # selecting the first word
    wordWanted = split_list[0]
    #  finding its len
    short_length = len(wordWanted)
    # going over every word
    for word in split_list:
        # if the length of each word is greater than the selected word being checked against it
        if short_length > len(word):
            #  change the short_length to the length of most current word in the list
            short_length = len(word)
            #   update my wordWanted to smallest word 
            wordWanted = word
    return len(wordWanted)

print(csShortestWord("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"))
print(csShortestWord("not great programmer; just good programmer with great habits."))
print(csShortestWord("Truth can only be found in one place: the code"))
print(csShortestWord("Give man program frustrate him for day Teach man program frustrate him for lifetime"))


