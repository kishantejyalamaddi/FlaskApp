#Memcache effectiveness
import random
import sys
import pymysql as mysql
import memcache
import time
from decimal import *

#Connecting to memcache on AWS
memc = memcache.Client(["testcache.t70qbx.cfg.usw2.cache.amazonaws.com:11211"],debug=1);

conn=mysql.connect(user='testdb',password='hyd_1234',
	host='testdb.cv74yfhlg7sh.us-west-2.rds.amazonaws.com', database='testdb')

time1 = time.time()
#Searching Memcache if the query result is already present
testQuery = memc.get('runQueryfor200')
#If the query is not found 
if not testQuery:
    cursor = conn.cursor()
    lim= range(1,200)
    for count in lim:
        query = "SELECT * FROM earth WHERE mag like '2.%' ;"
        num = cursor.execute(query)
		result = cursor.fetchall()
        for row in result:
            print row
    #Set the result as a key value pair in Memcache
	memc.set('runQueryfor200',rows,200)
	print "Memcache is updated with new data"
#If data found in memcache get data from it directly
else:
    print "Data found in memcache"
    for row in testQuery:
        print row
    print("Loaded from Memcache!")
time2 = time.time()
#Calculating time taken to get or set data from memcache
print("Total Time taken is:")
ftime = ime2-time1
print ftime
#Close connection
conn.close()
