def FindMaxRainWaterTrapped(arr, ln):
    if ln < 3:
        return -1
    left = 0
    right = ln - 1
    left_max = right_max = -1
    result = 0

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                result += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                result += right_max - arr[right]
            right -= 1

    return result


if __name__ == "__main__":
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(FindMaxRainWaterTrapped(array, len(array)))
