# perm_identity
# Longest substring of vowels
# Given a string s of lowercase letters, we need to find the longest substring length that
# contain (a, e, i, o, u) only.
#
# Examples :-
#
# Input : s = "geeksforgeeks"
# Output : 2
# Longest substring is "ee"
#
# Input : s = "theeare"
# Output : 3
# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# The idea is to traverse the string and keep track of current number of vowels in the string.
# If we see a character that is not vowel, we reset count to 0. But before resetting we update
# max count value which is going to be our result.


def isVowel(x):
    # Returns true if x is vowel
    x = str(x).lower()
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'


def longestVowelSubString(s):
    if len(s) < 1:
        return
    resStr = currStr = ""
    for i in range(len(s)):
        if isVowel(s[i]):
            currStr += s[i]

        elif len(currStr) > len(resStr):
            resStr = currStr
        else:
            currStr = ""

    if len(resStr) == 0:
        print("no vowels present")
    else:
        print("Longest SubString of vowels= ", resStr)


if __name__ == '__main__':
    st = "geeksforgeeks"
    longestVowelSubString(st)
