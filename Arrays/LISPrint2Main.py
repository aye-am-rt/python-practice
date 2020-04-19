def printLISMain(lst, n):
    if n == 1:
        return lst
    if n == 2:
        lst.remove(min(lst))
        return lst
    listTillI = [[] for i in range(n)]  # [[] * (n+1)] this is not working. later showing index out of range
    listTillI[0].append(lst[0])
    # arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j] and len(listTillI[i]) < len(listTillI[j]) + 1:
                listTillI[i] = listTillI[j].copy()
        listTillI[i].append(lst[i])

    mx = listTillI[0]
    for x in listTillI:
        if len(x) > len(mx):
            mx = x

    return mx


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(printLISMain(arr, len(arr)))
    print(list(zip(range(4, -1, -1), range(4, -1, -1))))
