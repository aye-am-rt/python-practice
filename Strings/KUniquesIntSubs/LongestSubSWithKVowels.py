"""Efficient Approach : Here we maintain the count of vowels occurring in the substring.
Till K is not zero, we count the distinct vowel occurring in the substring.
As K becomes negative, we start deleting the first vowel of the substring we have found till
 that time, so that it may be possible that new substring( larger length ) is
 possible afterward. As we delete the vowel we decrease its count so that new substring may
 contain that vowel occurring in the later part of the string. And as K is 0 we get the
 length of the substring."""


# Python3 program to find the longest substring
# with k distinct vowels.

MAX = 128


# Function to check whether a character is
# vowel or not
def isVowel(x):
    return (x == 'a' or x == 'e' or x == 'i' or
            x == 'o' or x == 'u' or x == 'A' or
            x == 'E' or x == 'I' or x == 'O' or
            x == 'U')


def KDistinctVowel(c, k):
    n = len(s)

    c = [0 for i in range(MAX)]
    result = -1

    j = -1

    for i in range(n):
        x = s[i]

        # If letter is vowel then we
        # increment its count value
        # and decrease the k value so
        # that if we again encounter the
        # same vowel character then we
        # don't consider it for our result

        if isVowel(x):
            c[ord(x)] += 1
            if c[ord(x)] == 1:
                k -= 1

        # Till k is 0 above if condition run
        # after that this while loop condition
        # also become active. Here what we have
        # done actually is that, if K is less
        # than 0 then we eliminate the first
        # vowel we have encountered till that
        # time . Now K is incremented and k
        # becomes 0. So, now we calculate the
        # length of substring from the present
        # index to the deleted index of vowel
        # which result in our results.
        while k < 0:
            j += 1
            x = s[j]
            if isVowel(x):
                # decreasing the count
                # so that it may appear
                # in another substring
                # appearing after this
                # present substring
                c[ord(x)] -= 1
                k += 1

        # Checking the maximum value
        # of the result by comparing
        # the length of substring
        # whenever K value is 0 means
        # K distinct vowel is present
        # in substring

        if k == 0:
            result = max(result, i - j)

    return result


s = "tHeracEBetwEEntheTwo"
k = 1
print(KDistinctVowel(s, k))
