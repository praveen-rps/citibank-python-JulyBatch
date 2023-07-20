# This program will read the configuration properties 
# from the configuration file 

import configparser

def read_db_params():
	# read the properties from env file

	config = configparser.ConfigParser()
	config.read('local.env')
	return config
