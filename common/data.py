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

	def read_excel_data(self, sheet_name):
		"""读取excel中的数据"""
		if not os.path.exists(self.excel_file_path):
			Log.get_logger().error(f"file '{self.excel_file_path}' is not existed!")
			sys.exit(1)
		s = pd.ExcelFile(self.excel_file_path)
		df = s.parse(sheet_name)
		return df.values.tolist()


if __name__ == '__main__':
	reader = DataReader("test_user_data.xlsx")
	print(reader.read_excel_data("reg"))
	print(reader.read_excel_data("login"))
	print(reader.read_excel_data("sql"))
