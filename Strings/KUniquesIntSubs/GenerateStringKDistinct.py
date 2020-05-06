# Generate a string of size N whose each substring of size M has exactly K distinct characters
# Given 3 positive integers N, M and K. the task is to construct a string of length N
# consisting of lowercase letters such that each substring of length M having exactly K
# distinct letters.
# Examples:
# Input: N = 5, M = 2, K = 2
# Output: abade
# Explanation:
# Each substring of size 2 “ab”, “ba”, “ad”, “de” have 2 distinct letters.

# Input: N = 7, M = 5, K = 3
# Output: abcaaab
# Explanation:
# Each substring of size 5 “tleel”, “leelt”, “eelte” have 3 distinct letters.
#
# Approach: In a string of size N, every substring of size M must contain exactly K distinct
# letters
#
# Construct a string having K distinct alphabets starting from ‘a’ to ‘z’ up to the size of M
# and put the rest of letters like ‘a’..
# Since, we have generated a string of size M with K distinct value. Now, keep repeating it
# till we reach string size of N.


def GenerateString(totalLength, SubSSizeM, DLettersK):
    ansString = ""
    cntM = cntK = 0  # counter for M and K
    for i in range(totalLength):  # Loop to generate string size of N
        cntK += 1  # K is num of distinct letters in each substring
        cntM += 1  # M is substring size
        if cntM <= SubSSizeM:  # Generating K distinct letters one by one
            if cntK <= DLettersK:
                ansString += chr(96 + cntM)
            else:
                ansString += 'a'
        else:  # Reset the counter value and repeat the process
            cntK = cntM = 1
            ansString += 'a'
    print(ansString)


if __name__ == '__main__':
    N = 7
    M = 5
    K = 3
    GenerateString(N, M, K)
