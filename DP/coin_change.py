def count_sums(n, arr):
    """
    input: a positive integer n and an array of distinct integers arr
    output: how many ways n can be written as the sum of elements in arr
    example: count_sums(5, [1, 3, 4]) = 6:
             1 + 1 + 1 + 1 + 1
             1 + 1 + 3
             1 + 3 + 1
             3 + 1 + 1
             1 + 4
             4 + 1
    """
    ans = [0]*(n + 1)
    ans[0] = 1
    for i in xrange(1, n + 1):
        ans[i] = sum(ans[i - num] for num in arr if num <= i)
    return ans[n]


def coin_change(n, coins):
    """
    input: a positive integer n and an array of distinct integers coins
    output: how many ways n can be written as the sum of elements in coins
    ignoring the order
    example: coin_change(5, [1, 3, 4]) = 3:
             1 + 1 + 1 + 1 + 1
             1 + 1 + 3
             1 + 4
    """
    ans = [0]*(n + 1)
    ans[0] = 1
    for j in xrange(len(coins) - 1, -1, -1):
        for i in xrange(1, n + 1):
            if i >= coins[j]:
                ans[i] += ans[i - coins[j]]
    return ans[n]


def coin_change_once(n, coins):
    """
    input: a positive integer n and an array of integers coins
    output: how many ways n can be written as the sum of elements in coins
    ignoring the order and using it element at most once
    example: coin_change_once(5, [1, 3, 4]) = 1:
             1 + 4
    """
    ans = [0]*(n + 1)
    ans[0] = 1
    for j in xrange(len(coins) - 1, -1, -1):
        for i in xrange(n, 0, -1):
            if i >= coins[j]:
                ans[i] += ans[i - coins[j]]
    return ans[n]


print count_sums(5, [1, 3, 4])
print coin_change(5, [1, 3, 4])
print coin_change_once(5, [1, 3, 4])
