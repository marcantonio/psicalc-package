class NmiCache:
    """
    Memoize NMI lookups
    """

    def __init__(self, f):
        self.cache = dict()
        self.nmi_func = f

    def get(self, a, b, msa):
        # Uncommenting this is a big perf gain. However, due to asymmetries in the nmi
        # calculation (caused by floating point inconsistencies) there are sometimes large
        # differences that lead to issues. For example, in the hist test data, (127, 128)
        # == 0 but (128, 127) = 1.0.
        #(a, b) = sorted([a, b])

        if a in self.cache:
            if b not in self.cache[a]:
                self.cache[a][b] = self.nmi_func(msa[:, a], msa[:, b])

                v = self.nmi_func(msa[:, b], msa[:, a])
                if v != self.cache[a][b]:
                    if v >= 1.0 or self.cache[a][b] >= 1.0:
                        print("HERE")
                    print(msa[:, a])
                    print(msa[:, b])
                    print(f"({a}, {b}): {self.cache[a][b]}")
                    print(f"({b}, {a}): {v}")
        else:
            self.cache[a] = {b: self.nmi_func(msa[:, a], msa[:, b])}

        return self.cache[a][b]

    def clear(self):
        self.cache = dict()
