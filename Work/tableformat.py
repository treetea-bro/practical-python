class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for h in rowdata:
            print(f"<td>{h}</td>", end="")
        print("</tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt) -> TableFormatter:
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
    formatter.headings(cols)
    for stock in stocks:
        row = []
        for col in cols:
            row.append(getattr(stock, col))
        formatter.row(row)
