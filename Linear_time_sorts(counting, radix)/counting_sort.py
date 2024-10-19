def counting_sort(arr):
    largest = max(arr)
    count_arr = [0] * (largest+1)
    for num in arr:
        count_arr[num] += 1

    sorted_arr = []

    for j in range(len(count_arr)):
        sorted_arr.extend([j]*count_arr[j])

    return sorted_arr

arr = [1,2,3,7,4,9,0,5,6,7,7,7]

print(counting_sort(arr))