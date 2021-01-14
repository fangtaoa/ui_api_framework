import os

import pytest

from common.log import Log
from pages.zentao_page import ZentaoPage
from  common.config import Config


class TestZentaoLogin():
	def setup_class(self):
		self.zentao = ZentaoPage(driver=None)

	@pytest.fixture(scope="function", autouse=True)
	def start_page(self, driver, env):
		Log.get_logger().info("让每个用例都从登录页开始")
		host = Config().get_node_value("server", env).split(":")
		driver.get("http://192.168.116.1:80/pro/user-login.html")
		driver.delete_all_cookies()
		driver.refresh()

	def test_login_success(self, driver):
		self.zentao.driver = driver
		self.zentao.submit_login("admin", "Ft123456")
		ret = self.zentao.login_result("admin")
		print(f"登录结果: {ret}")
		assert ret

	def test_login_fail(self, driver):
		self.zentao.driver = driver
		self.zentao.submit_login("admin", "Ft1234561")
		ret = self.zentao.get_alert()
		print(f"测试结果: {ret}")
		assert "登录失败" in ret


if __name__ == '__main__':
	pytest.main(["-v", "-s", f"{os.path.basename(__file__)}", "--env", "test"])
