import collections


def sum_prod(a, b, c):
    return (a+b+c, a*b*c)


def not_all_different(lst):
    for tpl in lst:
        if len(set(tpl)) != 3:
            return True
    return False


ages_tuples = collections.defaultdict(list)

for i in range(1, 19):
    for j in range(i, 19):
        for k in range(j, 19):
            sum_and_prod = sum_prod(i, j, k)
            ages_tuples[sum_and_prod].append((i, j, k))


for key, values in ages_tuples.iteritems():
    if len(values) > 1 and not_all_different(values) and key[1] > 72:
        print key, ":", values
