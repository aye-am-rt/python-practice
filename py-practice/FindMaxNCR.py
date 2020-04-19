# Find a pair (n,r) in an integer array such that value of nCr is maximum
# Given an array of non-negative integers arr[]. The task is to find a pair (n, r) such that
# value of nCr is maximum possible r < n.
"""
Efficient approach: It is known from combinatorics:

When n is odd:
nC0 < nC1 ….. < nC(n-1)/2 = nC(n+1)/2 > ….. > nCn-1 > nCn

When n is even:
nC0 < nC1 ….. < nCn/2 > ….. > nCn-1 > nCn

Also, nCr = nCn-r

It can be observed that nCr will be maximum when n will be maximum and abs(r – middle) will be
minimum. The problem now boils down to finding the largest element in arr[] and r such that
 abs(r – middle) is minimum."""


# Driver code
def findPairToNCRMax(array, ln):
    if ln < 2:
        return -1
    if ln == 2:
        if array[0] > array[1]:
            return {'n': array[0], 'r': array[1]}
        else:
            return {'n': array[1], 'r': array[0]}

    else:
        mx = max(array)
        hlf = mx // 2
        closestToHalf = float('inf')
        r = 0
        for i, elem in enumerate(array):
            if abs(elem - hlf) < closestToHalf:
                closestToHalf = abs(elem - hlf)
                r = array[i]
        return {'n': mx, 'r': r}


if __name__ == "__main__":
    arr = [3, 8, 4]
    n = len(arr)

    print(findPairToNCRMax(arr, n))
