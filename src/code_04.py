"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:
--------
csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string

Expected Output:
---------------
print(csLongestPossible("aretheyhere", "yestheyarehere")) # -> Expected Output:"aehrsty"
print(csLongestPossible("loopingisfunbutdangerous", "lessdangerousthancoding")) # -> Expected Output: "abcdefghilnoprstu"
print(csLongestPossible("inmanylanguages", "theresapairoffunctions")) # -> "acefghilmnoprstuy"
print(csLongestPossible("etxtxgxqxkrwu", "fvaqjrvnzeyed")) # -> "adefgjknqrtuvwxyz"

"""
def csLongestPossible(str_1, str_2):
    #  This is where duplicate letters go
    duplicates = []
    #  This is where single letters go
    singles = []
    #   Making string into array
    array1 = list(str_1)
    array2 = list(str_2)
    print(array1)
    #  Combine 2 arrays
    combined = array1 + array2
    #  Go over everyletter in the array 
    for letter in combined:
        #  check if not in singles
        if letter not in singles:
            # if not, put letter in singles
            singles.append(letter)
            #  sort singles alphabeticaly
            singles.sort()
        else:
            #  otherwise move letter to duplicate
            duplicates.append(letter)

    return ''.join(singles)

print(csLongestPossible("aretheyhere", "yestheyarehere")) # -> Expected Output:"aehrsty"
print(csLongestPossible("loopingisfunbutdangerous", "lessdangerousthancoding")) # -> Expected Output: "abcdefghilnoprstu"
print(csLongestPossible("inmanylanguages", "theresapairoffunctions")) # -> "acefghilmnoprstuy"
print(csLongestPossible("etxtxgxqxkrwu", "fvaqjrvnzeyed")) # -> "adefgjknqrtuvwxyz"