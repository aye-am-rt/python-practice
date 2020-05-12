"""Maximum length sub-array which satisfies the given conditions
Given an array arr[] of N integers, the task is to find the maximum length of any sub-array of
arr[] which satisfies one of the given conditions:

The sub array is strictly increasing.
The sub array is strictly decreasing.
The sub array is first strictly incresing then strictly decreasing.
Examples:

Input: arr[] = {1, 2, 2, 1, 3}
Output: 2
{1, 2}, {2, 1} and {1, 3} are the valid sub arrays.



Input: arr[] = {5, 4, 3, 2, 1, 2, 3, 4}
Output: 5
{5, 4, 3, 2, 1} is the required sub array.

Approach: Create an array incEnding[] where incEnding[i] will store the length of the largest
increasing sub array of the given array ending at index i. Similarly, create another array
decStarting[] where decStarting[i] will store the length of the largest decreasing sub array of
the given array starting at the index i. Now start traversing the original array and for every
element, assume it to be the mid of the required sub array then the length of the largest required
sub array whose mid at index i will be incEnding[i] + decStarting[i] – 1. Note that 1 is subtracted
 because arr[i] will be counted twice for both the increasing and the decreasing sub array."""

# Driver code
arr = [1, 2, 2, 1, 3]
n = len(arr)


def largestSubArrIncORDec(ary, ln):
    if ln == 0 or ln == 1:
        return -1
    if ln == 2 and ary[0] != ary[1]:
        return ary
    incIEnding = [0] * n
    incIEnding[0] = 1
    for i in range(1, n):
        if ary[i] > ary[i - 1]:
            incIEnding[i] = incIEnding[i - 1] + 1
        else:
            incIEnding[i] = 1
    decIStarting = [0] * (n - 1) + [1]
    for i in range(n - 2, -1, -1):
        if ary[i + 1] < ary[i]:
            decIStarting[i] = decIStarting[i + 1] + 1
        else:
            decIStarting[i] = 1
    maxSubArrLen = 0

    for i in range(ln):
        if decIStarting[i] + incIEnding[i] - 1 > maxSubArrLen:
            maxSubArrLen = decIStarting[i] + incIEnding[i] - 1
    return maxSubArrLen


print(largestSubArrIncORDec(arr, n))
