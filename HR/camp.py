def solve():
    n, m = map(int, raw_input().split())
    intervals = []
    G = [[] for _ in xrange(m)]
    for i in xrange(m):
        intervals.append(map(int, raw_input().split()))

    for i in xrange(m):
        for j in xrange(m):
            if i == j:
                continue
            if is_immediately_inner(intervals[i], intervals[j], intervals):
                G[j].append(i)

    def is_in(k, i):
        if not intervals[i][0] <= k <= intervals[i][1]:
            return False
        for j in G[i]:
            if intervals[j][0] <= k <= intervals[j][1]:
                return False
        return True

    def find_interval(k):
        for i in xrange(m):
            if is_in(k, i):
                return i

    ans = []
    for i in xrange(m):
        for j in G[i]:
            potential = intervals[j][0]
            if is_in(potential, j) and is_in(potential - 1, i):
                ans.append((potential - 1, potential))
            potential = intervals[j][1]
            if is_in(potential, j) and is_in(potential + 1, i):
                ans.append((potential, potential + 1))
    print len(ans)
    for x, y in ans:
        print x, y


def is_immediately_inner(i1, i2, intervals):
    if not (i1[0] >= i2[0] and i1[1] <= i2[1]):
        return False
    for i in intervals:
        if i == i2 or i == i1:
            continue
        if i1[0] <= i[0] <= i2[0] or i2[1] >= i[1] >= i1[1]:
            return False
    return True
