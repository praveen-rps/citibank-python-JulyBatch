import mysql.connector
from mysql.connector import Error


try:
	conn  =mysql.connector.connect("localhost","accenture","root","root")
	if conn:
		print("Database connection established")
	else:
		print("Not connected")
except(Exception,Error) as error:
	print(error)