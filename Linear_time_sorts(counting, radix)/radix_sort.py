# Counting sort as a helper function for radix sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # count array to store occurrences of digits (0 to 9)

    # Store the count of occurrences for each digit
    for i in range(n):
        index = (arr[i] // (10**exp)) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // (10**exp)) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] contains sorted numbers
    # according to the current digit
    for i in range(n):
        arr[i] = output[i]

# Radix Sort function
def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Do counting sort for every digit. exp is 10^i (i is current digit position)
    exp = 0
    while max_val // (10**exp) > 0:
        counting_sort(arr, exp)
        exp += 1

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)
