class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        max_length_seen = 0
        first = 0

        for char in s:
            while char in seen:
                seen.remove(s[first])
                first += 1
            seen.add(char)
            max_length_seen = max(max_length_seen, len(seen))

        return max_length_seen


A = Solution()

print A.lengthOfLongestSubstring('aaaaaa')
