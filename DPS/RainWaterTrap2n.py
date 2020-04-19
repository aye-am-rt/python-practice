def FindMaxRainWaterTrapped(arr, ln):
    if ln < 3:
        return -1
    leftMaxArr = [arr[0]] + [0] * (ln - 1)
    rightMaxArr = [0] * (ln - 1) + [arr[ln - 1]]

    for i in range(1, ln):
        if arr[i] >= leftMaxArr[i - 1]:
            leftMaxArr[i] = arr[i]
        else:
            leftMaxArr[i] = leftMaxArr[i - 1]
        # leftMaxArr[i] = max(arr[i], leftMaxArr[i - 1])
    for i in range(ln - 2, -1, -1):
        if arr[i] >= rightMaxArr[i + 1]:
            rightMaxArr[i] = arr[i]
        else:
            rightMaxArr[i] = rightMaxArr[i + 1]
        # rightMaxArr[i] = max(arr[i], rightMaxArr[i + 1])
    waterTrapped = 0
    for i in range(ln):
        waterTrapped += min(leftMaxArr[i], rightMaxArr[i]) - arr[i]
    return waterTrapped


if __name__ == "__main__":
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(FindMaxRainWaterTrapped(array, len(array)))
