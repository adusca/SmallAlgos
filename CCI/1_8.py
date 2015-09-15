def zero_matrix(M):
    columns = [None for _ in xrange(len(M[0]))]
    lines = [None for _ in xrange(len(M))]

    # Finding the zeros
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if M[i][j] == 0:
                columns[j] = 0
                lines[i] = 0

    # Zeroing what needs to be zeroed
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if columns[j] == 0 or lines[i] == 0:
                M[i][j] = 0


def test_zero_matrix():
    M = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 0, 14, 15]]
    N = [[1, 2, 0, 4, 5], [6, 7, 0, 9, 10], [0, 0, 0, 0, 0]]
    zero_matrix(M)
    assert M == N

test_zero_matrix()
