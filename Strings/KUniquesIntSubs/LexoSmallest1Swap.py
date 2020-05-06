# Find lexicographically smallest string in at most one swaps
# Given a string str of length N. The task is to find out the lexicographically smallest
# string when at most only one swap is allowed. That is, two indices 1 <= i, j <= n can be
# chosen and swapped. This operation can be performed at most one time.
#
# Examples:
#
# Input: str = “string”
# Output: gtrins
# Explanation:
# Choose i=1, j=6, string becomes – gtrins. This is lexicographically smallest strings that
# can be formed.
"""
Approach: The idea is to use sorting and compute the smallest lexicographical string possible
for the given string. After computing the sorted string, find the first unmatched character
from the given string and replace it with the last occurrence of the unmatched character in the
 sorted string.

For example, let str = “geeks” and the sorted = “eegks”. First unmatched character is in the
first place. This character has to swapped such that this character matches the character with
sorted string. Resulting lexicographical smallest string. On replacing “g” with the last
occurring “e”, the string becomes eegks which is lexicographically smallest."""


def findLexicoSmallest1Swap(strAsList):
    if len(strAsList) < 1:
        print(" size small ")
        return -1

    # print(list(zip(strAsList, sorted(strAsList))))
    i = 0
    while sorted(strAsList)[i] == strAsList[i] and i < len(strAsList):
        i += 1
    firstMisMatchIndex = i
    firstMisMatchChar = sorted(strAsList)[i]
    lastMisMatchIndex = i
    i += 1
    while i < len(strAsList):
        if strAsList[i] == firstMisMatchChar:
            lastMisMatchIndex = i
        i += 1
    print(f"{firstMisMatchIndex}, {firstMisMatchChar}, {lastMisMatchIndex}")

    strAsList[firstMisMatchIndex], strAsList[lastMisMatchIndex] = \
        strAsList[lastMisMatchIndex], strAsList[firstMisMatchIndex]
    # print(strAsList)
    return "".join(strAsList)


if __name__ == "__main__":
    s = "geeks"
    print(findLexicoSmallest1Swap(list(s)))
