# report.py
#
# Exercise 2.4

import csv
from tableformat import TableFormatter, create_formatter
from typing import Iterable, Iterator
from portfolio import Portfolio


def read_portfolio(filename: str, **opts) -> Portfolio:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        return Portfolio.from_csv(lines)


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


def make_report(
    portfolio: Portfolio, prices: dict
) -> Iterator[tuple[str, int, float, float]]:
    for row in portfolio:
        if row.name in prices:
            yield (
                row.name,
                row.shares,
                prices[row.name],
                round(prices[row.name] - row.price, 2),
            )


def print_report(
    reportdata: Iterable[tuple[str, int, float, float]],
    cols: Iterable[str],
    formatter: TableFormatter,
) -> None:
    formatter.headings(cols)
    for rowdatas in reportdata:
        formatter.row(r for r in rowdatas)


def portfolio_report(portfolio_filename: str, prices_filename: str, fmt: str) -> None:
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = create_formatter(fmt)
    print_report(report, ["Name", "Shares", "Price", "Change"], formatter)


def main(
    portfolio_filename: str = "Data/portfolio.csv",
    prices_filename: str = "Data/prices.csv",
    fmt: str = "txt",
):
    portfolio_report(portfolio_filename, prices_filename, fmt)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        main(*sys.argv[1:])
    else:
        main()
