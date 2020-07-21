def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
       if arr[i] == target:
        return i

    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            high = mid - 1

        if target > arr[mid]:
            low = mid + 1
    # Your code here


    return -1  # not found

arr = [3, 4, 6, 16, 26, 28, 52, 55]
print(binary_search(arr, 4))