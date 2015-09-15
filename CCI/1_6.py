def compress_string(s):
    if s == "":
        return ""

    ans = ""
    count = 1
    current = s[0]

    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            ans += current + str(count)
            current = s[i]
            count = 1

    ans += current + str(count)

    if len(ans) < len(s):
        return ans
    return s


def test_compress_string():
    assert compress_string('aabcccccaaa') == 'a2b1c5a3'
    assert compress_string('banana') == 'banana'
    assert compress_string("") == ""

test_compress_string()
