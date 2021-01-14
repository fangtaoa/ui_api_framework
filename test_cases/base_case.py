from common.log import Log
from common.config import Config
from common.db import DB
from common.data import DataReader
from common.http_method import HTTPRequests


class BaseCase(object):
	def __init__(self):
		self.logger = Log.get_logger()
		self.cf = Config()
		self.requester = HTTPRequests()

	def load_data(self, data_file):
		self.data = DataReader(data_file)

	def set_env(self, env):
		self.env = env