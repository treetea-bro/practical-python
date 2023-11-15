# report.py
#
# Exercise 2.4

import csv
import tableformat
from stock import Stock
from typing import List
import fileparse
from portfolio import Portfolio


def read_portfolio(filename: str) -> Portfolio:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as file:
        portdicts = fileparse.parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float]
        )

    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    return Portfolio(portfolio)


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


def print_report(reportdata, cols, formatter):
    formatter.headings(cols)
    for rowdata in reportdata:
        # rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata[col] for col in cols)


def portfolio_report(portfolio_filename, prices_filename, fmt):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, ["Name", "Shares", "Price", "Change"], formatter)


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
