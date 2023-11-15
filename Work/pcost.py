# pcost.py
#
# Exercise 1.27
import sys
import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(filename):
    cost = portfolio_cost(filename)
    print("Total cost:", cost)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"
    main(filename)
