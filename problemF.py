class Machine:
    def __init__(self, day, price, resale, profit_per_day):
        self.day = day
        self.price = price
        self.resale = resale
        self.profit_per_day = profit_per_day

    def profit_on_day(self, d):
        upfront_cost = self.price - self.resale
        return self.profit_per_day*(d - self.day - 1) - upfront_cost


class TestCase:
    @staticmethod
    def read():
        ans = TestCase()
        N, ans.C, ans.D = map(int, raw_input().split(" "))
        if (N, ans.C, ans.D) == (0, 0, 0):
            return None

        # Initialize machines with 2 sentinel machines
        ans.machines = [Machine(0, 0, 0, 0), Machine(ans.D+1, 0, 0, 0)]
        for i in range(N):
            Di, Pi, Ri, Gi = map(int, raw_input().split(" "))
            ans.machines.append(Machine(Di, Pi, Ri, Gi))
        return ans

    def max_profit(self):
        self.machines.sort(key=lambda x: x.day)
        self.cache = [-1 for _ in xrange(len(self.machines))]
        return self.max_ending_here(len(self.machines) - 1)

    def max_ending_here(self, i):
        """
        Return the maximum possible total capital before day Di starts
        """
        if i == 0:
            return self.C

        if self.cache[i] != -1:
            return self.cache[i]

        today = self.machines[i].day
        maximum = 0

        # Loop on every possible value for current machine
        for j in xrange(0, i):
            m = self.max_ending_here(j)
            if m >= self.machines[j].price:
                maximum = max(m + self.machines[j].profit_on_day(today),
                              maximum)

        self.cache[i] = maximum
        return maximum


def main():
    case = 1
    while True:
        tc = TestCase.read()
        if tc is None:
            break
        print "Case %i: %i" % (case, tc.max_profit())
        case += 1

if __name__ == "__main__":
    main()
