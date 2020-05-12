# Maximum length of a sub-array with ugly numbers
# Given an array arr[] of N elements (0 ≤ arr[i] ≤ 1000). The task is to find the maximum length of
# the sub-array that contains only ugly numbers. Ugly numbers are numbers whose only prime factors
# are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ….. shows first few ugly numbers. By convention,
# 1 is included.
#
# Examples:
#
# Input: arr[] = {1, 2, 7, 9, 120, 810, 374}
# Output: 3
# Longest possible sub-array of ugly number sis {9, 120, 810}
"""Approach:
Take a unordered_set, and insert all the ugly numbers which are less than 1000 in the set.
Traverse the array with two variables named current_max and max_so_far.
Check for each element if it is present in the set.
If an ugly number is found then increment current_max and compare it with max_so_far.
    If current_max > max_so_far then max_so_far = current_max.
Every time a non ugly element is found, reset current_max = 0."""


# Function to get the nth ugly number
def uglyNumber(nth):
    uglyNums = [0] * nth   # [0 for i in range(nth)]
    uglyNums[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    next_ugly_no = 1
    for i in range(1, nth):
        next_ugly_no = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        uglyNums[i] = next_ugly_no

        if next_ugly_no == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = uglyNums[i2] * 2

        if next_ugly_no == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = uglyNums[i3] * 3

        if next_ugly_no == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = uglyNums[i5] * 5

    return next_ugly_no


def maxUglySubArray(arr, ln):
    s = set()
    i = 1
    while 1:
        next_ugly_num = uglyNumber(i)
        if next_ugly_num >= 1000:
            break
        s.add(next_ugly_num)
        i += 1

    currentMax = maxSoFar = 0
    for i in range(ln):
        if arr[i] not in s:
            currentMax = 0
        else:
            currentMax += 1
            maxSoFar = max(maxSoFar, currentMax)

    return maxSoFar


if __name__ == '__main__':
    a = [1, 0, 6, 7, 320, 800, 100, 648]
    n = len(a)
    print(maxUglySubArray(a, n))
