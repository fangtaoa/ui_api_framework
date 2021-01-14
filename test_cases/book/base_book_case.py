import json
import os

from test_cases.base_case import BaseCase
from common.data import DataReader
from common.config import base_dir


class BaseBookCase(BaseCase):
	def __init__(self):
		super(BaseBookCase, self).__init__()
		self.all_case_list = []
		self.pre_conditions_set = set()
		self.token = None
		self.data_reader = DataReader("test_books_token.xls")

	def get_runnable_cases(self):
		data_list = self.data_reader.read_excel_data()
		header = data_list[0]
		runnable_case_list = []

		for item in data_list[1:]:
			self.all_case_list.append(dict(zip(header, item)))
		for case in self.all_case_list:
			if case["is_run"].lower() == "y".lower():
				runnable_case_list.append(case)
		for case in runnable_case_list:
			self.pre_conditions_set.add(case["pre_condition"])

		return runnable_case_list

	def get_header(self, headers):
		if isinstance(headers, float):
			headers = {"Content-Type": "application/json"}
			return headers
		if headers.strip():
			return json.loads(headers.replace("{token}", self.token))

	def request_pre_condition(self):
		"""执行该case的前置条件呢"""
		for case in self.all_case_list:
			for pre_condition in self.pre_conditions_set:
				if pre_condition == case["case_id"]:
					headers = self.get_header(case["headers"])
					data = json.loads(case["data"])
					self.get_token(case["url"], method=case["method"], json=data, headers=headers)
					return

	def get_token(self, url, **kwargs):
		r = self.requester.request(url, **kwargs)
		self.token = r.json()["access_token"]

	def change_url(self, url):
		kw = "{bookID}"
		if kw in url:
			return url.replace(kw, self.data_reader.read_content("book_id.txt"))
		return url

	def run_book_case(self, case_data):
		self.request_pre_condition()
		url = self.change_url(case_data["url"])
		method = case_data["method"]
		data = json.loads(case_data["data"]) if isinstance(case_data["data"], str) else ""
		headers = self.get_header(case_data["headers"])

		if method.lower() == "get":
			return self.requester.get(url, headers=headers)
		elif method.lower() == "post":
			r = self.requester.post(url, json=data, headers=headers)
			book_id = r.json()[0]["datas"]["id"]
			self.data_reader.write_content("book_id.txt", str(book_id))
			return r
		elif method.lower() == "put":
			return self.requester.put(url, json=data, headers=headers)
		elif method.lower() == "delete":
			return self.requester.delete(url, json=data, headers=headers)

	def clean(self):
		"""测试用例执行完毕,需要把环境恢复到初始状态"""
		os.remove(os.path.join(base_dir, "data", "book_id.txt"))


if __name__ == '__main__':
	c = BaseBookCase()

