class Stock:
    __slots__ = ("name", "_shares", "price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        self.shares -= num
        return self.shares


class MyStock(Stock):
    def cost(self):
        # Check the call to `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost


if __name__ == "__main__":
    goog = Stock("GOOG", 100, 490.1)
    print(repr(goog))
