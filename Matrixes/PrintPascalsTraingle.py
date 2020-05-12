# Python3 program for Pascal's Triangle
# A O(n^2) time and O(1) extra
# space method for Pascal's Triangle


def printPascal(n):
    for i in range(1, n + 1):
        C = 1  # used to represent C(i, j)   #  i can be seen as line number
        for j in range(1, i + 1):
            # The first value in a line(or i ) is always 1
            print(C, end=" ")
            C = int(C * (i - j) / j)
        print("")


if __name__ == '__main__':
    n = 5
    printPascal(n)

"""
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
"""
