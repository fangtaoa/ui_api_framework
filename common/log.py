"""
1.配置log输出格式 time - log level - file - func - line -msg
2.支持输出到log文件及屏幕
3.支持返回一个logger, 让其他模块调用
"""


import logging
import time
import os

from common.config import Config, base_dir


class Log(object):
	@classmethod
	def config_log(cls):
		cf = Config()
		log_dir = os.path.join(base_dir, cf.get_node_value("runtime", "log_dir"))
		today = time.strftime("%Y%m%d", time.localtime(time.time()))
		log_file = os.path.join(log_dir, today + ".log")

		# 获取一个标准的logger, 配置loglevel
		cls.logger = logging.getLogger()

		cls.logger.setLevel(eval("logging." + cf.get_node_value("runtime", "log_level").upper()))

		# 创建不同的handler
		file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
		console_handler = logging.StreamHandler()

		# 定义输出格式
		file_handler_format = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
		file_handler.setFormatter(file_handler_format)
		console_handler.setFormatter(file_handler_format)

		# 把定制的handler 添加到logger中
		cls.logger.addHandler(file_handler)
		cls.logger.addHandler(console_handler)

	@classmethod
	def get_logger(cls):
		cls.config_log()
		return cls.logger


if __name__ == '__main__':
	logger = Log.get_logger()
	logger.info("abc")
