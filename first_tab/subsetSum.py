# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given
# set with sum equal to given sum.
# Example:
# Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.


def isSubsetSum(l1, n, findSum):
    if findSum == 0:
        return True
    if n == 0 and findSum != 0:
        return False
    # for i in l1:      This does not works stack overflow recursion
    #     if i > findSum:
    #         l1.remove(i)
    # n = len(l1)
    if l1[n - 1] > findSum:
        return isSubsetSum(l1, n - 1, findSum)
    return isSubsetSum(l1, n - 1, findSum) or isSubsetSum(l1, n - 1, findSum - l1[n - 1])


if __name__ == "__main__":
    # l1 = [int(x) for x in input("give space separated positive numbers for list 1 = ").split()]
    # l1 = list(set(l1))
    l1 = [3, 34, 4, 12, 5, 2]
    print(l1)
    # findSum = int(input('give positive sum to find in list = '))
    findSum = 10
    nm = len(l1)
    if isSubsetSum(l1, nm, findSum):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")
