def count_differences(k, arr):
    """
    input: a positive number k and an array of numbers arr
    output: how many pairs in arr have a difference of exactly k
    """
    ans = 0
    hash_table = set(arr)
    for num in arr:
        if num + k in hash_table:  # O(1) average case
            ans += 1
    return ans
