def has_a_palindrome_permutation(s):
    """
    input: an ascii string s
    output: a boolean indicating if s has a palindrome permutation
    """
    s = s.replace(' ', '')  # Spaces don't matter
    chars = [0 for _ in range(128)]
    for c in s:
        chars[ord(c)] = (chars[ord(c)] + 1) % 2

    odd_number = filter(lambda x: x == 1, chars)
    if len(s) % 2 == 0:
        return len(odd_number) == 0
    else:
        return len(odd_number) == 1


def test_has_a_palindrome_permutation():
    assert has_a_palindrome_permutation('house') is False
    assert has_a_palindrome_permutation('taco cat') is True
