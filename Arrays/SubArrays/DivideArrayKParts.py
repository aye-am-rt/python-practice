"""
Divide an array into K sub array with the given condition
Given an array arr[] and an integer K. The task is to divide the array into K parts
( sub array ) such that the sum
of the values of all sub array is minimum.

The value of every sub array is defined as:

Take the maximum from that sub array.
Subtract each element of the sub array with the maximum.
Take the sum of all the values after subtraction.

The task is to minimize the sum of the values after dividing the array into K parts.

SOLUTION=
So, We can form a basic recursive formula and that computes every possible solution and finds
the best possible solution. We can see that the recursive solution has many overlapping
sub-problems we can reduce the complexity using Dynamic programming.

Recursive formula:
F(i, K) = { min of all values such that j < i [ max(Arr[i..j]) * (i – j + 1) – Sum(A[i…j] ]
          } + F(j, K-1)

The bottom-up approach can be used to compute the values of sub-problems first and store them.

    Here dp[i][j] defines the minimum value that can be obtained if the array is starting from
    index i and have j partition
So, the answer to the problems will be dp[0][K], array starting at 0 and having K partitions."""


def divideArrayKParts(ary, ln, kParts):
    dp = [[0 for i in range(500)] for j in range(500)]
    kParts -= 1
    for i in range(ln - 1, -1, -1):
        for j in range(0, kParts + 1):
            dp[i][j] = 10 ** 9
            maxx = -1
            summ = 0
            for subElem in range(i, ln):
                maxx = max(maxx, ary[subElem])
                summ += arr[subElem]
                diffSum = maxx * (subElem - i + 1) - summ
                if j > 0:
                    dp[i][j] = min(dp[i][j], diffSum + dp[subElem + 1][j - 1])
                else:
                    dp[i][j] = diffSum

    for i in range(n + 1):
        for j in range(k + 1):
            print(dp[i][j], end="  ")
        print(" ")
    return dp[0][kParts]


# Driver code
arr = [2, 9, 5, 4, 8, 3, 6]
n = len(arr)
k = 2
print("ans = ", divideArrayKParts(arr, n, k))
