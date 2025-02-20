from pyspark.sql import DataFrame
from pyspark.rdd import RDD

from loguru import logger as Logger


def get_partition_info(df: DataFrame, logger: Logger) -> None:
    """
    Get partition info to easily determine optimal partition count for  repartition/coalesce
    :param df:
    :param logger:
    :return: None.  Prints the results to the console
    """
    import statistics

    def process_marker(logger: Logger, msg: str) -> None:
        logger.info("\n" + "==" * 15 + msg + "==" * 15 + "\n")

    def get_partition_len(iterator):
        yield sum(1 for _ in iterator)

    rdd: RDD = df.rdd

    count = rdd.getNumPartitions()
    lengths = rdd.mapPartitions(get_partition_len, True).collect()

    logger.info(f"{count} partition(s) total.")
    process_marker(logger, message="PARTITION SIZE STATS")
    logger.info(f"\tmin: {min(lengths)}")
    logger.info(f"\tmax: {max(lengths)}")
    logger.info(f"\tavg: {sum(lengths) / len(lengths)}")
    logger.info(f"\tstddev: {statistics.stdev(lengths)}")

    logger.info("\tdetailed info")
    for i, pl in enumerate(lengths):
        logger.info(f"{i}. {pl}")
