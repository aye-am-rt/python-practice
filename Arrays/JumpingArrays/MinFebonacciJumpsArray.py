# Minimum number of Fibonacci jumps to reach end
# Given an array of 0s and 1s, If any particular index i has value 1 then it is a safe index
# and if the value is 0 then it is an unsafe index. A man is standing at index -1(source)
# can only land on a safe index and he has to reach the Nth index (last position). At each
# jump, the man can only travel a distance equal to any Fibonacci Number. You have to
# minimize the number of steps, provided man can jump only in forward direction.
#
# Note: First few Fibonacci numbers are – 0, 1, 1, 2, 3, 5, 8, 13, 21….
#
# Examples:
#
# Input: arr[]= {0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0}
# Output: 3
#
# The person will jump from:
# 1) index -1 to index 4 (a distance of jump = 5)
# 2) index 4 to index 6 (a distance of jump = 2)
# 3) index 6 to the destination (a distance of jump = 5)
#
# Input: arr[]= {0, 0}
# Output: 1
#
# The person will jump from:
# 1) index -1 to destination (a distance of jump = 3)
"""
Approach:

First, we will create an array fib[] for storing fibonacci numbers.
Then, we will create a DP array and initialize it with INT_MAX and the 0th index DP[0] = 0
 and will move in the same way as Coin Change Problem with minimum number of coins.
The DP definition and recurrence is as followed:

DP[i] = min( DP[i], 1 + DP[i-fib[j]] )

where i is the current index and j denotes
the jth fibonacci number of which the
jump is possible
Here DP[i] denotes the minimum steps required to reach index i considering all Fibonacci
numbers."""

import sys

INT_MAX = sys.maxsize


# # Time Complexity: O(Nlog(N))
def minFebJumpsArrayEnd(array, ln):
    # We consider only those Fibonacci numbers which are less than n,
    # where we can consider fib[30] to be the upper bound as this will cross 10^5
    fib = [0 for i in range(30)]
    fib[0], fib[1] = 0, 1
    for i in range(2, 30):
        fib[i] = fib[i - 1] + fib[i - 2]

    # DP[i] will be storing the minimum number of jumps required for the position i. So DP[N+1]
    # will have the result we consider 0 as source and N+1 as the destination
    DP = [INT_MAX for i in range(ln + 1)]
    DP[0] = 0

    for i in range(1, ln + 1):
        # Calculate the minimum of that position if all the Fibonacci numbers are considered
        for j in range(1, 30):
            if (array[i - 1] == 1 or i == ln) and (i >= fib[j]):
                DP[i] = min(DP[i], 1 + DP[i - fib[j]])

    if DP[ln] != INT_MAX:
        return DP[ln]
    else:
        return -1


# # Time Complexity: O(Nlog(N))
if __name__ == '__main__':
    arr = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
    n = len(arr)
    print(minFebJumpsArrayEnd(arr, n))  # # Time Complexity: O(Nlog(N))
