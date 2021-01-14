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
			from selenium.webdriver.chrome.options import Options
			chrome_options = Options()
			chrome_options.add_argument('--headless')  # 无界面
			chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
			chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
			chrome_options.add_argument('--disable-dev-shm-usage')
			chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
			_driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
	print(f"正在启动'{_driver}'浏览器")

	def close_driver():
		print("当全部用例执行完毕后, 关闭浏览器!")
		_driver.quit()

	request.addfinalizer(close_driver)
	return _driver
