def binary_search(lst, num):
    """
    input: a sorted list lst and a number num
    output: the smallest index i such that lst[i] >= num,
    if the whole list is smaller then num, return len(lst)
    """
    larger = len(lst)
    smaller = 0
    while larger > smaller:
        mid = (larger + smaller)/2
        if lst[mid] >= num:
            larger = mid
        else:
            smaller = mid + 1
    return larger


def modified_binary_search(lst, num):
    """
    input: a sorted list lst and a number num
    output: the largest index i such that lst[i] <= num,
    if the whole list is larger then num, return -1
    """
    larger = len(lst) - 1
    smaller = -1
    while larger > smaller:
        mid = (larger + smaller + 1)/2
        if lst[mid] > num:
            larger = mid - 1
        else:
            smaller = mid
    return larger


print binary_search([1, 1, 1, 2, 2, 2], 2)
print modified_binary_search([1, 1, 1, 2, 2, 2], 2)
print modified_binary_search([1, 1, 1, 2, 2, 2], -1)
print binary_search([1, 1, 1, 2, 2, 2], 3)
print binary_search([1, 2, 4, 5], 3)
print binary_search([], 2)
