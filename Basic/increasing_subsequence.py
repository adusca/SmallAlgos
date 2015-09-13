def lis_aux(array, i, cache):
    """
    input: an integer array and an index 0 <= i < len(array)
    output: the length of the longest increasing subsequence
    such that the first element has index i
    """
    if cache[i] != -1:
        return cache[i]
    first = array[i]
    max_len = 0
    for k in range(i + 1, len(array)):
        if array[k] >= first:
            max_len = max(max_len, lis_aux(array, k, cache))
    cache[i] = 1 + max_len
    return cache[i]


def lis(array):
    n = len(array)
    cache = [-1 for _ in xrange(n)]
    return max(lis_aux(array, i, cache) for i in xrange(n))


print lis([1, 2, 3, 4, 5, 6])
print lis([1, 2, 3, 4, 5, 6, 1, 2, 3, 4])
print lis([1, 4, 2, 3, 3, 2, 4, 1, 5, 6])
