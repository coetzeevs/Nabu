import pymysql
import pymysql.cursors
import pandas as pd
# Connect to the database
connection = pymysql.connect(host='karel-sandbox.conflmsz3tjg.eu-west-1.rds.amazonaws.com',
user='dba',
password='juLKY8xIefhO',
db='sandbox',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
name = 'coetzee'
password = 'coetzee'

with connection.cursor() as cursor:
	# Read a single recor
	sql = "insert into login values('{0}', '{1}')".format(name, password)
	cursor.execute(sql)
	connection.commit()
	#result = pd.DataFrame(cursor.fetchall())
connection.close()

#print result