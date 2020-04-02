# Sliding Window Maximum (Maximum of all subarrays of size k)
# Given an array and an integer K, find the maximum for each and every contiguous sub-array of size k.
# Examples :
#
# Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
# Output: 3 3 4 5 5 5 6


# Method to find the maximum for each
# and every contiguous sub-array of s
# of size k
# def printMax(arr, n, k):
#     max = 0
#
#     for i in range(n - k + 1):
#         max = arr[i]
#         for j in range(1, k):
#             if arr[i + j] > max:
#                 max = arr[i + j]
#         print(str(max) + " ", end = "")
#
#     # Driver method
# if __name__=="__main__":
#     arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     n = len(arr)
#     k = 3
#     printMax(arr, n, k)

# Output:
# 3 4 5 6 7 8 9 10
# Time Complexity : The outer loop runs n-k+1 times and the inner loop runs k times for every
# iteration of outer loop. So time complexity is O((n-k+1)*k) which can also be written as O(N * K).

"""
Method 3 (A O(n) method: use Deque) We create a Deque, Qi of capacity k, that stores only useful
elements of current window of k elements. An element is useful if it is in current window and is
greater than all other elements on left side of it in current window. We process all array elements
one by one and maintain Qi to contain useful elements of current window and these useful elements
are maintained in sorted order. The element at front of the Qi is the largest and element at rear
of Qi is the smallest of current window."""

from collections import deque


def printMaxInSubArrays(array, ln, k):
    if ln < k:
        print("no subset")
        return
    qi = deque()

    for i in range(k):
        while qi and array[i] >= array[qi[-1]]:
            qi.pop()
        qi.append(i)

    for i in range(k, ln):
        print(str(arr[qi[0]]) + " ", end=" ")

        while qi and (i - qi[0]) >= k:
            qi.popleft()

        while qi and array[i] >= array[qi[-1]]:
            qi.pop()
        qi.append(i)
    print(str(arr[qi[0]]))


if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMaxInSubArrays(arr, len(arr), k)
