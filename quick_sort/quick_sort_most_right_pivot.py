def quicksort(arr, low, high):
    if low < high:
        # 피벗을 high 값으로 설정
        pivot_index = partition(arr, low, high)
        # 피벗 기준으로 좌우 부분을 다시 정렬
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # 피벗을 high 값으로 설정
    pivot = arr[high]
    rightHI = low - 1  # 피벗보다 작은 값들의 끝 인덱스

    for j in range(low, high):
        if arr[j] <= pivot:
            rightHI += 1
            arr[rightHI], arr[j] = arr[j], arr[rightHI]

    # 피벗을 자신의 올바른 위치에 놓기
    arr[rightHI + 1], arr[high] = arr[high], arr[rightHI + 1]
    return rightHI + 1


# 사용 예시
arr = [2,8,7,1,3,5,6,9]
quicksort(arr, 0, len(arr) - 1)
print("정렬된 배열:", arr)
