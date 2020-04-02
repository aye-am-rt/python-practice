# Maximum Length Bitonic Subarray | Set 2 (O(n) time and O(1) Space)
# Given an array A[0 … n-1] containing n positive integers, a subarray A[i … j] is bitonic if
# there is a k with i <= k <= j such that A[i] = .. A[j – 1] > = A[j]. Write a function that takes
# an array as argument and returns the length of the maximum length bitonic subarray.

"""The idea is to check longest bi-tonic sub array starting at A[i]. From A[i], first we will check
 for end of ascent and then end of descent.Overlapping of bi-tonic sub arrays is taken into account
 by recording a nextStart position when it finds two equal values when going down the slope of
 the current sub array. If length of this sub array is greater than max_len, we will update max_len.
 We continue this process till end of array is reached"""


def MaxBitonicLength(array, ln):
    if ln < 2:
        return 0
    maxLenFound = 1
    start = 0
    nextStart = 0
    j = 0
    while j < ln - 1:
        while j < ln - 1 and array[j + 1] >= array[j]:
            j += 1
        while j < ln - 1 and array[j + 1] <= array[j]:
            # if j < n - 1 and A[j] > A[j + 1]:
            nextStart = j + 1
            j += 1
        maxLenFound = max(maxLenFound, j - start + 1)
        start = nextStart
    return maxLenFound


if __name__ == '__main__':
    A = [1, 2, 30, 14, 5, 7, 10, 14, 13, 12, 11, 10, 9, 8, 7, 14, 67, 78]
    # ans is from 5,7,10.....9,8,7  ===> 11 elements
    n = len(A)
    print("Length of max length Bi-tonic Sub array is", MaxBitonicLength(A, n))
