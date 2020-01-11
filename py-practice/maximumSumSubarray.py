from sys import maxsize


# Kadane’s Algorithm:

def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = start = end = s = 0
    for i in range(0, size):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    print("Maximum sum sub-array is %d" % max_so_far)
    print("Starting Index %d" % start)
    print("Ending Index %d" % end)


if __name__ == "__main__":
    l1 = [int(x) for x in input("give space separated numbers positive or negative = ").split()]
    maxSubArraySum(l1, len(l1))
