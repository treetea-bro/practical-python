class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

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
    s = MyStock('GOOG', 100, 490.1)
    print(s.cost())