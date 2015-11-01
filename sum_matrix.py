def precompute_sums(M):
    sums = [[0]*(len(M[0]) + 1) for _ in xrange(len(M) + 1)]

    for i in xrange(1, len(M) + 1):
        for j in xrange(1, len(M[0]) + 1):
            sums[i][j] = M[i-1][j-1] + sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1]
    return sums


def solve():
    N, M = map(int, raw_input().split())
    matrix = []
    for i in xrange(N):
        matrix.append(map(int, raw_input().split()))
    Q = int(raw_input())
    sums = precompute_sums(matrix)
    for line in sums:
        print line
    for q in xrange(Q):
        i1, j1, i2, j2 = map(int, raw_input().split())
        i2 += 1
        j2 += 1
        print sums[i2][j2] - sums[i2][j1] - sums[i1][j2] + sums[i1][j1]

solve()
