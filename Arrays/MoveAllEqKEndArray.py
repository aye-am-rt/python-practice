# Move all values equal to K to the end of the Array
# Given an array arr[] of size N and an integer K, the task is to print the array after moving
# all value equal to K at the end of the array.
#
# Examples:
#
# Input: arr = [2, 1, 2, 2, 2, 3, 4, 2], K = 2
# Output: [4, 1, 3, 2, 2, 2, 2, 2]
# Explanation:
# 2 is the number which has to be moved to the end of the array arr[]. Therefore, after making the
# change the array is [4, 1, 3, 2, 2, 2, 2, 2]. The numbers 4, 1, and 3 could be
# ordered differently.
"""
Approach: To solve the problem mentioned above we use Two Pointer Technique.

Initialize two pointers where the left pointer marks the start of the array and the other one
that is right one marks the end of the array, respectively.
Decrement the count of right pointer long as it points to K, and increment the left pointer as
long as it doesn’t point to the any other integer m.
When both pointers aren’t moving, swap their values in place.
Repeat this process until the pointers pass each other."""


def moveElementEqualKToEnd(ary, k):
    left = 0
    right = len(ary) - 1
    while left < right:
        while left < right and ary[right] == k:
            right -= 1
        while left < right and ary[left] != k:
            left += 1
        if left < right:
            ary[left], ary[right] = ary[right], ary[left]
            left += 1
            right -= 1

    return ary


if __name__ == "__main__":

    arr = [1, 1, 3, 1, 1, 5, 6, 1, 1, 7, 3, 23, 65, 1]
    K = 1
    ans = moveElementEqualKToEnd(arr, K)
    for i in range(len(arr)):
        print(ans[i], end=" ")
