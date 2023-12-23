#!/usr/bin/env python3
from __future__ import print_function

import os
import sys
from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta as td
import json
from collections import OrderedDict
import ast
from loguru import logger

from pyspark import SparkContext, SparkConf, SparkFiles

# os.system("pip3 install -r requirements.txt --user")

run_date = (dt.now(tz=tz.utc) - td(days=1)).strftime("%Y%m%d")

primary = sys.argv[1]
secondary = sys.argv[2]

primary_report = {}
secondary_report = {}
process_report = {}


def spark_details(SparkContext):
    localsc = SparkContext
    logger.info("=" * 100 + "\n")
    logger.info(localsc.version)
    logger.info(localsc.pythonVer)
    logger.info(localsc.master)
    logger.info(str(localsc.sparkHome))
    logger.info(str(localsc.sparkUser()))
    logger.info(localsc.appName)
    logger.info(localsc.applicationId)
    logger.info(localsc.defaultParallelism)
    logger.info(localsc.defaultMinPartitions)
    logger.info("End of Spark ENV Details.")
    logger.info("=" * 100 + "\n")


def sort_each_message(raw_json_str):
    obj = dict(ast.literal_eval(f"{raw_json_str}"))
    listed = raw_json_str.iteritems
    # zip(d.keys(), d.values())
    logger.info(obj)
    logger.info(listed.items())
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

    rdd_secondary = sc.textFile(
        secondary, minPartitions=4, use_unicode=True
    ).distinct()
    rdd_secondary.partitionBy(10).cache()

    primary_count = rdd_primary.count()
    primary_report["count"] = primary_count
    logger.info(primary_report)

    secondary_count = rdd_secondary.count()
    secondary_report["count"] = secondary_count
    logger.info(secondary_report)

    # Return each Primary file line/record not contained in Secondary
    not_in_primary = rdd_primary.subtract(rdd_secondary)
    primary_diff = not_in_primary.count()
    primary_report["diff"] = primary_diff

    os.system("rm -Rf collects_*.csv")

    primary_dir = f"collects_{run_date}_primary"
    primary_report_name = f"collects_{run_date}_primary_report.csv"

    not_in_primary.coalesce(1, True).saveAsTextFile(primary_dir)

    # os.system('cat collects_{}_primary/part-0000* >> collects_{}_primary_report.csv'.format(run_date, run_date))
    os.system(f"cat {primary_dir}/part-0000* >> {primary_report_name}")
    os.system(f"wc -l collects_{run_date}_primary_report.csv")

    # Flip Primary Vs Secondary
    # Return each Secondary file line/record not contained in Primary
    not_in_secondary = rdd_secondary.subtract(rdd_primary)
    secondary_diff = not_in_secondary.count()
    secondary_report["diff"] = secondary_diff

    not_in_secondary.coalesce(1, True).saveAsTextFile(
        f"collects_{run_date}_secondary"
    )
    os.system(
        f"cat collects_{run_date}_secondary/part-0000* >> collects_{run_date}_secondary_report.csv"
    )
    os.system(f"wc -l collects_{run_date}_secondary_report.csv")

    process_report["primary"] = primary_report
    process_report["secondary"] = secondary_report

    logger.info("=" * 100 + "\n")
    logger.info(process_report)
    logger.info("=" * 100 + "\n")
    spark_details(sc)

    sc.stop()


if __name__ == "__main__":
    main()
