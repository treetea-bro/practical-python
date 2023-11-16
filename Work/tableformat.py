from typing import Iterable


class TableFormatter:
    def headings(self, headers: Iterable[str]) -> None:
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata: Iterable[str]) -> None:
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers: Iterable[str]) -> None:
        for h in headers:
            print(f"{h:>10}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata: Iterable[str]) -> None:
        for d in rowdata:
            print(f"{d:>10}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers: Iterable[str]) -> None:
        print(",".join(headers))

    def row(self, rowdata: Iterable[str]) -> None:
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers: Iterable[str]) -> None:
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>")

    def row(self, rowdata: Iterable[str]) -> None:
        print("<tr>", end="")
        for h in rowdata:
            print(f"<td>{h}</td>", end="")
        print("</tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt: str) -> TableFormatter:
    match fmt:
        case "txt":
            return TextTableFormatter()
        case "csv":
            return CSVTableFormatter()
        case "html":
            return HTMLTableFormatter()
        case _:
            raise FormatError(f"Unkown table format {fmt}")


def print_table(stocks, cols, formatter: TableFormatter):
    """
    Make a nicely formatted table from a list of objects and attribute names.
    """
    formatter.headings(cols)
    for stock in stocks:
        rowdata = (str(getattr(stock, col)) for col in cols)
        formatter.row(rowdata)
