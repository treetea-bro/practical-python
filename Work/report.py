# report.py
#
# Exercise 2.4

import csv
import tableformat


def read_portfolio(iterable):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []

    rows = csv.reader(iterable)
    headers = next(rows)
    for row in rows:
        record = dict(zip(headers, row))
        stock = {
            "name": record["name"],
            "shares": int(record["shares"]),
            "price": float(record["price"]),
        }
        portfolio.append(stock)
    return portfolio


def read_prices(iterable):
    dic = {}
    rows = csv.reader(iterable)
    for i, row in enumerate(rows, start=1):
        try:
            dic[row[0]] = float(row[1])
        except:
            pass
    return dic


def make_report(portfolio, prices):
    for row in portfolio:
        if row["name"] in prices:
            yield (
                row["name"],
                row["shares"],
                prices[row["name"]],
                round(prices[row["name"]] - row["price"], 2),
            )


def print_report(reportdata, formatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt):
    with open(portfolio_filename) as f:
        portfolio = read_portfolio(f)
    with open(prices_filename) as f:
        prices = read_prices(f)
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
