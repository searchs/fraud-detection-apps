#!/usr/bin/env python3

# Important info:  Apache Spark MUST be available on machine (Jenkins Slave)

import os
import sys
from stat import *
from datetime import datetime 

os.system("pip3 install -r requirements.txt --user")

import findspark
findspark.init()

import pyspark
from pyspark import SparkContext, SparkConf, SparkFiles

run_date = datetime.today().strftime('%Y%m%d')

primary = sys.argv[1]
secondary = sys.argv[2]

def spark_details(SparkContext):
    localsc = SparkContext
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
    
'''
Compares 2 extract files contents
'''
def main():
    conf = (SparkConf()
                .setMaster("local[*]")
                .setAppName("compare_engine"))

    sc = SparkContext(conf = conf)
    sc.setLogLevel('INFO')

    raw_primary = sc.textFile(primary, minPartitions=4, use_unicode=False).distinct()   
    raw_primary.partitionBy(8).cache()
    raw_secondary = sc.textFile(secondary, minPartitions=4, use_unicode=False).distinct()
    raw_secondary.partitionBy(8).cache()

    print(raw_primary.getNumPartitions())
    primary_count = raw_primary.count()
    print("DEBUG: Primary Count:__", primary_count)

    secondary_count = raw_secondary.count()
    print("DEBUG: Secondary Count:__",secondary_count)

    # Return each Primary file line/record not contained in Secondary
    not_in_primary  = raw_primary.subtract(raw_secondary)
    print("Subtraction Partion Count:__", not_in_primary.count())
    
    os.system('rm -Rf collects_*.csv')
    not_in_primary.coalesce(1, True).saveAsTextFile('collects_{}_1.csv'.format(run_date))

    os.system('cat collects_{}_1.csv/part-0000* > collects_{}_report.csv'.format(run_date, run_date))
    os.system('wc -l collects_{}_report.csv'.format(run_date))

    # Flip Primary Vs Secondary
     # Return each Secondary file line/record not contained in Primary
    not_in_secondary  = raw_secondary.subtract(raw_primary)
    not_in_primary.coalesce(1,True).saveAsTextFile('collects_{}_2.csv'.format(run_date))

    # DEBUG INFO ONLY # spark_details(sc)
    sc.stop()
    # DEBUG INFO: File Data - primary_stats = os.stat(primary) - secondary_stats = os.stat(secondary)

if __name__ == "__main__":
    main()
