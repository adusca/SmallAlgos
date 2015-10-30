MAX = 10**5


def solve():
    n, m, q = map(int, raw_input().strip().split())
    count_bit = [0 for _ in xrange(MAX + 1)]
    sums = [0 for _ in xrange(MAX + 1)]
    A = map(int, raw_input().strip().split())

    for a in A:
        update_bit(count_bit, a, 1)
        update_bit(sums, a, a)

    for i in xrange(q):
        t, x, y = map(int, raw_input().strip().split())

        if t == 1:
            tmp = A[x - 1]
            A[x - 1] = y
            update_bit(count_bit, tmp, -1)
            update_bit(count_bit, y, 1)
            update_bit(sums, tmp, -tmp)
            update_bit(sums, y, y)

        if t == 2:
            print ans(x, y, m, count_bit, sums)


def sum_bit(bit, x):
    total = 0
    while x != 0:
        total += bit[x]
        x &= x - 1
    return total


def update_bit(bit, pos, delta):
    while pos < len(bit):
        bit[pos] += delta
        pos += pos & -pos


def sum_i_j(bit, i, j):
    i = max(0, i)
    j = min(MAX, j)
    if i >= j:
        return 0
    return sum_bit(bit, j) - sum_bit(bit, i)


"""
def ans(A, x, y, m):
    total = 0
    for a in A:
        c = 0
        if y - m - 1 < a <= x-1:
            c += y - x + 1
        if max(x-1, y-m) < a <= y-1:
            c += y - a
        if x-m-1 < a <= min(x-1, y - m) - 1:
            c += m - x + a + 1
        if x-2 < a <= y-m:
            c += m

        total += c


    return total

"""


def ans(x, y, m, bit, bit2):
    total = 0

    total += sum_i_j(bit, y - m, x - 2)*(y - x + 1)

    total += sum_i_j(bit, max(y - m, x - 1), y - 1)*y
    total -= sum_i_j(bit2, max(y - m, x - 1), y - 1)

    total += sum_i_j(bit, x - m - 1, min(y - m, x - 1) - 1) * (m - x + 1)
    total += sum_i_j(bit2, x - m - 1, min(y - m, x - 1) - 1)

    total += sum_i_j(bit, x - 2, y - m)*m
    return total

solve()
