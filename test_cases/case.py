"""
1. 加载数据
2. 发送接口
3. 为用例封装一些方法

"""
import sys

from common.log import Log
from common.config import Config
from common.db import DB
from common.data import DataReader
import json
import requests


class Case(object):
	def __init__(self):
		self.logger = Log.get_logger()
		self.cf = Config()

	def load_data(self, data_file):
		self.data = DataReader(data_file)

	def set_env(self, env):
		self.env = env

	def run_case(self, case_data, var={}):
		url = self.cf.get_node_value("server", self.env) + case_data[1]
		data = case_data[4]

		if case_data[3].lower() == "form":
			data = json.loads(data)
			headers = {}
		else:
			headers = {"content-type": "application/json"}

		if case_data[2].lower() == "get":
			resp = requests.get(url=url)
		else:
			resp = requests.post(url=url, headers=headers, json=data)
		return resp

	def check_response(self):
		pass

	def check_db(self, sql_name, vars={}):
		pass
		# sql = self.data.get_sql(sql_name).format(**vars)
		# return self.db.exec_sql(sql)


if __name__ == "__main__":
	c = Case()
	c.set_env("test")
	c.load_data("test_user_data.xls")
	c.run_case("login")
