def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    rightHigh = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            rightHigh += 1
            arr[j], arr[rightHigh] = arr[rightHigh] , arr[j]

    arr[rightHigh + 1], arr[high] = arr[high], arr[rightHigh + 1]
    return rightHigh + 1

arr = [2,8,7,1,3,5,6,9]
quick_sort(arr, 0, len(arr) - 1)
print("정렬된 배열:", arr)