# Longest Subsequence of a String containing only vowels
# Given a string str containing only alphabets, the task is to print the longest subsequence of
# the string str containing only vowels.
# Examples:
# Input: str = “geeksforgeeks”
# Output: eeoee
# Explanation:
# “eeoee” is the longest subsequence of the string containing only vowels.


def isVowel(x):
    # Returns true if x is vowel
    x = str(x).lower()
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'


def longestVowelSubsequence(s):
    if len(s) < 1:
        return
    resStr = ""
    for i in range(len(s)):
        if isVowel(s[i]):
            resStr += s[i]

    if len(resStr) == 0:
        print("no vowels present")
    else:
        print("Longest SubSequence of vowels= ", resStr)


if __name__ == '__main__':
    st = "geeksforgeeks"
    longestVowelSubsequence(st)
