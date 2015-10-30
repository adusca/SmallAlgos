import heapq


def solve():
    pearls = range(1, 2000000)
    total = 0
    heapq.heapify(pearls)
    while len(pearls) > 1:
        a = heapq.heappop(pearls)
        b = heapq.heappop(pearls)
        c = (a + b) % 1000000007
        total = (total + c) % 1000000007
        heapq.heappush(pearls, c)
    return total

print solve()
