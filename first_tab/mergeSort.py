def mergeCompared(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def mergeSort(lt):
    if len(lt) is 0:
        return "no element in array"
    if len(lt) is 1:
        return lt
    mid_point = (len(lt) // 2)
    left = lt[:mid_point]
    right = lt[mid_point:]
    return mergeCompared(mergeSort(left), mergeSort(right))


if __name__ == "__main__":
    l1 = [int(x) for x in input("give space separated positive numbers for list 1 = ").split()]
    print("given array = ", l1)
    # l1 = [2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]
    print("After merge sorting = ", mergeSort(l1))
