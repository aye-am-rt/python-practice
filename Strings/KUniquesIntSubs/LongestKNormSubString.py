# Find length of longest substring with at most K normal characters
# Given a string P consisting of small English letters and a 26-digit bit string Q, where 1
# represent special character and 0 represent normal character for the 26 English alphabets.
# The task is to find the length of longest substring with at most K normal characters.
#
# Examples:
#
# Input : P = “normal”, Q = “00000000000000000000000000”, K=1
# Output : 1
# Explanation : In string Q all characters are normal.
# Hence we can select any substring of length 1.
#
# Input : P = “giraffe”, Q = “01111001111111111011111111”, K=2
# Output : 3
# Explanation : Normal characters in P from Q are {a, f, g, r}.
# Therefore, possible substrings with at most 2 normal characters are {gir, ira, ffe}.
# The maximum length of all substring is 3.

# Approach:
#
# To solve the problem mentioned above we will be using the concept of two pointers. Hence, maintain
# left and right pointers of the substring, and a count of normal characters. Increment right index
# till the count of normal characters is at most K. Then update the answer with a maximum length of
# substring encountered till now. Increment left index and decrement count till is it greater
# than K.


def maxNormal_K_Chars_Substring(st, alphaCodes, kMax, ln):
    if kMax == 0:
        return 0

    countNorms = 0
    left, right = 0, 0
    length_Of_Longest_With_K = 0
    while right < ln:
        while right < ln and countNorms <= kMax:
            pos = ord(st[right]) - ord('a')  # get position of character

            if alphaCodes[pos] == '0':
                if countNorms + 1 > kMax:  # check if normal characters count exceeds K
                    break
                else:
                    countNorms += 1
            right += 1
            # update answer with substring length
            if countNorms <= kMax:
                length_Of_Longest_With_K = max(length_Of_Longest_With_K, (right - left))

        while left < right:
            # get position of character
            pos = ord(st[left]) - ord('a')
            left += 1
            # check if character is normal then decrement count
            if alphaCodes[pos] == '0':
                countNorms -= 1

            if countNorms < kMax:
                break

    return length_Of_Longest_With_K


if __name__ == "__main__":
    P = "giraffe"
    Q = "01111001111111111011111111"
    K = 2
    N = len(P)

    print(maxNormal_K_Chars_Substring(P, Q, K, N))
