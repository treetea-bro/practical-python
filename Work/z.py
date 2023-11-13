class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    # Used with `repr()`
    def __repr__(self):
        return f"Date({self.year},{self.month},{self.day})"


d = Date(2012, 12, 21)
print(d)
print(repr(d))
