# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    filename,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records
    """

    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(filename, delimiter=delimiter)

    if has_headers:
        headers = next(rows)
    else:
        select = None

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for i, row in enumerate(rows, start=1):
        if not row:
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {e}")
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
