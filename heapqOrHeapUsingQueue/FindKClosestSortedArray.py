"""Find k closest elements to a given value
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
Examples:
Input: K = 4, X = 35
arr[] = {12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
Note that if the element is present in array, then it should not be in output, only the other
closest elements are required.

A simple solution is to do linear search for k closest elements.
1) Start from the first element and search for the crossover point (The point before which
elements are smaller than or equal to X and after which elements are greater). This step takes
O(n) time.
2) Once we find the crossover point, we can compare elements on both sides of crossover point to
print k closest elements. This step takes O(k) time.

The time complexity of the above solution is O(n).

An Optimized Solution is to find k elements in O(Logn + k) time. The idea is to use Binary Search
to find the crossover point. Once we find index of crossover point, we can print k closest
elements in O(k) time.
"""
import bisect


def printKClosestInSortedArray(array, xInArray, kClosest, ln):
    if ln < kClosest:
        print("not enough elements ")

    # assuming all elements are distinct otherwise make a set but it will not be in sorted format
    # so we have to sort it again. ===> set_list = list(set(array)) this will not maintain order
    sorted_set_list = sorted(list(set(array)))
    print(sorted_set_list)
    # now we can easily get index of req element using built in index function.
    # indexOfx = sorted_set_list.index(xInArray)  # but this uses linear Search so takes more time.
    indexOfx = bisect.bisect_left(sorted_set_list, xInArray)
    """if index < len(elements) and elements[index] == value:
        return index"""
    # bisect.bisect and bisect.bisect_right are same and give the 1 ahead position of element(0 base)
    # bisect.bisect_left gives actual position assuming 0 base indexing in array.(binary search)
    print(indexOfx)
    l = indexOfx
    r = l + 1
    count = 0
    if sorted_set_list[l] == xInArray:
        l -= 1
    while l >= 0 and r < ln and count < kClosest:
        if xInArray - sorted_set_list[l] < sorted_set_list[r] - xInArray:
            print(sorted_set_list[l], end=" ")
            l -= 1
        else:
            print(sorted_set_list[r], end=" ")
            r += 1
        count += 1

    while count < kClosest and l >= 0:
        print(sorted_set_list[l], end=" ")
        l -= 1
        count += 1
    while count < kClosest and r < ln:
        print(sorted_set_list[r], end=" ")
        r += 1
        count += 1


if __name__ == "__main__":
    arr = [12, 12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    n = len(arr)
    x = 35
    k = 4
    printKClosestInSortedArray(arr, x, 4, n)
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(3000)
    # print(sys.getrecursionlimit())

# I am trying to convert a set to a list in Python 2.6. I'm using this syntax:
# first_list = [1,2,3,4]
# my_set=set(first_list)
# my_list = list(my_set)

"""
It is already a list

type(my_set)
>>> <type 'list'>
Do you want something like

my_set = set([1,2,3,4])
my_list = list(my_set)
print my_list
>> [1, 2, 3, 4]
EDIT : Output of your last comment

>>> my_list = [1,2,3,4]
>>> my_set = set(my_list)
>>> my_new_list = list(my_set)
>>> print my_new_list
[1, 2, 3, 4]"""
