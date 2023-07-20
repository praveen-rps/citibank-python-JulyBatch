import mysql.connector
from mysql.connector import Error

from readdbconfig import *

def connect():
	try:
		# read the env file and get the configurations
		params = read_db_params()
		
		conn = mysql.connector.connect(
				 host = params.get('DB','host'),
				 database = params.get('DB','database'),
				 user = params.get('DB','username'),
				 password = params.get('DB','password'),
				 port = params.get('DB','port')
		)
		print("connection successfull")
		return conn
	except(Exception, Error) as error:
		print(error)


				
		
