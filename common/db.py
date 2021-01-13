"""
1.从配置文件中读取数据库配置
2.连接数据库
3.执行sql并返回所有结果
"""
import pymysql as pymysql

from common.config import Config


class DB(object):
	def __init__(self):
		cf = Config()
		self.conn = pymysql.connect(
			host=cf.get_node_value("db_test", "host"),
			port=int(cf.get_node_value("db_test", "port")),
			user=cf.get_node_value("db_test", "user"),
			passwd=cf.get_node_value("db_test", "passwd"),
			db=cf.get_node_value("db_test", "mysql"),
			charset="utf8")
		self.cur = self.conn.cursor()

	def get_all(self, sql):
		self.cur.execute(sql)
		return self.cur.fetchall()

	def get_one(self, sql):
		self.cur.execute(sql)
		return self.cur.fetchone()

	def __del__(self):
		self.cur.close()
		self.conn.close()


if __name__ == '__main__':
	db = DB()
	print(db.get_all("select * from user"))