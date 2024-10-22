def quicksort(arr,start, end):
    if start < end:
        pivot_i = partition(arr,start,end)
        quicksort(arr,start,pivot_i - 1)
        quicksort(arr,pivot_i,end)
    return arr

def partition(arr,start,end):
    pivot = arr[end]
    right_high = start - 1
    for i in range(start,end):
        if arr[i] <= pivot:
            right_high += 1
            arr[i], arr[right_high] = arr[right_high], arr[i]

    arr[right_high + 1], arr[end] = arr[end], arr[right_high + 1]
    return right_high + 1

arr = [2,8,7,1,3,5,6,9]
print(quicksort(arr,0,len(arr) - 1))