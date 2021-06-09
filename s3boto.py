from boto.s3.connection import S3Connection

conn = S3Connection(
    "your-access-key", "your-secret-key"
)  # NEVER add your key in the code.   12 Factor!
bucket = conn.get_bucket("bucket")
for key in bucket.list():
    try:
        res = key.get_contents_to_filename(key.name)
    except:
        logging.info(key.name + ":" + "FAILED")

        # TODO: DELETE Test files in Bucket
# TODO: get manifest file first

# boto3.setup_default_session(profile_name=AWS_PROFILE)

# s3 = boto3.resource('s3')
# bucket = s3.Bucket(S3_BUCKET)
# bucket.objects.filter(Prefix="reports/adhoc/report").delete()

# client = boto3.client('s3')
# client.delete_object(Bucket=S3_BUCKET,Key='reports/adhoc/report/2016/12/05/formatted_report_20161205')
# client.delete_object(Bucket=S3_BUCKET,Key='reports/adhoc/report/2016/11/15/formatted_report_20161105')
# client.delete_object(Bucket=S3_BUCKET,Key='reports/adhoc/report/2016/11/15/formatted_report_20161115.csv')
# client.delete_object(Bucket=S3_BUCKET,Key='reports/adhoc/report/2016/11/16/formatted_report_20161115.csv')
print("Delete done!")
