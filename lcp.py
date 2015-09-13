from itertools import takewhile


class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        return reduce(self.pairLongestCommonPrefix, strs)

    def pairLongestCommonPrefix(self, s, t):
        """
        :type s, t: str
        :rtype: str
        """
        ans = takewhile(lambda (l, r): l == r, zip(s, t))
        return "".join(l[0] for l in ans)
