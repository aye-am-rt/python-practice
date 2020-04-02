# Maximum sum bitonic subarray
# Given an array containing n numbers. The problem is to find the maximum sum bitonic subarray.
# A bitonic subarray is a subarray in which elements are first increasing and then decreasing.
# A strictly increasing or strictly decreasing subarray is also considered as bitonic subarray.
# Time Complexity of O(n) is required.
"""
Approach: The problem is closely related to Maximum Sum Bitonic Subsequence. We create two arrays
 msis[] and msds[]. msis[i] stores the sum of Increasing subarray ending with arr[i]. msds[i]
 stores the sum of Decreasing subarray starting from arr[i]. Now, maximum sum bitonic subarray
 is calculated as max(msis[i]+msds[i]-arr[i]) for each index i of the array."""


def maxSumBitonicSubArrON(array, ln):
    if ln < 2:
        return
    incPart = [array[0]] + [0] * (ln - 1)
    decPart = [0] * (ln - 1) + [array[ln - 1]]
    maxSumPossible = float('-inf')
    for i in range(1, ln):
        if array[i] > array[i - 1]:
            incPart[i] = incPart[i - 1] + array[i]
        else:
            incPart[i] = array[i]
    for i in range(ln - 2, -1, -1):
        if array[i + 1] < array[i]:
            decPart[i] = decPart[i + 1] + array[i]
        else:
            decPart[i] = array[i]
    for i in range(ln):
        if maxSumPossible < (incPart[i] + decPart[i] - array[i]):
            maxSumPossible = (incPart[i] + decPart[i] - array[i])
    return maxSumPossible


if __name__ == '__main__':
    # The example from the article, the
    # answer is 19.
    arr = [5, 3, 9, 2, 7, 6, 4]
    n = len(arr)
    print("Maximum Sum = ", maxSumBitonicSubArrON(arr, n))

    # Always increasing, the answer is 15.
    arr2 = [1, 2, 3, 4, 5]
    n2 = len(arr2)
    print("Maximum Sum = ", maxSumBitonicSubArrON(arr2, n2))

    # Always decreasing, the answer is 15.
    arr3 = [5, 4, 3, 2, 1]
    n3 = len(arr3)
    print("Maximum Sum = ", maxSumBitonicSubArrON(arr3, n3))

    # All are equal, the answer is 5.
    arr4 = [5, 5, 5, 5]
    n4 = len(arr4)
    print("Maximum Sum = ", maxSumBitonicSubArrON(arr4, n4))

    # The whole array is bitonic,
    # but the answer is 7.
    arr5 = [-1, 0, 1, 2, 3, 1, 0, -1, -10]
    n5 = len(arr5)
    print("Maximum Sum = ", maxSumBitonicSubArrON(arr5, n5))

    # The answer is 4 (the tail).
    arr6 = [-1, 0, 1, 2, 0, -1, -2, 0, 1, 3]
    n6 = len(arr6)
    print("Maximum Sum = ", maxSumBitonicSubArrON(arr6, n6))
