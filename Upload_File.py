import boto
import boto.s3
import sys
from boto.s3.key import Key
from timeit import default_timer
#Credentials to access the AWS S3 bucket
AWS_ACCESS_KEY_ID = 'AKIAIVPX4M6XPLQXKKIQ'
AWS_SECRET_ACCESS_KEY = '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'
#accessing the bucket
my_bucket = AWS_ACCESS_KEY_ID.lower() + 'cloud93'
#Connect the bucket to upload the file
try:
	conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)
	print "Connection successful"
except:
	print "Connection failed"
#Calculate time taken to copy the fie to bucket
time1 = default_timer();
s3=boto.connect_s3()

bucket = conn.get_bucket("cloud93",validate=False)
key=bucket.new_key("UNPrecip.csv")
myFfile = "UNPrecip.csv"
print 'Copying %s file to Cloud93 bucket %s' % \
   (myFfile, my_bucket)
#Define percentage of completion
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

conn.commit()
key.set_contents_from_filename(myFfile,policy='public-read')
time_taken=default_timer() - time1

print 'Time taken to copyfile to bucket is %f' %(time_taken)
