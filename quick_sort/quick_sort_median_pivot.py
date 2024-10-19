def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a = arr[low]
    b = arr[mid]
    c = arr[high]

    # 세 값 중 중앙값을 구함
    if a < b:
        if b < c:
            return mid  # b가 중앙값
        elif a < c:
            return high  # c가 중앙값
        else:
            return low  # a가 중앙값
    else:
        if a < c:
            return low  # a가 중앙값
        elif b < c:
            return high  # c가 중앙값
        else:
            return mid  # b가 중앙값


def partition(arr, low, high):
    # Median of three 방식으로 피벗 선택
    pivot_index = median_of_three(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 사용 예시
arr = [2,8,7,1,3,5,6,9]
quicksort(arr, 0, len(arr) - 1)
print("정렬된 배열:", arr)
