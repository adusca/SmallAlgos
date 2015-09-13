def max_profit(machines, C, D):
    pass


def get_next_day(machines, d):
    pass


def max_starting_here(machines, i, d, C, D):
    """
    Return the maximum possible profit after day d, considering you
    begin with machine i, C capital.
    """
    next_day = get_next_day(machines, d)
    profit_until_sale = machines[i][3]*(next_day - d - 1)
    buy = machines[i][2] - machines[i + 1][1] + max_starting_here(
        machines, i + 1, next_day,
        C + machines[i][2] - machines[i + 1][1] + profit_until_sale, D)
    stay = max_starting_here(machines, i, next_day, C + profit_until_sale, D)
    return max(buy, stay)

# Reading input and printing output
while True:
    C, N, D = map(int, raw_input().split(" "))
    if (C, N, D) == (0, 0, 0):
        break
    machines = []
    for i in range(N):
        Di, Pi, Ri, Gi = map(int, raw_input.split(" "))
        machines.append((Di, Pi, Ri, Gi))
    print "Case %i: %i" % (i + 1, max_profit(machines, C, D))
