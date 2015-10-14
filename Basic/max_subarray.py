def max_subarray_sum(lst):
    """
    input: a list of numbers
    output: the largest possible subarray sum of lst
    """
    max_ending_here = 0
    max_so_far = 0
    for num in lst:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print max_subarray_sum([1, 2, -1, -1, 3, 4, -2, 1])
print max_subarray_sum([1, 1, -1, -1, 3, 4, -2, 10])
