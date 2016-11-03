#!/bin/python 
import MySQLdb
import argparse

def clean_db_and_clean_data(host, port, user, db, table, col, value):
	con = MySQLdb.connect(host=host, port=port, user=user, db=db)
	sql = 'select %s from %s where %s = %s' % (col, table, col, value)
	print 'QUERY STRING: %s' % (sql)
	cur = con.cursor()
	cur.execute(sql)
	res = [each[0] for each in cur.fetchall()]
	print res
	if res:
		del_sql = 'delete from %s where %s = %s' % (table, col, value)
		print 'DELET STRING: %s' %(del_sql)

		cur.execute(del_sql)
		con.commit()


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--server', help='The host address')
	parser.add_argument('-p', '--port', help='port for the server', type=int)
	parser.add_argument('-u', '--user', help='user for the database')
	parser.add_argument('-d', '--database', help='name of the databaser')
	parser.add_argument('-t','--table', help='name of the table')
	parser.add_argument('-c', '--column', help='name of the column to query')
	parser.add_argument('-v', '--value', help='value for querying')

	args = parser.parse_args()
	clean_db_and_clean_data(host=args.server, port=args.port, user=args.user, db=args.database, table=args.table, col=args.column, value=args.value)


if __name__ == '__main__':
	main()