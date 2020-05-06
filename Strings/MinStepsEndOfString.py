# Find minimum number of steps to reach the end of String
# Given a binary string str of length N and an integer K, the task is to find the minimum
# number of steps required to move from str[0] to str[N – 1] with the following moves:
#
# From an index i, the only valid moves are i + 1, i + 2 and i + K
# An index i can only be visited if str[i] = ‘1’
# Examples:
#
# Input: str = “101000011”, K = 5
# Output: 3
# str[0] -> str[2] -> str[7] -> str[8]
"""
Approach: The idea is to use dynamic programming to solve the problem.

It is given that for any index i, it is possible to move to an index i+1, i+2 or i+K.
One of the three possibilities will give the required result that is the minimum number of
 steps to reach the end.
Therefore, the dp[] array is created and is filled in a bottom-up manner."""

import sys

INT_MAX = sys.maxsize


def minSteps(st, ln, K):
    if st[ln - 1] == '0':
        return -1
    if ln == 1:
        return 0
    if ln < 4:  # If the length is 2 or 3 then the end  can be reached in a single step
        return 1

    dp = [0] * ln

    dp[n - 1] = 0  # It requires no move from the  end to reach the end
    dp[n - 2] = 1  # according to given conditions in question
    dp[n - 3] = 1

    for i in range(ln - 4, -1, -1):
        if st[i] != 0:  # only then its reachable

            steps = INT_MAX  # # To store the minimum steps required from the current index
            if i + K < ln and st[i + k] == '1':
                steps = min(steps, dp[i + K])

            if st[i + 1] == '1':
                steps = min(steps, dp[i + 1])
            if st[i + 2] == '1':
                steps = min(steps, dp[i + 2])
            # dp[i] = steps if (steps == INT_MAX) else (1 + steps)
            if steps == INT_MAX:
                dp[i] = INT_MAX
            else:
                dp[i] = steps+1

    # Cannot reach the end starting from str[0]
    if dp[0] == INT_MAX:
        return -1

    return dp[0]


if __name__ == "__main__":
    string = "101000011"
    n = len(string)
    k = 5
    print(minSteps(string, n, k))
