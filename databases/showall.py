# python program to display the records of the given table
from connectmysqldbconfigs import *
from utils import *

try:
	conn = connect()
	cursor = conn.cursor()
	print("cursor successful")
	cnt = get_records_count(cursor)
	print("records count successful")
	if cnt == 0:
		print("NO records found")
	else:
		sql = "select * from orders"
		cursor.execute(sql)
		records = cursor.fetchall()
		print("Orders Information")
		print("------------------")
		for record in records:
			print("Order id = {}, Description = {}, Quantity = {}".format(record[0],record[1],record[2]))
except(Exception,Error) as error:
	print("error")
   
