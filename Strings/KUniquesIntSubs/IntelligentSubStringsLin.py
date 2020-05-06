"""Intelligent Substrings:

There are two types of characters in a particular language: special and normal. A character is
special if its value is 1 and normal if its value is 0. Given string s, return the longest
substring of s that contains at most k normal characters. Whether a character is normal is
determined by a 26-digit bit string named charValue. Each digit in charValue corresponds to a
lowercase letter in the English alphabet.
Example:

s = 'abcde'
For clarity, the alphabet is aligned with charValue below:

alphabet =  abcdefghijklmnopqrstuvwxyz
charValue = 10101111111111111111111111

The only normal characters in the language (according to charValue) are b and d. The string s
 contains both of these characters. For k = 2, the longest substring of s that contains at
 most k = 2 normal characters is 5 characters long, abcde, so the return value is 5. If k = 1
 instead, then the possible substrings are ['b', 'd', 'ab', 'bc', 'cd', 'de', 'abc', 'cde'].
 The longest substrings are 3 characters long, which would mean a return value of 3."""


def FindLongestIntelligentSubStringWithKAlphabets(st, K, alphas, values):
    if len(st) == 0 or len(st) < K:
        return
    charMap = {}
    for i in range(len(alphas)):
        # charMap.update({alphas[i]: str(values)[i]})
        charMap[alphas[i]] = int(str(values)[i])
    print(charMap)
    normalCount = 0
    l = 0
    r = len(st) - 1
    while l <= r:
        if charMap.get(st[l]) == 0:
            normalCount += 1
        if charMap.get(st[r]) == 0:
            normalCount += 1
        l += 1
        r -= 1
    if len(st) % 2 != 0 and st[len(st) // 2] == 0:
        normalCount -= 1
    print("initial normal characters count in string= ", normalCount)
    if normalCount == K:
        print("Longest Intelligent Sub String With K normal Alphabets = ", st)
        # return
    elif normalCount < K:
        print(" not possible ")
        # return
    else:
        n = len(st)
        ansString = st
        c = [0 for i in range(128)]
        result = j = -1
        for i in range(n):
            x = st[i]
            if charMap.get(x) == 0:
                c[ord(x)] += 1
                if c[ord(x)] == 1:
                    K -= 1
            while K < 0:
                j += 1
                x = st[j]
                if charMap.get(x) == 0:
                    c[ord(x)] -= 1
                    K += 1
            if K == 0:
                result = max(result, i - j)
                ansString = st[j:i]
        print(f"final length result = {result} and String = {ansString}")


if __name__ == '__main__':
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    charValue = 10101111111111111111111111

    s = 'abcde'
    k = 1
    FindLongestIntelligentSubStringWithKAlphabets(s, k, alphabet, charValue)
