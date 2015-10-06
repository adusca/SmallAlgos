from fractions import Fraction
from collections import defaultdict


def palin_substr(s):
    prefix_dict = defaultdict(int)
    chars = 0
    prefix_dict[0] = 1

    ans = 0
    for c in s:
        i = ord(c) - ord('a')
        chars ^= (1 << i)

        ans += prefix_dict.get(chars, 0)
        for i in xrange(26):
            tmp = chars ^ (1 << i)
            ans += prefix_dict.get(tmp, 0)

        prefix_dict[chars] += 1

    return ans

def pretty_prob(a, b):
    p = Fraction(a, b)
    return str(p.numerator) + '/' + str(p.denominator)

def compute_prob(string):
    n = len(string)
    m = (n*(n+1))/2
    return pretty_prob(palin_substr(string), m)

n = input()
for s in xrange(n):
    print compute_prob(raw_input().strip())
