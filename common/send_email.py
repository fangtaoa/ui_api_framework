"""
1.从配置文件读取smtp配置
2.从report文件夹下打开report.html, 发送邮件
"""


import smtplib
import sys
from email.mime.text import MIMEText
import os

from common.config import Config, base_dir
from common.log import Log


def send_email(report_name):
	"""把测试报告发送出去"""
	cf = Config()
	logger = Log.get_logger()
	report_file = os.path.join(base_dir, cf.get_node_value("runtime", "report_dir"), os.path.basename(report_name))

	with open(report_file, "rb") as f:
		body = f.read()

	# 格式化email正文
	msg = MIMEText(body, "html", "utf-8")

	msg["Subject"] = cf.get_node_value("email", "subject")
	msg["From"] = cf.get_node_value("email", "username")
	msg["To"] = cf.get_node_value("email", "receiver")

	# 连接smtp服务器, 发送邮件
	smtp = smtplib.SMTP()
	try:
		smtp.connect(
			host=cf.get_node_value("email", "mail_host"),
			port=int(cf.get_node_value("email", "mail_port")))
		smtp.login(cf.get_node_value("email", "username"), cf.get_node_value("email", "password"))
		smtp.sendmail(cf.get_node_value("email", "username"), cf.get_node_value("email", "receiver"), msg.as_string())
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	print("邮件发送成功")


if __name__ == '__main__':
	send_email("test_report.html")

