# # def quicksort(data)


# def countdown_to_one(n):
#     # 2 base case
#     if n == 0:
#         return
#     print(n)
#     # 3. move towards base case
#     countdown_to_one(n-1)  # 1 calls itself


# countdown_to_one(5)


# def sum_list(items):
#     # 1 base case
#     if len(items) == 1:
#         return items[0]
#     else:
#         return items[0] + sum_list(items[1:])  # 2 recursive call
#         # 3moves towards the base case


# sum_list([1, 2, 3, 4, 5])
# 1 + (2 + 3 + 4 + 5)
# 1 + (2 + (3 + 4 + 5))
# 1 + (2 + (3 + (4 + 5)))
# 1 + (2 + (3 + (4 + (5))))


# # fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# # we know the first two items are 0 and 1

# # we lnow that every item in the sequence is dtermined
# # by summing the previeous two items


# def naive_fibonacci(n):
#     # what is the base case?
#     # TODO: look at handlinf negatives
#     if n == 0:
#         return n
#     if n == 1:
#         return 1
#     # what is the recursive case?
#     n_minus_1 = naive_fibonacci(n-1)
#     n_minus_2 = naive_fibonacci(n-2)
#     return n_minus_1 + n_minus_2

#     # how does it move towards the base case
# naive_fibonacci(3)


# we expect a list
def quicksort(data):
    # check if data has 1 or 0 elements

    # (base case) a side only contains a single element
    if len(data) <= 1:
        return data

    # choose a pivot (first or last)
    pivot = data[0]
    # create sorage for LHS and RHS
    left = []
    right = []
    # we need to loop through each item
    for current in data[1:]:
        # if it is smaller, add to LHS storage
        if current <= pivot:
            left.append(current)
        else:
            right.append(current)
        # if is is bigger, add to RHS storage

    # recursuve case recursively quick sort all LHS and RHS until
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([1, 9, 5, 7, 6, 8, 4]))
