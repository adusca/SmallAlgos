def is_one_away(s, t):
    n = len(s)
    m = len(t)

    # If the length difference is larger then 1, we can return False
    if abs(n - m) > 1:
        return False

    # If one of the strings is empty and the other has one character,
    # we can return True, this avoids having to deal with the empty
    # string edge case latter
    elif n + m == 1:
        return True

    # If both strings have the same length, the edit distance will be
    # less then 1 if they have at most 1 different character
    if n == m:
        return is_one_replace_away(s, t)

    smaller, larger = sorted([s, t], key=len)
    for index, char in enumerate(smaller):
        if char != larger[index]:
            return smaller[index:] == larger[index+1:]

    # If we didn't return until now, this means the larger string is
    # the smaller string with one extra character, so we should return
    # True
    return True


def is_one_replace_away(s, t):
    assert len(s) == len(t)

    count_different = sum(1 for i in xrange(len(s)) if s[i] != t[i])
    return count_different < 2

print is_one_away('pale', 'ple')
print is_one_away('pale', 'pales')
print is_one_away('pale', 'bale')
print is_one_away('pale', 'bake')
