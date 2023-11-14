# report.py
#
# Exercise 2.4

import csv
import tableformat
from stock import Stock
from typing import List


def read_portfolio(portfolio_filename: str) -> List[Stock]:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []
    with open(portfolio_filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            s = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(s)
    return portfolio


def read_prices(prices_filename: str) -> dict:
    dic = {}
    with open(prices_filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                dic[row[0]] = float(row[1])
            except:
                pass
    return dic


def make_report(portfolio: List[Stock], prices):
    for row in portfolio:
        if row.name in prices:
            yield (
                row.name,
                row.shares,
                prices[row.name],
                round(prices[row.name] - row.price, 2),
            )


def print_report(reportdata, formatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(
    portfolio_filename="Data/portfolio.csv",
    prices_filename="Data/prices.csv",
    fmt="txt",
):
    portfolio_report(portfolio_filename, prices_filename, fmt)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        main(*sys.argv[1:])
    else:
        main()
