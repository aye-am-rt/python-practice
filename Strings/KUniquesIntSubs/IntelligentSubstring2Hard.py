# Python program to find the longest substring with k unique
# characters in a given string
MAX_CHARS = 26


# def isValid(count, k):
#     val = 0
#     for i in range(MAX_CHARS):
#         if count[i] > 0:
#             val += 1
#
#     # Return true if k is greater than or equal to val
#     return (k >= val)


def FindLongestSubStringWithAtMostKAlphabets(st, K, alphabets, alphaValues):
    if len(st) == 0 or len(st) < K:
        return
    charMap = {}
    for i in range(len(alphabets)):
        # charMap.update({alphabets[i]: str(values)[i]})
        charMap[alphabets[i]] = int(str(alphaValues)[i])
    print(charMap)

    iniCount = 0
    n = len(st)

    for i in range(n):
        if charMap.get(st[i]) == 0:
            iniCount += 1

    if iniCount < K:
        print("Not enough normal characters")
        return
    # Otherwise take a window with first element in it.
    # start and end variables.
    curr_start = 0
    curr_end = 0
    # Also initialize values for result longest window
    max_window_size = 1
    max_window_start = 0
    countArr = [0 for i in range(MAX_CHARS)]
    countArr[ord(st[0]) - ord('a')] += 1

    for i in range(1, n):
        # Add the character 's[i]' to current window
        countArr[ord(st[i]) - ord('a')] += 1
        curr_end += 1

        # If there are more than k unique characters in
        # current window, remove from left side
        while iniCount > K:
            countArr[ord(st[curr_start]) - ord('a')] -= 1
            curr_start += 1
            iniCount -= 1

        # Update the max window size if required
        if curr_end - curr_start+1 > max_window_size:
            max_window_size = curr_end - curr_start+1
            max_window_start = curr_start

    print("Max substring is : " + st[max_window_start:max_window_start + max_window_size]
          + " with length " + str(max_window_size))


if __name__ == '__main__':
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    charValue = 10101111111111111111111111

    s = 'abcde'
    k = 1
    FindLongestSubStringWithAtMostKAlphabets(s, k, alphabet, charValue)
