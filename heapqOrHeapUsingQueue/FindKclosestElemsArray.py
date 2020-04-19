from queue import PriorityQueue


# A simple solution is to sort the array. Then apply the method discussed to k closest values in
# a sorted array. its # Time Complexity : O(n Log n)

# ==================== BETTER SOLUTION ======================= #
# A better solution is to use Heap Data Structure
# 1) Make a max heap of differences with first k elements.
# 2) For every element starting from (k+1)-th element, do following.
# …..a) Find difference of current element with x.
# …..b) If difference is more than root of heap, ignore current element.
# …..c) Else insert the current element to the heap after removing the root.
# 3) Finally the heap has k closest elements.


def PrintKClosestElementsInArray(arr, n, x, k):
    # Make a max heap of difference with
    # first k elements.
    pq = PriorityQueue()
    for i in range(k):
        pq.put((-abs(arr[i] - x), i))
    # Now process remaining elements
    for i in range(k, n):
        diff = abs(arr[i] - x)
        p, pi = pq.get()
        curr = -p
        # If difference with current
        # element is more than root,
        # then put it back.
        if diff > curr:
            pq.put((-curr, pi))
        else:
            # Else remove root and insert
            pq.put((-diff, i))
    # Print contents of heap.
    while not pq.empty():
        p, q = pq.get()
        print("{} ".format(arr[q]), end="")


if __name__ == '__main__':
    array = [-10, -50, 20, 17, 80]
    xInArray, kClosest = 20, 2
    ln = len(array)
    PrintKClosestElementsInArray(array, ln, xInArray, kClosest)
