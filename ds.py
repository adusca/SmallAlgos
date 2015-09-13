class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        num = [[0 for _ in xrange(len(t) + 1)] for _ in xrange(len(s) + 1)]

        num[0][0] = 1

        for i in xrange(1, len(s)+1):
            num[i][0] = 1
            for j in xrange(1, len(t)+1):
                num[i][j] = num[i-1][j]
                if s[i-1] == t[j-1]:
                    num[i][j] += num[i-1][j-1]

        return num[len(s)][len(t)]

A = Solution()
print A.numDistinct('rabbbit', 'rabbit')
