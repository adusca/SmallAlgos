import bisect
from bit import Bit


def lis_aux(array, i, cache):
    """
    input: an integer array and an index 0 <= i < len(array)
    output: the length of the longest strictly increasing
    subsequence such that the first element has index i
    """
    if cache[i] != -1:
        return cache[i]
    first = array[i]
    max_len = 0
    for k in range(i + 1, len(array)):
        if array[k] > first:
            max_len = max(max_len, lis_aux(array, k, cache))
    cache[i] = 1 + max_len
    return cache[i]


def lis(array):
    n = len(array)
    cache = [-1 for _ in xrange(n)]
    return max(lis_aux(array, i, cache) for i in xrange(n))


def lis_bit(array):
    M = max(array)
    bit = Bit(max, 0, M)
    for num in array:
        # arr[val] is the lis that ends with val
        a = bit.compute(num - 1)
        bit.update(num, a + 1)
    return bit.compute(M)


def lis_traditional(array):
    """
    If we want to have a list such that list[i] is the
    smallest ending for a increasing subsequence of size i
    We can iterate for every num in the array finding where to
    update to keep the property:
    1 -> x1
    2 -> x2
          num
    3 -> x3
    We can update to:
    1 -> x1
    2 -> x2
    3 -> num
    """
    M = min(len(array), max(array)) + 1
    # smallest_val[i] = smallest ending of a increasing subsequence of len i
    smallest_val = [M]*M
    smallest_val[0] = 0
    # smallest_idx[i] = index of the smallest ending of an inc subseq of len i
    smallest_idx = [-1]*M
    prev = [None]*len(array)
    for i, num in enumerate(array):
        index = bisect.bisect_left(smallest_val, num)
        smallest_val[index] = num
        smallest_idx[index] = i
        prev[i] = smallest_idx[index - 1]
    last = smallest_idx[bisect.bisect_left(smallest_val, M) - 1]
    ans = []
    while last != -1:
        ans.append(array[last])
        last = prev[last]
    return ans[::-1]


print lis([1, 2, 3, 4, 5, 6])
print lis([1, 2, 3, 4, 5, 6, 1, 2, 3, 4])
print lis([1, 4, 2, 3, 3, 2, 4, 1, 5, 6])
print lis_bit([1, 2, 3, 4, 5, 6])
print lis_bit([1, 2, 3, 4, 5, 6, 1, 2, 3, 4])
print lis_bit([1, 4, 2, 3, 3, 2, 4, 1, 5, 6])
print lis_traditional([1, 2, 3, 4, 5, 6])
print lis_traditional([5, 4, 3, 2, 1])
print lis_traditional([1, 2, 3, 4, 5, 6, 1, 2, 3, 4])
print lis_traditional([1, 4, 2, 3, 3, 2, 4, 1, 5, 6])
