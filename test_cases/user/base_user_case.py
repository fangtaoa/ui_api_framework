"""
1. 加载数据
2. 发送接口
3. 为用例封装一些方法

"""
import sys
import json

from test_cases.base_case import BaseCase


class BaseUserCase(BaseCase):
	def __init__(self):
		super(BaseUserCase, self).__init__()

	def run_user_case(self, case_data, var={}):
		url = self.cf.get_node_value("server", self.env) + case_data[1]
		data = case_data[4]

		if case_data[3].lower() == "form":
			data = json.loads(data)
			headers = {}
		else:
			headers = {"content-type": "application/json"}

		if case_data[2].lower() == "get".lower():
			resp = self.requester.get(url=url, is_session=True)
		else:
			resp = self.requester.post(url=url, is_session=True, headers=headers, json=data, )
		return resp

	def check_response(self):
		pass

	def check_db(self, sql_name, vars={}):
		pass
		# sql = self.data.get_sql(sql_name).format(**vars)
		# return self.db.exec_sql(sql)


if __name__ == "__main__":
	c = BaseUserCase()
	c.set_env("test")
	c.load_data("test_user_data.xls")
	c.run_case("login")
