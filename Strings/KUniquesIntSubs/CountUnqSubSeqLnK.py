"""Count unique subsequences of length K
Given an array of N numbers and an integer K. The task is to print the number of unique subsequences possible
of length K.

Examples:
Input : a[] = {1, 2, 3, 4}, k = 3
Output : 4.
Unique Subsequences are:
{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}

Input: a[] = {1, 1, 1, 2, 2, 2 }, k = 3
Output : 4
Unique Subsequences are
{1, 1, 1}, {1, 1, 2}, {1, 2, 2}, {2, 2, 2}
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach: There is a well-known formula how many subsequences of fixed length K can be chosen from N unique
 objects. But the problem here has several differences. One among them is the order in subsequences is important
  and must be preserved as in the original sequence. For such a problem there can be no ready combinatorics
  formula because the results depend on the order of the original array.
The main idea is to deal recurrently by the length of the subsequence. On each recurrent step, move from the
end to the beginning and count the unique combinations using the count of shorter unique combinations from the
previous step. More strictly on every step j we keep an array of length N and every element in the place p means
 how many unique subsequences with length j we found to the right of the element in place i, including i
  itsel"""


# Function which returns the number of
# unique subsequences of length K
def solution(A, k):
    # size of the vector which does is constant
    N = len(A)

    # bases cases
    if N < k or N < 1 or k < 1:
        return 0
    if N == k:
        return 1

    # Prepare arrays for recursion
    v1 = [0] * N
    v2 = [0] * N
    v3 = [0] * N

    # initiate separately for k = 1  initiate the last element
    v2[N - 1] = 1
    v3[ A[N - 1] - 1 ] = 1

    # initiate all other elements of k = 1
    for i in range(N - 2, -1, -1):

        # initialize the front element
        # to vector v2
        v2[i] = v2[i + 1]

        # if element v[a[i]-1] is 0
        # then increment it in vector v2
        if v3[A[i] - 1] == 0:
            v2[i] += 1
            v3[A[i] - 1] = 1

    # iterate for all possible values of K
    for j in range(1, k):

        # fill the vectors with 0
        v3 = [0] * N

        # fill(v1.begin(), v1.end(), 0) the last must be 0 as from last no unique  subarray can be formed
        v1[N - 1] = 0

        # Iterate for all index from which unique
        # subsequences can be formed
        for i in range(N - 2, -1, -1):
            # add the number of subsequence formed
            # from the next index
            v1[i] = v1[i + 1]

            # start with combinations on the
            # next index
            v1[i] = v1[i] + v2[i + 1]

            # Remove the elements which have
            # already been counted
            v1[i] = v1[i] - v3[A[i] - 1]

            # Update the number used
            v3[A[i] - 1] = v2[i + 1]

        # prepare the next iteration
        # by filling v2 in v1
        for i in range(len(v1)):
            v2[i] = v1[i]

        # last answer is stored in v2
    return v2[0]


# Function to push the vector into an array
# and print all the unique subarrays
def solve(a, n, k):
    # fill the vector with a[]
    v = a

    # Function call to print the count
    # of unique susequences of size K
    print(solution(v, k))


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    n = len(a)
    k = 3
    solve(a, n, k)
