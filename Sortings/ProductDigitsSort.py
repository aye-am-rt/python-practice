# Sort the numbers according to their product of digits
# Given an array arr[] of N non-negative integers, the task is to sort these integers according
# to the product of their digits.
#
# Examples:
#
# Input: arr[] = {12, 10, 102, 31, 15}
# Output: 10 102 12 31 15
# 10 -> 1 * 0 = 0
# 102 -> 1 * 0 * 2 = 0
# 12 -> 1 * 2 = 2
# 31 -> 3 * 1 = 3
# 15 -> 1 * 5 = 5


def productOfDigits(elem):
    if elem == 0:
        return 1
    prod = 1
    while elem > 0:
        prod *= (elem % 10)
        elem //= 10
    return prod


def sortArrDigitsProduct(ar, ln):
    if ln == 1:
        print(ar[0])
    print("given array == ", ar)
    PairList = []
    for elem in ar:
        PairList.append((productOfDigits(elem), elem))
        # made a tuple of products of digits and the element in array
    # when sorting done by default it will sort by first Element of tuple
    print("pairList before sorting == ", PairList)
    PairList.sort()  # or use reverse=True to sort in descending order
    print("pairList after sorting increasing order == ", PairList)

    for i in range(len(PairList)):
        print(PairList[i][1], end="  ")
    # printing the second elements of tuple which is also element in array


if __name__ == "__main__":
    arr = [12, 10, 102, 31, 15]
    n = len(arr)

    sortArrDigitsProduct(arr, n)
