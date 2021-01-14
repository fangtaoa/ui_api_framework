"""
1.从Excel中读取接口数据
2.读取SQL语句
"""
import os
import sys
import pandas as pd

from common.config import base_dir
from common.log import Log


class DataReader(object):
	def __init__(self, filename, data_dir="data"):
		self.excel_file_path = os.path.join(base_dir, data_dir, filename)

	def read_excel_data(self, sheet_name=None):
		"""读取excel中的数据"""
		if not os.path.exists(self.excel_file_path):
			Log.get_logger().error(f"file '{self.excel_file_path}' is not existed!")
			sys.exit(1)

		s = pd.ExcelFile(self.excel_file_path)

		if not sheet_name:
			df = s.parse(sheet_name=0, header=None)
		else:
			df = s.parse(sheet_name=sheet_name, header=None)
		return df.values.tolist()

	def write_content(self, filename, content, data_dir="data"):
		"""写入数据到文件中"""
		with open(os.path.join(base_dir, data_dir, filename), mode="w", encoding="utf-8") as f:
			f.write(str(content))

	def read_content(self, filename, data_dir="data"):
		"""读取文件中的数据"""
		with open(os.path.join(base_dir, data_dir, filename), mode="r", encoding="utf-8") as f:
			return f.read()


if __name__ == '__main__':
	reader = DataReader("test_user_data.xlsx")
	print(reader.read_excel_data("reg"))
	print(reader.read_excel_data("login"))
	print(reader.read_excel_data("sql"))
