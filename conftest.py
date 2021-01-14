import pytest
from selenium import webdriver


def pytest_addoption(parser):
	parser.addoption(
		"--env", action="store", default="test", help="set env"
	)
	parser.addoption(
		"--browser", action="store", default="chrome", help="browser option: firefox or chrome"
	)


@pytest.fixture(scope="session")
def env(request):
	"""获取测试环境参数"""
	return request.config.getoption("--env")


_driver = None


@pytest.fixture(scope="session")
def driver(request):
	"""全局driver"""
	global _driver
	if not _driver:
		name = request.config.getoption("--browser")
		if hasattr(webdriver, name.title()):
			_driver = getattr(webdriver, name.title())()
		else:
			_driver = webdriver.Chrome()
	print(f"正在启动'{_driver}'浏览器")

	def close_driver():
		print("当全部用例执行完毕后, 关闭浏览器!")
		_driver.quit()

	request.addfinalizer(close_driver)
	return _driver
