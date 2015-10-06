def mtc(s, x, a, b, c):
    # assuming x > s
    d = min(a + b, c)  # Real replace cost
    total = 0
    to_insert = len(x) - len(s)
    replace_buffer = 0
    char_s = get_chars(s)
    char_x = get_chars(x)
    for i in xrange(26):
        j = char_s[i] - char_x[i]
        while j < 0:
            if to_insert == 0 and replace_buffer == 0:
                total += d
                replace_buffer += 1

            elif to_insert != 0:
                to_insert -= 1
                total += b

            else:
                replace_buffer -= 1
            j += 1
        while j > 0:
            if replace_buffer == 0:
                total += d
                replace_buffer += 1
            else:


    return total


def get_chars(s):
    chars = [0 for _ in xrange(26)]
    for c in s:
        chars[ord(c) - ord('a')] += 1
    return chars
