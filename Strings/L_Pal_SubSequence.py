"""
We have discussed a Dynamic Programming solution for Longest Palindromic Subsequence which is based on
 below recursive formula.

// Every single character is a palindrome of length 1
L(i, i) = 1 for all indexes i in given sequence

// IF first and last characters are not same
If (X[i] != X[j]) L(i, j) = max{L(i + 1, j), L(i, j – 1)}

// If there are only 2 characters and both are same
Else if (j == i + 1) L(i, j) = 2

// If there are more than two characters, and first
// and last characters are same
Else L(i, j) = L(i + 1, j – 1) + 2

The solution discussed above takes O(n2) extra space. In this post a space optimized solution is discussed
that requires O(n) extra space. The idea is to create a one dimensional array a[] of same size as given
string.
We make sure that a[i] stores length of longest palindromic subsequence of prefix ending with i
(or substrings[0..i])."""


# Returns the length of the longest
# palindromic subsequence in str
def lps(s):
    n = len(s)

    # a[i] is going to store length of longest palindromic subsequence of substring s[0..i]
    a = [0] * n

    # Pick starting point
    for i in range(n - 1, -1, -1):

        back_up = 0

        # Pick ending points and see if s[i] increases length of longest common
        # subsequence ending with s[j].
        for j in range(i, n):

            # similar to 2D array L[i][j] == 1
            # i.e., handling substrings of length
            # one.
            if j == i:
                a[j] = 1

            # Similar to 2D array L[i][j] = L[i+1][j-1]+2
            # i.e., handling case when corner characters are same.
            elif s[i] == s[j]:
                temp = a[j]
                a[j] = back_up + 2
                back_up = temp

            # similar to 2D array L[i][j] = max(L[i][j-1], a[i+1][j])
            else:
                back_up = a[j]
                a[j] = max(a[j - 1], a[j])

    return a[n - 1]


string = "GEEKSFORGEEKS"
print(lps(string))
