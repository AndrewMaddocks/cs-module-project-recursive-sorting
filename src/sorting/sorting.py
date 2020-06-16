# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

  # identify pointers
    point_A = 0
    point_B = 0
    # for loop
    for el in range(0, len(merged_arr)):
        if point_A >= len(arrA):
            merged_arr[el] = arrB[point_B]
            point_B += 1

        elif point_B >= len(arrB):
            merged_arr[el] = arrA[point_A]
            point_A += 1

        elif arrA[point_A] < arrB[point_B]:
            merged_arr[el] = arrA[point_A]
            point_A += 1

        else:
            merged_arr[el] = arrB[point_B]
            point_B += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # what do we do if we get an empty array
    # we need a base case
    if len(arr) <= 1:
        return arr
    # a for loop that will merge
    # identify pointers
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    arr = merge(left, right)
    # we need recursion

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
