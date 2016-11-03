import MySQLdb

def query_db_with_single_condition(host, port, user, db, table, col, value):
	con = MySQLdb.connect(host=host, port=port, user=user, db=db)
	sql = 'select %s from %s where %s = %s' % (col, table, col, value)
	print 'QUERY STRING: %s' % (sql)
	cur = con.cursor()
	cur.execute(sql)
	res = [each[0] for each in cur.fetchall()]
	print res
	
