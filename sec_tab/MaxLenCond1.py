"""Maximum length sub-array which satisfies the given conditions
Given a binary array arr[], the task is to find the length of the longest sub-array of the given
 array such that if the sub-array is divided into two equal-sized sub-arrays then both the sub-arrays
 either contain all 0s or all 1s. For example, the two sub-arrays must be of the form {0, 0, 0, 0}
and {1, 1, 1, 1} or {1, 1, 1} and {0, 0, 0} and not {0, 0, 0} and {0, 0, 0

Examples:

Input: arr[] = {1, 1, 1, 0, 0, 1, 1}
Output: 4
{1, 1, 0, 0} and {0, 0, 1, 1} are the maximum length valid sub-arrays.

Input: arr[] = {1, 1, 0, 0, 0, 1, 1, 1, 1}
Output: 6
{0, 0, 0, 1, 1, 1} is the only valid sub-array with maximum length
"""


def LongestSubArrToDivide(array, ln):
    if ln < 2:
        return -1
    if ln == 2:
        return array
    maxSameLen = 0
    currLen = 1
    subArrLen = 0
    # [1, 1, 1, 0, 0, 1, 1]
    for i in range(1, ln):
        if array[i] == array[i - 1]:
            currLen += 1
        else:
            maxSameLen = currLen
            currLen = 1
        subArrLen = max(subArrLen, min(maxSameLen, currLen))
    return subArrLen * 2


if __name__ == '__main__':
    arr = [1, 0, 1, 1, 1]
    print(LongestSubArrToDivide(arr, arr.__len__()))
