# perm_identity
# Find the minimum of maximum length of a jump required to reach the last island in exactly
# k jumps
# Given an array arr[] of integers, where the ith integer represents the position where an
# island is present, and an integer k (1 ≤ k < N). A person is standing on the 0th island
# and has to reach the last island, by jumping from one island to another in exactly k jumps,
# the task is to find the minimum of the maximum length of a jump a person will make in his
# journey. Note that the position of all the islands are given in ascending order.
#
# Examples:
#
# Input: arr[] = {2, 15, 36, 43}, k = 1
# Output: 41
# There is only way to reach the end
# 2 -> 43
# Input: arr[] = {2, 15, 36, 43}, k = 2
# Output: 28
# There are two ways to reach the last island
# 2 -> 15 -> 43
# Here maximum distance between any two consecutive islands is between 43 and 15 that is 28.
# 2 -> 36 -> 43
# Here maximum distance between any two consecutive islands is between 36 and 2 that is 34.
# Thus minimum of 28 and 34 is 28.
"""
Approach: The idea is to use binary search, and for a distance mid, compute whether it is
possible to reach the end of the array in exactly k jumps where the maximum distance between
any two islands chosen for jumping is less than or equal to the distance mid, then check if
some distance less than mid exists for which it is possible to reach the end in exactly
k jumps."""


# Returns the minimum maximum distance required
# to reach the end of the array in exactly k jumps
def isPossibleKJump(ary, ln, dist, K):
    req = curr = prev = 0
    for i in range(ln):
        while curr != ln and (ary[curr] - ary[prev] <= dist):
            curr += 1
        req += 1

        if curr == ln:
            break
        prev = curr - 1
    if curr != ln:
        return False
    if req <= K:
        return True
    return False


def minDistanceKJumps(ary, ln, K):
    left = 0
    right = ary[ln - 1]
    ansJumps = 0
    while left <= right:
        m = (left + right) // 2
        if isPossibleKJump(ary, ln, m, K):
            ansJumps = m
            right = m - 1
        else:
            left = m + 1
    return ansJumps


if __name__ == '__main__':
    arr = [2, 15, 36, 43]
    n = len(arr)
    k = 2

    print(minDistanceKJumps(arr, n, k))
