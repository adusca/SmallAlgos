n = input()
nxt = []
probs = []
for i in range(n):
    a, p = map(int, raw_input().split(' '))
    nxt.append(a - 1)
    probs.append(0.01*p)


def dfs(v, global_seen):
    cycle = set()
    seen = set()
    while v not in global_seen:
        seen.add(v)
        global_seen.add(v)
        v = nxt[v]
    if v not in seen:
        return set()
    while v not in cycle:
        cycle.add(v)
        v = nxt[v]
    return cycle

global_seen = set()
cycles = []
for i in range(len(nxt)):
    if i not in global_seen:
        c = dfs(i, global_seen)
        cycles.append(c)


def get_cycle_prob(cycle):
    ans = 1
    if len(cycle) == 0:
        return 0
    for v in cycle:
        ans *= probs[v]
    return ans

ans = 0
for cycle in cycles:
    ans += get_cycle_prob(cycle)

print round(ans, 2)
