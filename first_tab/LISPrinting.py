def printLIS(lt1, n):
    if n == 1:
        return lt1
    if n == 2:
        lt1.remove(min(lt1))
        return lt1

    listTillI = [lt1[0]]
    resultList = []
    mx = float('-inf')
    for i in range(1, n):
        for j in range(i, n):
            if lt1[j] > mx:
                mx = lt1[j]
                listTillI.append(mx)
        if len(listTillI) > len(resultList):
            resultList = listTillI
            mx = float('-inf')
            listTillI = [lt1[0]]

    return resultList


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(printLIS(arr, len(arr)))
