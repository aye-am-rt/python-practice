def findPerfectSquareRoot(n):
    if n < 5:
        if n == 4:
            return 2
        elif n >= 0:
            return n
        else:
            return " this input is un-valid for square-root"
    for i in range(2, int(n / 2)):
        if i * i == n:
            return i
    return None


def findNonPerfectSquare(n):
    before = after = 0
    for i in range(2, n):
        if i * i > n:
            before = i - 1
            after = i
            break
    if before != 0 and after != 0:
        if n - before*before <= after*after - n:
            return before + (n-before*before)/(2*before)
        else:
            return after - (after*after-n)/(2*after)
    else:
        return None


if __name__ == '__main__':
    num = int(input("give a number"))
    res = findPerfectSquareRoot(num)
    if res is not None:
        print(res)
    else:
        print(findNonPerfectSquare(num))
