import sys

dp = [0x3f3f3f3f for _ in xrange(100001)]
dp[0] = 0

factorials = [1]
for i in xrange(2, 9):
    factorials.append(factorials[-1] * i)

for N in sys.stdin.readlines():
    N = int(N)
    count = 0

    for i in xrange(7, -1, -1):
        count += N/factorials[i]
        N %= factorials[i]

    print count
