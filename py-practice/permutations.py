def printRecursivePermutations(a, left, right):
    if left == right:
        print(''.join(a))
    else:
        for i in range(left, right):
            a[left], a[i] = a[i], a[left]
            printRecursivePermutations(a, left + 1, right)
            a[left], a[i] = a[i], a[left]


if __name__ == "__main__":
    string = "four"
    printRecursivePermutations(list(string), 0, len(string))
