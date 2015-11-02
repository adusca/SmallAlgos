from lcs import lcs


def palindrome_inserts(s):
    """
    input: a string s
    output: the minimum number of characters that must be inserted
    to make s a palindrome
    """
    # D[i][j] is the solution for s[i:j]
    n = len(s) + 1
    D = [[0]*n for _ in xrange(n)]
    for length in xrange(2, n):
        for end in xrange(length, n):
            start = end - length
            if s[start] == s[end-1]:
                D[start][end] = D[start+1][end-1]
            else:
                D[start][end] = 1 + min(D[start][end-1], D[start+1][end])
    return D[0][len(s)]


def alternative_pal(s):
    r = s[::-1]
    L = len(lcs(s, r))
    return len(s) - L

print palindrome_inserts('Ab3bd')
print palindrome_inserts('')
print alternative_pal('Ab3bd')
print alternative_pal('')
