import mysql.connector
from mysql.connector import Error


try:
	conn  =mysql.connector.connect(host="localhost",database="citibank",user="root",password="root",port="3306")
	if conn:
		print("Database connection established")
	else:
		print("Not connected")
	cursor = conn.cursor()
	sql = "create table orders1(oid int not null, orderitem varchar(20), quantity int)";
	cursor.execute(sql)
	print("Table is created")
except(Exception,Error) as error:
	print(error)