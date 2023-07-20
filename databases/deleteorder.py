from connectmysqldbconfigs import *


def get_by_id(cursor,eid):
	sql = "select * from orders where oid = %s";
	cursor.execute(sql,[eid])
	return cursor.fetchone()


def delete(conn,eid):
	cursor = conn.cursor()
	query = "delete from orders where oid = %s;"
	try:
		record = get_by_id(cursor,eid)
		if record is None:
			print("Order is not found for given id")
		else:
			cursor.execute(query, [eid])
			conn.commit()
			print("Employedd is = {} deleted".format(eid))
	except(Exception,Error) as error:
		print(error)
	finally:
		if conn is not None:
			cursor.close()
			conn.close()
			print("connections are closed")

if __name__=='__main__':
	n = input("Enter orders id")
	delete(connect(),n)
