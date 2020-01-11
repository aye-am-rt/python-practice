def printUpperTriangle(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i > j:
                print(" ", end=" ")
            else:
                print("* ", end=" ")
        print("\n")
    return 0


if __name__ == '__main__':
    n = int(input("give a digit"))
    printUpperTriangle(n)
