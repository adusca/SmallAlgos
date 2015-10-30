def build_s():
    s = [1, 2, 2]
    count_one = [0, 1, 1, 1]

    for index in xrange(2, 10**5):
        c = 3 - s[-1]
        for i in range(s[index]):
            s.append(c)
            count_one.append(count_one[-1] + (2 - c))
    return count_one
