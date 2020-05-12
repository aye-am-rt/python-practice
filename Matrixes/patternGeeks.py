import math


def printPyramidGivenBase(num):
    for i in range(1, num + 1):
        for j in range(num, (i-1), -1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*  ", end=" ")
        print(" ")


def printTriangle(num):
    mh = int(math.sqrt(1 + 8.0 * num) - 1) // 2
    sp = 2 * mh - 2
    ch = 1
    for i in range(mh):
        for j in range(sp):
            print(" ", end="")
        sp -= 1
        for j in range(i + 1):
            print(ch, end=" ")
            ch += 1
        print(" ")


if __name__ == '__main__':
    n = int(input("give a number for patterns = "))
    printPyramidGivenBase(n)
    print("///////////////////////////////")
    """ /////////////////////////////// 2nd question print below pattern given last term like 6 here
        1 
       2  3
     4   5   6 
     """
    N = 9   # only 6 tk will be printed coz before 10 , 4th line will be incomplete.
    printTriangle(N)
