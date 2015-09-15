def is_rotation(s, t):
    """
    input: 2 strings
    output: a boolean indicating if one string is a rotation of the other
    """
    if len(s) != len(t):
        return False
    return is_substring(s, t + t)


def is_substring(s, t):
    """
    input: 2 strings

    output: a boolean indicating if the first string is a substring of
    the second
    """
    return s in t


def test_is_rotation():
    assert is_rotation('pandas', 'aspand') is True
    assert is_rotation('pandas', 'sadnap') is False

test_is_rotation()
