# Count ways to partition a string such that both parts have equal distinct characters
# Given a string S, the task is to count the number of ways to partition the string
# into two non-empty parts such that both the parts have the same number of distinct characters.
#
# Examples:
#
# Input: S = “aaaa”
# Output: 3
# Explanation:
# There can be three ways to partition the string –
# {{a, aaa}, {aa, aa}, {aaa, a}}

"""
Naive Approach: The idea is to choose the every possible partition point of the string and for
each partition compute the distinct characters in the partitioned string. If the count of distinct
characters in both the partitioned string is equal then increment the number of ways by 1.

# Function to count the distinct
# characters in the string

def distinctChars(s) :

    # Frequency of each character
    freq = [0]*26;
    count = 0;

    # Loop to count the frequency
    # of each character of the string

    # // Loop to count the frequency    ====== this is for java
    # // of each character of the String

    # for (int i = 0; i < s.length(); i++)
    #     freq[s.charAt(i) - 'a']++;

    for i in range(len(s)) :
        freq[ord(s[i]) - ord('a')] += 1;

        # If frequency is greater than 0
    # then the character occured
    for i in range(26) :
        if (freq[i] > 0) :
            count += 1;

    return count;

# Function to count the number
# of ways to partition the string
# such that each partition have
# same number of distinct character
def waysToSplit(s) :
    n = len(s);
    answer = 0;

    # Loop to choose the partition
    # index for the string
    for i in range(1, n) :

        # Divide in two parts
        left = s[0 : i];
        right = s[i : n ];

        # Check whether number of distinct
        # characters are equal
        if (distinctChars(left) == distinctChars(right)) :
            answer += 1;

    return answer;

# Driver Code
if __name__ == "__main__" :

    s = "ababa";

    print(waysToSplit(s));

"""
"""
Efficient Approach: The idea is to precompute the distinct character for every possible substring with the help
 of hash-map for visited characters and Prefix and suffix sum arrays for the distinct characters from start to
  current index of the string. Below is the illustration of the steps:

Traverse the string for each possible indices and compute the count of distinct characters from start to that
index.
If the current index character is visited for the first time, then increment the count of the distinct
characters from the previous index by 1.
if (visited[s[i]] == False)
    prefix[i] = prefix[i-1] + 1
If the current index character is visited earlier, then count of distinct characters from starting index to current
index will be equal to last index distinct characters. That is –
if (visited[s[i]] == True)
    prefix[i] = prefix[i-1]
Finally, Traverse the string and for each index count of distinct characters for each partitioned string
 can be calculated as –
Count in left partitioned string
= prefix[i]

Count in right partitioned string
= prefix[L] - prefix[i+1]
"""
# Function to count the number
# of ways to partition the string
# such that each partition have
# same number of distinct character


def waysToSplit(s):
    n = len(s)
    answer = 0

    # Prefix and suffix array for
    # distinct character from
    # start and end
    prefix = [0] * n
    suffix = [0] * n

    # To check whether a character
    # has appeared till ith index
    seen = [0] * 26

    # Calculating prefix array
    for i in range(n):

        prev = prefix[i - 1] if (i - 1 >= 0) else 0

        # Character appears for
        # the first time in string
        if seen[ord(s[i]) - ord('a')] == 0:
            prefix[i] += (prev + 1)

        else:
            prefix[i] = prev

            # Character is visited
        seen[ord(s[i]) - ord('a')] = 1

        # Resetting seen for
    # suffix calculation
    seen = [0] * len(seen)

    # Calculating the suffix array
    suffix[n - 1] = 0
    for i in range(n - 1, 0, -1):
        prev = suffix[i]

        # Character appears
        # for the first time
        if seen[ord(s[i]) - ord('a')] == 0:
            suffix[i - 1] += (prev + 1)

        else:
            suffix[i - 1] = prev

            # This character
        # has now appeared
        seen[ord(s[i]) - ord('a')] = 1

        # Loop to calculate the number
    # partition points in the string
    for i in range(n):
        # Check whether number of
        # distinct characters are equal
        if prefix[i] == suffix[i]:
            answer += 1

    return answer


# Driver Code
if __name__ == "__main__":
    s = "ababa"

    print(waysToSplit(s))
