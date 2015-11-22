n = input()
G = {(0, 0, 0): []}

memo = {}

for i in xrange(n):
    x, y, w = map(int, raw_input().strip().split(' '))
    G[(x, y, w)] = []
    for xi, yi, wi in G.keys():
        if xi == x and yi == y:
            continue
        if xi <= x and yi <= y:
            G[(xi, yi, wi)].append((x, y, w))
        elif x <= xi and y <= yi:
            G[(x, y, w)].append((xi, yi, wi))

ordered = sorted(G.keys(), reverse=True)
for x, y, w in ordered:
    ans = w
    for xi, yi, wi in G[(x, y, w)]:
        ans = max(ans, w + memo[xi, yi])
    memo[x, y] = ans

print memo[0, 0]
