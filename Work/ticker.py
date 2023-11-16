from follow import follow
import csv
import report
import tableformat


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield (func(val) for func, val in zip(types, row))


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfile, logfile, fmt):
    producer = follow(logfile)
    rows = parse_stock_data(producer)
    portfolio = report.read_portfolio(portfile)
    rows = (row.values() for row in rows if row["name"] in portfolio)
    s = tableformat.create_formatter(fmt)
    report.print_report(rows, ["name", "price", "change"], s)


if __name__ == "__main__":
    ticker("Data/portfolio.csv", "Data/stocklog.csv", "txt")
