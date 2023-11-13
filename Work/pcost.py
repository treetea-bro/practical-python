# pcost.py
#
# Exercise 1.27
import csv
import sys
from stock import Stock


def portfolio_cost(iterable):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    rows = csv.reader(iterable)
    headers = next(rows)
    types = [str, int, float]
    for row in rows:
        name, shares, price = (func(el) for func, el in zip(types, row))
        s = Stock(name=name, shares=shares, price=price)
        total_cost += s.shares * s.price
    return total_cost


def main(filename):
    with open(filename, "rt") as f:
        cost = portfolio_cost(f)
    print("Total cost:", cost)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"
    main(filename)
