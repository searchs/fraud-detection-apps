#!/usr/bin/env python3
from __future__ import print_function

import os
import sys
from datetime import datetime, timedelta
import json
from collections import OrderedDict
import ast

import findspark

os.system("pip3 install -r requirements.txt --user")
findspark.init()

import pyspark
from pyspark import SparkContext, SparkConf, SparkFiles

run_date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")

primary = sys.argv[1]
secondary = sys.argv[2]

primary_report = {}
secondary_report = {}
process_report = {}


def spark_details(SparkContext):
    localsc = SparkContext
    print("=" * 100)
    print("\n")
    print(localsc.version)
    print(localsc.pythonVer)
    print(localsc.master)
    print(str(localsc.sparkHome))
    print(str(localsc.sparkUser()))
    print(localsc.appName)
    print(localsc.applicationId)
    print(localsc.defaultParallelism)
    print(localsc.defaultMinPartitions)
    print("End of Spark ENV Details.")
    print("\n")
    print("=" * 100)
    print("\n")


def sort_each_message(raw_json_str):
    obj = dict(ast.literal_eval("{}".format(raw_json_str)))
    listed = raw_json_str.iteritems
    # zip(d.keys(), d.values())
    print(obj)
    print(listed.items())
    values = OrderedDict(listed)
    return json.dumps(values, sort_keys=True, indent=None, ensure_ascii=False)


"""
Compares 2 extract files contents
"""


def main():
    conf = SparkConf().setMaster("local[*]").setAppName("compare_engine")

    sc = SparkContext(conf=conf)
    sc.setLogLevel("INFO")

    sc.addFile(primary)

    # rdd_primary = sc.textFile(primary, minPartitions=4, use_unicode=True).distinct()
    rdd_primary = sc.textFile(
        SparkFiles.get(primary), minPartitions=4, use_unicode=True
    ).distinct()
    rdd_primary.partitionBy(10).cache()

    os.system("rm -Rf collects_*")
    os.system("rm -Rf holder.txt")

    rdd_secondary = sc.textFile(secondary, minPartitions=4, use_unicode=True).distinct()
    rdd_secondary.partitionBy(10).cache()

    primary_count = rdd_primary.count()
    primary_report["count"] = primary_count
    print(primary_report)

    secondary_count = rdd_secondary.count()
    secondary_report["count"] = secondary_count
    print(secondary_report)

    # Return each Primary file line/record not contained in Secondary
    not_in_primary = rdd_primary.subtract(rdd_secondary)
    primary_diff = not_in_primary.count()
    primary_report["diff"] = primary_diff

    os.system("rm -Rf collects_*.csv")

    primary_dir = "collects_{}_primary".format(run_date)
    primary_report_name = "collects_{}_primary_report.csv".format(run_date)

    not_in_primary.coalesce(1, True).saveAsTextFile(primary_dir)

    # os.system('cat collects_{}_primary/part-0000* >> collects_{}_primary_report.csv'.format(run_date, run_date))
    os.system("cat {}/part-0000* >> {}".format(primary_dir, primary_report_name))
    os.system("wc -l collects_{}_primary_report.csv".format(run_date))

    # Flip Primary Vs Secondary
    # Return each Secondary file line/record not contained in Primary
    not_in_secondary = rdd_secondary.subtract(rdd_primary)
    secondary_diff = not_in_secondary.count()
    secondary_report["diff"] = secondary_diff

    not_in_secondary.coalesce(1, True).saveAsTextFile(
        "collects_{}_secondary".format(run_date)
    )
    os.system(
        "cat collects_{}_secondary/part-0000* >> collects_{}_secondary_report.csv".format(
            run_date, run_date
        )
    )
    os.system("wc -l collects_{}_secondary_report.csv".format(run_date))

    process_report["primary"] = primary_report
    process_report["secondary"] = secondary_report

    print("=" * 100)
    print("\n")
    print(process_report)
    print("\n")
    print("=" * 100)
    spark_details(sc)

    sc.stop()


if __name__ == "__main__":
    main()
