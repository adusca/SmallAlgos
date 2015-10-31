def lcs(s, t):
    """
    input: two strings s and t
    output: the length of the longest common subsequence of s and t
    """
    # D[i][j] = lcs(s[:i], t[:j])
    n = len(s)
    m = len(t)
    D = [[0]*(m + 1) for _ in xrange(n + 1)]
    extra_str = [[None]*(m + 1) for _ in xrange(n + 1)]
    prev = [[None]*(m + 1) for _ in xrange(n + 1)]
    for i in xrange(1, n+1):
        for j in xrange(1, m+1):
            if s[i-1] == t[j-1]:
                D[i][j] = D[i-1][j-1] + 1
                extra_str[i][j] = s[i-1]
                prev[i][j] = (i-1, j-1)
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
                extra_str[i][j] = ""
                prev[i][j] = max((i-1, j), (i, j-1), key=lambda (a, b): D[a][b])

    ans = ""
    cur = (n, m)
    while D[cur[0]][cur[1]] > 0:
        ans += extra_str[cur[0]][cur[1]]
        cur = prev[cur[0]][cur[1]]
    return ans[::-1]

print lcs('ABCBDAB', 'BDCABC')
