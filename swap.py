def is_possible(a, b):
    if not a.count('1') == b.count('1'):
        return False
    return a.count('0') == b.count('0')


def difference(a, b):
    ans = 0
    for i in xrange(len(a)):
        if a[i] != b[i]:
            ans += 1
    return ans


def count_swap(a, b):
    if len(a) != len(b):
        return -1
    if not is_possible(a, b):
        return -1
    return difference(a, b)/2

a = raw_input()
b = raw_input()

print count_swap(a, b)
