"""
1.从conf目录下的配置文件中读取各个段信息
2.返回项目的绝对路径
"""

import os
from configparser import ConfigParser
base_dir = os.path.dirname(os.path.dirname(__file__))


class Config(object):
	"""读取配置文件"""
	def __init__(self, conf_dir="conf", filename="default.conf"):
		self.conf_parser = ConfigParser()
		self.conf_parser.read(os.path.join(base_dir, conf_dir, filename))

	def get_node_value(self, node, option):
		return self.conf_parser.get(node, option)


if __name__ == '__main__':
	c = Config()
	print(c.get_node_value("runtime", "log_level"))


