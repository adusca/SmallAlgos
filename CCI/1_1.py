def are_all_characters_unique(s):
    """
    input: an ASCII string s
    output: a boolean indicating if all characters on the s
    are unique
    time complexity: O(1)
    space complexity: O(1)
    """
    # If s has more then 128 characters, we can immediately return False
    if len(s) > 128:  # O(1)
        return False

    chars = [0 for _ in range(128)]
    for c in s:  # at most 128 O(1) operations
        chars[ord(c)] += 1
        if chars[ord(c)] > 1:
            return False

    return True


def test_are_all_characters_unique():
    assert are_all_characters_unique("banana") is False
    assert are_all_characters_unique("") is True
    assert are_all_characters_unique("asdfghjkl;") is True

test_are_all_characters_unique()
