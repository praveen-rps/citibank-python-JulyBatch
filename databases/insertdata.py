# python program to read the data from keyboard and insert into table
from connectmysqldbconfigs import *


try:
	conn = connect()
	cursor = conn.cursor()
	sql = "insert into orders(oid,orderitem,quantity) values (%s,%s,%s)"
	"""
	toid = int(input("Enter order id"))
	titem = input("Enter order item name")
	tqty = int(input("Enter order quantity"))
	
	data = [(toid,titem,tqty)]
   	"""
	data = [(11,'fridges',2),(12,'fans',5),(13,'lamps',10),(14,'tables',20),(15,'chairs',30)]

	cursor.executemany(sql,data)
	conn.commit()
	print("Record inserted....")

except(Exception,Error) as error:
	print("error")
   
