def printUpperTriangle(n):
    for i in range(n):
        for j in range(n):
            if i > j:  # if you make it i < j  it will become right angle triangle 1 to n stars
                print(" ", end=" ")
            else:
                print("*", end=" ")  # if you put 2 spaces after this *  pattern will become
                # reverse triangle.
        print(" ")
    return 0


def printPyramidPattern(num):
    for i in range(num):
        for j in range(i, num):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print(" ")


def printHollowPyramid(num):
    for i in range(1, num + 1):
        for j in range(i, num):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            if i == num or j == 1 or j == (2 * i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ")


def printReversePyramidPattern(num):
    for i in range(1, num + 1):
        for j in range(1, i):
            print(" ", end=" ")
        for j in range(1, 2 * num - (2 * i - 1) + 1):
            print("*", end=" ")
        print(" ")


def SecWayToPrintRightTriangle(num):
    for i in range(num):
        for j in range(2 * (num - i), -1, -1):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*  ", end=" ")
        print("")


if __name__ == '__main__':
    n = int(input("give a digit = "))
    printUpperTriangle(n)
    print("/////////////////////////////////////////")
    printPyramidPattern(n)
    print("/////////////////////////////////////////")
    printHollowPyramid(n)
    print("/////////////////////////////////////////")
    printReversePyramidPattern(n)
    print("/////////////////////////////////////////")
    SecWayToPrintRightTriangle(n)
