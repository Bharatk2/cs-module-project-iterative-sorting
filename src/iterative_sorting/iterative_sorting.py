# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_value = arr[cur_index]
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # Your code here
        # I want to take the index by the length of arr
        # i want to use unsorted index
        for unsorted_index in range(cur_index, len(arr)):
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps_occurred = True 
    # Iterating through the arr and looking at elements two at a time
    # swapping them if they're out of order
    # if we do this all the way through, all the elements will
    # eventually end up in sorted order
    # we know all the elements are in sorted order when we do a full
    # pass through the array and perform no swaps.
    while swaps_occurred:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # parallel to selection sort: builds up the sorted portion of the array
    # starting by putting the largest element at the end of the array 
    # second-largest at the second-to-last spot, etc.
    
    # the number of iteration through the array that we need to make is equal
    # to the number of elemnents in the array - P(n^2)
    

    return arr

def recursive_bubble_sort(arr, unsorted_length):
    # hwo do we get closer to a base casE?
    # each pass shortens the unsorted portion by 1
   # each
    # base case8s)
    # re-use the swaps_occured boolean idea
    for i in range(unsorted_length - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length - 1)
arr = [33, 44, 55, 11, 33, 100]
print(recursive_bubble_sort(arr, len(arr)))

# the partition function handles the work of
# selecting a pivot element and partitioning
# the data in the array around that pivot
# returns the left partition, the pivot, and the right partition.
def partition(arr):
    # pick the first element as the pivot element
    pivot = arr[0]
    left = []
    right = []

    # iterate through the rest of the array, putting each
    # element in the appropriate bucket
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right
def quicksort(arr):
    # base case
    # if the length of the array is 0
    if len(arr) <= 1:
        return arr

    #how do we get closer to our base casde?
    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)
    # the boolean tells us when the unsorted portion of

arr = [13, 9, 55, 100, 22, 33]

print(quicksort(arr))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
