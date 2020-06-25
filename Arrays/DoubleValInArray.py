# Given an array of size n and an integer b, traverse the array and if the element in array is b,
# double b and continue traversal. In the end return value of b.
# Input:
# The first line of the input contains T denoting the number of test-cases. Then follows the
# description of test-cases. The first line of each testcase contains two space separated positive
# integers n and b denoting the size of array and initial value of b respectively.The second line
# contains n space separated positive integers denoting the elements of array.
# Output:
# For each testcase, print the final value of b.


def DoubleNumberInArray(ar, nd):
    print(f"given num = {nd}")
    curr = nd
    for elem in ar:
        print(f"elem = {elem}", end=" ,")
        if elem == curr:
            curr = curr * 2
            print(f"curr value after doubling = {curr}")

    return curr


if __name__ == '__main__':
    t = int(input("give number of testCases = "))
    for i in range(t):
        size, num = map(int, input("give space separated sizeOfArray and the numberInitially = ")
                        .strip(" ").split(" "))
        print(f" test case = {i} , size = {size}, num = {num}")
        arr = [int(i) for i in input("give space separated Array Elements = ").strip(" ").split(" ")]
        print("printing final value of num after doubling = ")
        print(DoubleNumberInArray(arr, num))
