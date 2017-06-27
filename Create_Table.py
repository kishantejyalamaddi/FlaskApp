import boto
import uuid
import time
import boto.s3.connection
import pymysql as mysql
#Credentials to access the bucket
AWS_ACCESS_KEY_ID='AKIAIVPX4M6XPLQXKKIQ'
AWS_SECRET_ACCESS_KEY = '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'

#Connect to the bucket to create table
s3 = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,is_secure = False)
bucket = s3.lookup('cloud93')
key = bucket.lookup('UNPrecip.csv')
print key

#Connect to the db
try:
	conn=mysql.connect(user='testdb',password='hyd_1234',
		host='testdb.cv74yfhlg7sh.us-west-2.rds.amazonaws.com', database='testdb')
except:
	print "Error in connection"
	
cursor=conn.cursor()
time1 = int(time.time())
#Create a table to upload the all_month.csv file to RDS
cursor.execute("""create table testdb.UNPrecip2 (Country_or_Territory varchar(50),Station_Name varchar(50),WMO_Station_Number varchar(50),Unit varchar(10),Jan float(10,3),Feb float(10,3),Mar float(10,3),Apr float(10,3),May float(10,3),Jun float(10,3),Jul float(10,3),Aug float(10,3),Sep float(10,3),Oct float(10,3),Nov float(10,3),Decm float(10,3));""")

cursor.execute("show tables")
print cursor.fetchall()
time2 = int(time.time())
time = time2 - time1
print 'Time taken to create is '+str(totalTime)+' seconds'
