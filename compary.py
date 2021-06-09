#!/usr/bin/env python3

# Get necessary file information using os.stat()

import os, sys, re
from os import linesep
import time
import csv
import pandas as pd
import numpy

delimiter = linesep.encode("ascii")

file_details = {}

# Get file info: name, size, row count,
file_name = sys.argv[1]
# print(file_name)
file_details["file_name"] = file_name

file_size = os.path.getsize(file_name)
# print(file_size)
file_details["file_size_bytes"] = file_size

file_row_count = len(open(file_name).readlines())
# print(file_row_count)
file_details["total_rows"] = file_row_count

suffixes = ["B", "KB", "MB", "GB", "TB", "PB"]


def sized(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.0
        i += 1
    f = ("%.2f" % nbytes).rstrip("0").rstrip(".")
    return "%s %s" % (f, suffixes[i])


file_details["file_size_more"] = str(sized(file_size))


def manifest():
    with open("manifest.csv", "w") as csvfile:
        csv_writer = csv.DictWriter(
            csvfile,
            fieldnames=["file_name", "total_rows", "file_size_bytes", "file_size_more"],
        )
        csv_writer.writeheader()
        csv_writer.writerow(file_details)


manifest()

os.system("head -n 5 manifest.csv")

os.system("rm missing.txt")


def compare(file_to_compare, search_string):
    if len(search_string) > 0:
        search_string = search_string[:]
        with open(file_to_compare, "r") as sf:
            bucket = sf.read()
            res = bucket.find(search_string)
            if res == -1:

                with open("missing.txt", "a") as mis:
                    mis.writelines(search_string)


filepath = file_name

second_file = sys.argv[2]
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #    print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1
        compare(second_file, line)
