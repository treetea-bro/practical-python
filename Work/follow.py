import os
import time


def follow(file_name):
    f = open(file_name)
    f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file

    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)  # Sleep briefly and retry
            continue
        yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == "__main__":
    import csv

    lines = follow("Data/stocklog.csv")
    rows = csv.reader(lines)
    ibm = filematch(lines, "IBM")
    for line in ibm:
        print(line)
