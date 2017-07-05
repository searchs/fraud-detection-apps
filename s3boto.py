from boto.s3.connection import S3Connection

conn = S3Connection('your-access-key','your-secret-key')  #NEVER add your key in the code.   12 Factor!
bucket = conn.get_bucket('bucket')
for key in bucket.list():
    try:
        res = key.get_contents_to_filename(key.name)
    except:
        logging.info(key.name+":"+"FAILED")
