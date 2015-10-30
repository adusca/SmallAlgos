# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve():
    n, m, q = map(int, raw_input().strip().split(' '))
    A = map(int, raw_input().strip().split(' '))
    for i in xrange(q):
        t, x, y = map(int, raw_input().strip().split(' '))
        if t == 1:
            A[x] = y
        if t == 2:
            print ans(A, x, y, m)


def ans(A, x, y, m):
    total = 0
    for a in A:
        menor = x - a
        maior = y - a
        c = min(maior, m) - max(1, menor)
        if c > 0:
            total += c
    return total

solve()
