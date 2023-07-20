

def get_records_count(cursor):
	cursor.execute("select * from orders")
	return len(cursor.fetchall())
