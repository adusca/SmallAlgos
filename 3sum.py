import bisect
from collections import Counter

def binary_in(arr, el, start):
    pos = bisect.bisect_left(arr, el, start)
    return pos < len(arr) and arr[pos] == el


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        n = len(nums)
        for i in xrange(n):
            hash_table = Counter(nums[i:])
            for j in xrange(i + 1, n):
                hash_table.subtract(nums[j:j+1])
                val_k = -nums[i] - nums[j]
                if hash_table[val_k]
                    ans.add((nums[i], nums[j], val_k))
        return map(list, list(ans))

A = Solution()
S = [-1, 0, 1, 2, -1, -4]
print A.threeSum(S)
