"""perm_identity
Count number of ways to cover a distance | Set 2
Given a distance N. The task is to count the total number of ways to cover the distance
 with 1, 2 and 3 steps.

Examples:

Input: N = 3
Output: 4
All the required ways are (1 + 1 + 1), (1 + 2), (2 + 1) and (3).
Input: N = 4
Output: 7

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach: In previous article, a recursive and dynamic programming based approach has been
discussed. Here we will reduce the space complexity. It can be onserved that to calculate the
 number of steps to cover the distance i, only the last three states are required (i – 1,
 i – 2, i – 3). So, the result can be calculated using the last three states.

Below is the implementation of the above approach:"""


# Function to return the count of the
# total number of ways to cover the
# distance with 1, 2 and 3 steps
def countWays(n):
    # Base conditions
    if n == 0:
        return 1
    if n <= 2:
        return n

        # To store the last three stages
    f0 = 1
    f1 = 1
    f2 = 2
    ans = 0

    # Find the numbers of steps required
    # to reach the distance i
    for i in range(3, n + 1):
        ans = f0 + f1 + f2
        f0 = f1
        f1 = f2
        f2 = ans

        # Return the required answer
    return ans


n = 4
print(countWays(n))
