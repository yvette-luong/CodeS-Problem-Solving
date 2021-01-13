'''
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string

Expected Output:
---------------
print(csRemoveTheVowels("Lambda School is awesome"))
-> Lmbd Schl s wsm

print(csRemoveTheVowels("Talk is cheap. Show me the code."))
-> Tlk s chp. Shw m th cd.

print(csRemoveTheVowels("f!a fbs,rI\\H[P^f}!h;!<\tyu>/`uD^d,xGDWPj{HU$m~$|_e#"))
-> f! fbs,r\H[P^f}!h;!<    y>/`D^d,xGDWPj{H$m~$|_#

print(csRemoveTheVowels("Programs must be written for people to read, and only incidentally for machines to execute."))
-> Prgrms mst b wrttn fr ppl t rd, nd nly ncdntlly fr mchns t xct.

print(csRemoveTheVowels("km%]jf&rSit&*g#M,.hba?}\\k^%tT>E^pdS\\A,*IIZtVhrPGXr"))
-> km%]jf&rSt&*g#M,.hb?}\k^%tT>^pdS\,*ZtVhrPGXr

'''

def csRemoveTheVowels(input_str):
    #  Making the vowels known
    vowels =  ['u','e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I']
    #  Looping over the string, and saying id that letter is not in vowels, then keep that letter 
    newStr = ''.join([l for l in input_str if l not in vowels])
    return newStr

print(csRemoveTheVowels("Lambda School is awesome"))
print(csRemoveTheVowels("Talk is cheap. Show me the code."))
print(csRemoveTheVowels("f!a fbs,rI\\H[P^f}!h;!<\tyu>/`uD^d,xGDWPj{HU$m~$|_e#"))
print(csRemoveTheVowels("Programs must be written for people to read, and only incidentally for machines to execute."))
print(csRemoveTheVowels("km%]jf&rSit&*g#M,.hba?}\\k^%tT>E^pdS\\A,*IIZtVhrPGXr"))



