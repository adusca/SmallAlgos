def counting_sort(array, k):
    """
    input: an array of non-negative integers, all smaller then k
    ouput: the sorted array
    """
    count = [0 for i in xrange(0, k)]  # O(k)
    for num in array:  # O(n)
        count[num] += 1

    ans = [0 for i in xrange(0, len(array))]  # O(n)
    pointer = 0

    for index, num in enumerate(count):  # O(n)
        for i in xrange(num):
            ans[pointer] = index
            pointer += 1

    return ans


assert counting_sort([], 100) == [2]
assert counting_sort([3, 4, 21, 1, 2, 2, 2, 3], 30) == [1, 2, 2, 2, 3, 3, 4, 21]
