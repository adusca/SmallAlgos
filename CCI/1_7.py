def rotate_matrix(M):
    """
    input: a squared matrix M represented as an array of arrays
    output: M rotated by 90 degrees
    """
    transpose_matrix(M)
    mirror_matrix_in_place(M)


def transpose_matrix(M):
    n = len(M)
    for i in xrange(n):
        for j in xrange(i + 1, n):
            M[i][j], M[j][i] = M[j][i], M[i][j]


def mirror_matrix(M):
    n = len(M)
    for i in xrange(n):
        M[i] = M[i][::-1]


def mirror_matrix_in_place(M):
    m = len(M[0])
    for i in xrange(len(M)):
        for j in xrange(m/2):
            M[i][j], M[i][m - j - 1] = M[i][m - j - 1], M[i][j]


def test_rotate_matrix():
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    for line in M:
        print " ".join(map(str, line))
    print " "
    rotate_matrix(M)
    for line in M:
        print " ".join(map(str, line))

    assert M == N

test_rotate_matrix()
