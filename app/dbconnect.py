def connect_login(name,password):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select sum(valid) as valid from (select case when user_name = '{0}' and password = '{1}' then 1 else 0 end as valid from login)aa".format(name, password)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	result = result.iat[0,0]
	return result

def get_all_customers():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select * from customer"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result

def get_customers(name):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select * from customer where bar_name = '{0}'".format(name)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result

def update_customer2(barname,dated):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "UPDATE customer SET last_called='{0}' WHERE bar_name='{1}'".format(dated,barname)
		cursor.execute(sql)
		connection.commit()
	connection.close()

def update_customer3(barname2):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "UPDATE customer SET last_visited=NOW() WHERE bar_name='{0}'".format(barname2)
		cursor.execute(sql)
		connection.commit()
	connection.close()

def register_user(name,password):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "insert into login values('{0}', '{1}')".format(name, password)
		cursor.execute(sql)
		connection.commit()
	connection.close()

def add_customer2(province,area,bar,person,number,email):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "insert into  customer values(NULL,'{0}','{1}', '{2}', '{3}', '{4}', '{5}',NULL, NULL)".format(province,area,bar,person,number,email)
		cursor.execute(sql)
		connection.commit()
	connection.close()
#def LoadStaging(test):
#	import pandas
#	import pymysql
#	import pymysql.cursors
#	
#	connection = pymysql.connect(host='karel-sandbox.conflmsz3tjg.eu-west-1.rds.amazonaws.com',
#	user='dba',
#	password='juLKY8xIefhO',
#	db='sandbox',
#	charset='utf8mb4',
#	cursorclass=pymysql.cursors.DictCursor)
#	
#	cur = connection.cursor()
#	
#	cur.execute("CREATE TABLE sandbox.stg_olx_genders (id INT,name VARCHAR(255),prob FLOAT);")
#	connection.commit()
#	
#	test.to_sql(name='stg_olx_genders', con=connection, if_exists='append',flavor='mysql', index = 0)
#	connection.commit()