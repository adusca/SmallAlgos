class Machine:
    def __init__(self, day, price, resale, profit_per_day):
        self.day = day
        self.price = price
        self.resale = resale
        self.profit_per_day = profit_per_day


def max_profit(machines, C, D):
    machines.sort(key=lambda x: x.day)
    return max_starting_here(machines, 0, C, D)


def max_starting_here(machines, i, C, D):
    """
    Return the maximum possible profit after day dj, considering you
    begin with machine i, C capital.
    """
    maximum = 0

    # Loop in all possibilities for next purchase
    for j in xrange(i + 1, len(machines)):
        profit_until_sale = machines[i].profit_per_day*(machines[j].day - machines[i].day - 1)
        capital_after_swap = C + machines[i].resale + profit_until_sale - machines[j].price
        if capital_after_swap >= 0:
            maximum = max(maximum, max_starting_here(
                machines, j,
                capital_after_swap, D))

    return max(maximum, C + machines[i].profit_per_day*(D - machines[i].day) + machines[i].resale)


# Reading input and printing output
case = 1
while True:
    N, C, D = map(int, raw_input().split(" "))
    if (C, N, D) == (0, 0, 0):
        break
    # Initialize machines with a sentinel machine
    machines = [Machine(0, 0, 0, 0)]
    for i in range(N):
        Di, Pi, Ri, Gi = map(int, raw_input().split(" "))
        machines.append(Machine(Di, Pi, Ri, Gi))
    print "Case %i: %i" % (case, max_profit(machines, C, D))
    case += 1
