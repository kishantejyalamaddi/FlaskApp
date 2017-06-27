import boto
import uuid
import boto.s3.connection
import mysql.connector
import csv
import time
import urllib
import itertools

#AWS Credentials to establish connection with S3 and RDS
AWS_ACCESS_KEY_ID='AKIAIVPX4M6XPLQXKKIQ'
AWS_SECRET_ACCESS_KEY = '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'
s3 = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,is_secure = False)

#Access the file from the bucket
bucket = s3.lookup('cloud93')
key = bucket.lookup('UNPrecip3.csv')

#Establish connectio with my RDS
conn=mysql.connector.connect(user='testdb',password='hyd_1234',
	host='testdb.cv74yfhlg7sh.us-west-2.rds.amazonaws.com', database='testdb')
print 'Connected to mySQL'
cursor= conn.cursor()

opens=urllib.URLopener()
#reading data to be inserted from the bucket
link="https://s3.amazonaws.com/cloud93/UNPrecip3.csv"
f=opens.open(link)
csvfile= csv.reader(f)
#calculating time taken to insert
time1 = int(time.time())
for row in itertools.islice(csvfile, 1,None):
	#executing the insert query
	query_1="""Insert into testdb.UNPrecipnw values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
	cursor.execute(query_1,row)
	conn.commit()
cursor.close()
time2 = int(time.time())
time = endTime - startTime
print 'total time is '+str(time)+' seconds'
