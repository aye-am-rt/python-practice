# Maximum sum bitonic subarray
# Given an array containing n numbers. The problem is to find the maximum sum bitonic subarray.
# A bitonic subarray is a subarray in which elements are first increasing and then decreasing.
# A strictly increasing or strictly decreasing subarray is also considered as bitonic subarray.
# Time Complexity of O(n) is required.
#
# Examples:
#
# Input : arr[] = {5, 3, 9, 2, 7, 6, 4}
# Output : 19
# The subarray is {2, 7, 6, 4}.
#
# Input : arr[] = {9, 12, 14, 8, 6, 5, 10, 20}
# Output : 54


def maxSumBitonicSubArr(array, ln):
    if ln < 2:
        return 0
    maxSumPossible = float('-inf')
    i = 0
    while i < ln - 1:
        j = i
        while j < ln - 1 and array[j + 1] > array[j]:
            j += 1
        while i < j and array[i] <= 0:
            i += 1
        k = j
        while k < ln - 1 and array[k + 1] < array[k]:
            k += 1
        last = k
        while j < k and array[k] <= 0:
            k -= 1
        incPart = array[i:j + 1]
        sumInc = sum(incPart)
        decPart = array[j:k + 1]
        sumDec = sum(decPart)
        sumAll = sumInc + sumDec - array[j]
        maxSumPossible = max(maxSumPossible, sumInc, sumDec, sumAll)
        i = max(last, i + 1)
    return maxSumPossible


if __name__ == '__main__':
    # The example from the article, the
    # answer is 19.
    arr = [5, 3, 9, 2, 7, 6, 4]
    n = len(arr)
    print("Maximum Sum = ", maxSumBitonicSubArr(arr, n))

    # Always increasing, the answer is 15.
    arr2 = [1, 2, 3, 4, 5]
    n2 = len(arr2)
    print("Maximum Sum = ", maxSumBitonicSubArr(arr2, n2))

    # Always decreasing, the answer is 15.
    arr3 = [5, 4, 3, 2, 1]
    n3 = len(arr3)
    print("Maximum Sum = ", maxSumBitonicSubArr(arr3, n3))

    # All are equal, the answer is 5.
    arr4 = [5, 5, 5, 5]
    n4 = len(arr4)
    print("Maximum Sum = ", maxSumBitonicSubArr(arr4, n4))

    # The whole array is bitonic,
    # but the answer is 7.
    arr5 = [-1, 0, 1, 2, 3, 1, 0, -1, -10]
    n5 = len(arr5)
    print("Maximum Sum = ", maxSumBitonicSubArr(arr5, n5))

    # The answer is 4 (the tail).
    arr6 = [-1, 0, 1, 2, 0, -1, -2, 0, 1, 3]
    n6 = len(arr6)
    print("Maximum Sum = ", maxSumBitonicSubArr(arr6, n6))
