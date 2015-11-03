def binary_search(lst, num):
    """
    input: a sorted list lst and a number num
    output: the smallest index i such that lst[i] >= num,
    if the whole list is smaller then num, return len(lst)
    """
    # P(i) := (lst[i] >= num) goes from False to True
    # P(smaller-1) = False
    # P(larger) = True
    larger = len(lst)
    smaller = 0
    while larger > smaller:
        # mid < larger
        # smaller < mid + 1
        mid = (larger + smaller)/2
        if lst[mid] >= num:
            # P(mid) = True
            larger = mid
            # P(larger) = True
        else:
            # P(mid) = False
            smaller = mid + 1
            # P(smaller - 1) = P(mid) = False
    return larger


def modified_binary_search(lst, num):
    """
    input: a sorted list lst and a number num
    output: the largest index i such that lst[i] <= num,
    if the whole list is larger then num, return -1
    """
    # P(larger+1) = False
    # P(smaller) = True
    larger = len(lst) - 1
    smaller = -1
    while larger > smaller:
        mid = (larger + smaller + 1)/2
        if lst[mid] > num:
            larger = mid - 1
        else:
            smaller = mid
    return larger


def binary_sqrt(num):
    """
    input: a positive interger num
    output: the largest number s such that Pred(s) := (s**2 <= num) is true
    """
    # The property we maintain is that
    # P(low) = True, P(high+1) = False
    high = num
    low = 0
    while low < high:
        # low < mid
        # mid - 1 < high
        mid = (high + low + 1)/2
        if mid*mid > num:
            # P(mid) = False
            high = mid - 1
            # P(high + 1) = P(mid) = False
        else:
            # P(mid) = True
            low = mid
            # P(low) = True

    # P(low) = True
    # P(high+1) = P(low+1) = False
    return low

for i in xrange(1, 102, 10):
    print i, binary_sqrt(i)

print binary_search([1, 1, 1, 2, 2, 2], 2)
print modified_binary_search([1, 1, 1, 2, 2, 2], 2)
print modified_binary_search([1, 1, 1, 2, 2, 2], -1)
print binary_search([1, 1, 1, 2, 2, 2], 3)
print binary_search([1, 2, 4, 5], 3)
print binary_search([], 2)
