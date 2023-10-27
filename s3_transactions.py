import os
import boto3
from botocore import session
from botocore.client import Config

import pandas as pd
from loguru import logger
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
S3_BUCKET = os.getenv("s3_data_bucket")
AWS_ACCESS_KEY_ID = os.getenv("aws_access_key_id")
AWS_SECRET_ACCESS_KEY = os.getenv("aws_secret_access_key")


def get_boto_session() -> session:
    _session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    return _session


def read_s3_buckets(session: boto3.Session, bucket_name: str, logger: logger):
    s3 = boto3.resource(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    logger.info("AWS S3 operations")
    bucket = s3.Bucket(S3_BUCKET)

    for buck in bucket.objects.all():
        logger.info(f"\t{buck.bucket_name}")

    s3.Bucket(S3_BUCKET).upload_file("test.csv", "uploads/")
    logger.info("Upload complete!")
    logger.info(bucket.objects.all())


def read_s3_bucket_by_client(bucket_name=S3_BUCKET):
    ...


if __name__ == "__main__":
    read_s3_buckets(get_boto_session(), bucket_name=S3_BUCKET, logger=logger)
