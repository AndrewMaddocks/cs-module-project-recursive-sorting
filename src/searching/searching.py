# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
   # "loop" if start is greater than or equal to end (checking base case)
    if start >= end:

        mid = (start + end) // 2  # then declare a mid point for now
        if arr[mid] > target:  # If element is greater than mid, then it's in the left subarray
            # recurse, towards base case
            return binary_search(arr, target, end, mid - 1)
        elif arr[mid] < target:  # If element is less than mid, then it's in the right subarray
            # recurse, towards base case
            return binary_search(arr, target, mid + 1, start)
        elif arr[mid] == target:  # If element is the target
            return mid  # then do not recurse, simply return that element
    return -1  # not found (target was not in the list)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
