class Bit:

    """
    Data Structure to compute a function over an interval arr[:x] in
    log(n) time, that can be updated (to f(arr[pos], delta)) in
    log(n) time.  function requirements:
    - commutativity
    - identity element
    - associativity
    """
    def __init__(self, function, identity, size):
        self.f = function
        self.bit = [identity for _ in xrange(size + 1)]
        self.identity = identity

    def compute(self, x):
        """Compute f(x) over the interval (0:x]"""
        # bit[x] = f((sem_menos_significativo(x), x])
        # 0 1 2 ... x_atual ... x
        #           (           ]
        #      (    ]
        #      (                ]
        #   (  ]
        total = self.identity
        while x != 0:
            total = self.f(self.bit[x], total)
            x &= x - 1

        return total

    def update(self, pos, delta):
        # arr[x] = self.f(arr[x], delta)
        while pos < len(self.bit):
            self.bit[pos] = self.f(self.bit[pos], delta)
            pos += pos & -pos
