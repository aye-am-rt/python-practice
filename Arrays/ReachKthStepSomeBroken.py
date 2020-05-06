# Find the number of ways to reach Kth step in stair case
# Given an array arr[] of size N and an integer K. Array represents the broken steps in a
# staircase. One can not reach a broken step. The task is to find the number of ways to reach
# the Kth step in the staircase starting from 0 when a step of maximum length 2 can be taken
# at any position. The answer can be very large. So, print the answer modulo 109 + 7.
#
# Examples:
#
# Input: arr[] = {3}, K = 6
# Output: 4
# 0 -> 1 -> 2 -> 4 -> 5 -> 6
# 0 -> 1 -> 2 -> 4 -> 6
# 0 -> 2 -> 4 -> 5 -> 6
# 0 -> 2 -> 4 -> 6
#
# Approach: This problem can be solved using dynamic programming. Create a dp[] array where
# dp[i] will store the number of ways to reach the ith step and the recurrence relation will
# be dp[i] = dp[i – 1] + dp[i – 2] only if the ith step is not broken otherwise 0. The final
# answer will be dp[K].

MOD = 10 ** 7


def number_of_waysToReachKthStep(ar, ln, K, ):
    if K == 1:
        return 1
    dp = [-1 for i in range(K + 1)]

    # broken steps fill 0
    for i in range(ln):
        dp[ar[i]] = 0

    dp[0] = 1
    dp[1] = 1 if (dp[1] == -1) else dp[1]

    # Calculate the number of ways for  the rest of the positions
    for i in range(2, K + 1):
        if dp[i] != 0:  # # If it is a blocked position
            dp[i] = dp[i - 1] + dp[i - 2]

            dp[i] = dp[i] % MOD

    return dp[K]


if __name__ == "__main__":
    brokenSteps = [3]
    n = len(brokenSteps)
    k = 6
    print(number_of_waysToReachKthStep(brokenSteps, n, k))
