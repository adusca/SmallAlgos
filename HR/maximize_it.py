import bisect
import itertools

K, M = map(int, raw_input().split(" "))
lists = [[int(x)**2 for x in raw_input().split(" ")[1:]] for _ in xrange(K)]

if K == 1:
    lists.append([0])

K2 = K/2
all_sums = set()
for tup in itertools.product(*lists[0:K2]):
    all_sums.add(sum(tup) % M)
sum_list = sorted(list(all_sums))

ans = -1
for tup in itertools.product(*lists[K2:]):
    cur_sum = sum(tup) % M
    pos = bisect.bisect(sum_list, M - 1 - cur_sum)
    ans = max(ans,
              (cur_sum + sum_list[pos-1]) % M,
              (cur_sum + sum_list[-1]) % M)

sum_list[0:pos]

print ans
