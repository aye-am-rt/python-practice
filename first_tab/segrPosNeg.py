def segregatePositiveNegative(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] < 0:
            i += 1
        elif arr[j] > 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    # l1 = [int(x) for x in input("give space separated positive numbers for list 1 = ").split()]
    # print("given array = ", l1)
    l1 = [2, 12, 34, 56, -1, 3, -2, 3, 4, 5, -1, -2, -8]
    print("after Segregating pos and neg  = ", segregatePositiveNegative(l1))
