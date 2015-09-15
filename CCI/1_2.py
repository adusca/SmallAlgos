#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_permutation(s, t):
    """
    input: 2 strings
    output: a boolean indicating if one string is a permutation of the other
    time complexity: O(n log n)
    space complexity O(n)
    """
    if len(s) != len(t):  # O(len(s) + len(t))
        return False

    return sorted(s) == sorted(t)  # O(len(s)*log(len(s)))


def is_permutation_ascii(s, t):
    """
    input: 2 ascii strings
    output: a boolean indicating if one string is a permutation of the other
    time complexity: O(n)
    space complexity O(1)
    """
    if len(s) != len(t):  # O(len(s) + len(t))
        return False

    chars_in_s = [0 for _ in range(128)]
    chars_in_t = [0 for _ in range(128)]

    for i in range(len(s)):
        chars_in_s[ord(s[i])] += 1
        chars_in_t[ord(t[i])] += 1

    return chars_in_s == chars_in_t


def test_is_permutation():
    assert is_permutation('não', 'pois') is False
    assert is_permutation('mão', 'ãom') is True
    assert is_permutation('', '') is True
    assert is_permutation('', 'casa') is False


def test_is_permutation_ascii():
    assert is_permutation_ascii('', '') is True
    assert is_permutation_ascii('', 'a') is False
    assert is_permutation_ascii('cat', 'tac') is True
    assert is_permutation_ascii('aabbccdd', 'ababdcdd') is False

test_is_permutation()
test_is_permutation_ascii()
