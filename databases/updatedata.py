from connectmysqldbconfigs import *

def get_by_id(cursor,eid):
	sql = "select * from orders where oid = %s";
	cursor.execute(sql,[eid])
	return cursor.fetchone()


def update(conn,eid):
	cursor = conn.cursor()
	query = "update orders set orderitem = %s where oid = %s;"
	try:
		record = get_by_id(cursor,eid)
		if record is None:
			print("Order id is not found")
		else:
			cdata = input("Enter the new item name")
			cursor.execute(query,[cdata,eid])
			conn.commit()
			print("order id {} is updated".format(eid))
	except:
		print("Error occured")
		conn.rollback()
		
	finally:
		if conn is not None:
			cursor.close()
			conn.close()
			print("Connections are closed")

if __name__=='__main__':
	update(connect(),int(input("enter order id to update")))



