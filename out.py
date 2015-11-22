MAX = 1499
print MAX, MAX*MAX

cnt1, cnt2 = 0, 0
out = [[], []]

for i in xrange(1, MAX+1):
    for j in xrange(1, MAX+1):
        if j % 2 == 0 or (i == 1 and j % 4 == 1) or (i == MAX and j % 4 == 3):
            out[0].append((i, j))
        else:
            out[1].append((i, j))

for (i1, j1), (i2, j2) in zip(out[0], out[1]):
    print i1, j1
    print i2, j2

print out[0][-1][0], out[0][-1][1]
