# Python program to print Diamond shape


def Diamond(rows):
    n = 0
    for i in range(1, rows + 1):
        # loop to print spaces
        for j in range(1, (rows - i) + 1):
            print(end=" ")

        # loop to print star
        while n != (2 * i - 1):
            print("*", end="")
            n = n + 1
        n = 0

        # line break
        print()

    k = 1
    n = 1
    for i in range(1, rows):
        # loop to print spaces
        for j in range(1, k + 1):
            print(end=" ")
        k = k + 1

        # loop to print star
        while n <= (2 * (rows - i) - 1):
            print("*", end="")
            n = n + 1
        n = 1
        print()


if __name__ == '__main__':
    r = 5
    Diamond(r)
