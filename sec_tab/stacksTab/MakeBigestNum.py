def MakeBiggestNum(arr, ln):
    if ln == 1:
        return arr[0]
    maxNumStr = str(max(arr))
    maxDigits = len(maxNumStr)
    NumDict = {}
    # print(maxNumStr, maxDigits)
    for i in range(ln):
        if len(str(arr[i])) <= maxDigits + 1:
            k = (maxDigits + 1) % (len(str(arr[i])))
            req = (maxDigits + 1) // (len(str(arr[i])))
            # print(f" for i= {i} k is {k} and req= {req}")
            if k == 0:
                strKey = str(arr[i]) * req
                strVal = str(arr[i])
                NumDict[strKey] = strVal
                arr[i] = str(arr[i]) * req
            else:
                strKey = str(arr[i]) * req + str(arr[i])[0:k]
                strVal = str(arr[i])
                NumDict[strKey] = strVal
                arr[i] = str(arr[i]) * req + str(arr[i])[0:k]
    arr.sort(reverse=True)
    print(arr)
    finalAns = ""
    print(NumDict)
    for i in arr:
        finalAns += NumDict.get(i)
    return finalAns


if __name__ == '__main__':
    array = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]
    print(MakeBiggestNum(array, len(array)))
