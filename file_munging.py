#!/usr/bin/env python3

# Get necessary file information using os.stat()

import os, sys
import stat  
import time
import csv
import pandas as pd

file_name = sys.argv[1]

file_stats = os.stat(file_name)
print(stat.S_ENFMT)
print(file_stats)
# print(type(file_stats))

# print(file_stats)
# create a file to hold file info
file_info = {
   'file_name': file_name,
   'file_size': file_stats [stat.ST_SIZE],
   'f_lm': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
   'f_la': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_ATIME])),
   'f_ct': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
}

# df = pd.DataFrame(file_info.items())
# file_info = dict(file_info)
# print(file_n)
# df = pd.DataFrame.from_dict(file_info.items(), orient='columns', dtype=None)
# df = pd.DataFrame.from_dict(file_info.items())
# print(df.info())
# print(file_info)

# def directory_check(filename_passed,file_stats):
#     if stat.S_ISDIR(file_stats[stat.ST_MODE]):
#         exit
#     else:
#         return

# def generate_manifest(manifest_name, file_stats):
#     directory_check(file_name, file_stats)
#     headers = list(file_stats.keys())

#     with open(manifest_name, 'w', newline='') as csvfile:
#         fieldnames = headers
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         writer.writerow(file_stats.values())

#     # with open(manifest_name, 'w+') as report:
#     #     report.writelines(file_info.keys())
#     #     report.writelines(str(file_info.values()))

# generate_manifest('legacy.csv', file_stats)
