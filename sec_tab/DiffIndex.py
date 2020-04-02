"""Count the pairs in an array such that the difference between them and their indices is equal
Given an array arr[] of size N, the task is to count the number of pairs (arr[i], arr[j])
such that arr[j] – arr[i] = j – i.
Input: arr[] = {5, 2, 7}
Output: 1
The only valid pair is (arr[0], arr[2]) as 7 – 5 = 2 – 0 = 2.


Approach: A pair (arr[i], arr[j]) is said to be valid if (arr[j] – arr[i]) = (j – i), it can
also be written as (arr[j] – j) = (arr[i] – i) which is the difference of the element with its index.
 Now, the task is to divide the array into groups such that every group has equal difference of the
element with its index then for every group if it has N elements, the count of possible
 pairs will be (N * (N – 1)) / 2.
"""


# Function to return the count
# of all valid pairs
def countPairs(arr, n):
    # To store the frequencies
    # of (arr[i] - i)
    map = dict()
    for i in range(n):
        map[arr[i] - i] = map.get(arr[i] - i, 0) + 1

    # To store the required count
    res = 0
    for x in map:
        cnt = map[x]

        # If cnt is the number of elements
        # whose differences with their index
        # is same then ((cnt * (cnt - 1)) / 2)
        # such pairs are possible
        res += ((cnt * (cnt - 1)) // 2)

    return res


# Driver code
arr = [1, 5, 6, 7, 9]
n = len(arr)

print(countPairs(arr, n))
